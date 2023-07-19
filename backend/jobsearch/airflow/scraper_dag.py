import concurrent
from functools import partial
import pandas as pd

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scrapers.linkedin import get_jobs_for_keyword, save_data_to_excel
from processing.preprocessing import preprocess_job
from processing.related_keywords_handler import train_keyword_model, find_related_keywords
from processing.data_handler import save_data_to_db
from backend.jobsearch.processing.requirements_handler import calculate_requirements
from parameters import keywords_list, location


def scrape_jobs():
    global dataset

    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
            func = partial(get_jobs_for_keyword, location=location)
            results = list(executor.map(func, keywords_list))

        for df in results:
            if not df.empty:
                dataset = pd.concat([dataset, df], axis=0, ignore_index=True)

        dataset = dataset.drop_duplicates()
        dataset = dataset.reset_index(drop=True)

    except Exception as e:
        print(f"An error occurred: {e}")


def process_data():
    global dataset

    if not dataset.empty:
        dataset['description'] = dataset['description'].apply(preprocess_job)
        dataset['title'] = dataset['title'].apply(preprocess_job)

        dataset['title_and_description'] = dataset['title'] + ' ' + dataset['description']
        model, cluster_keywords, vectorizer = train_keyword_model(dataset['title_and_description'].tolist())

        dataset['related_keywords'] = dataset['title'].apply(
            lambda job_title: find_related_keywords(job_title, model, cluster_keywords, vectorizer)
        )

        dataset = calculate_requirements(dataset)

        dataset = dataset.reset_index(drop=True)


def save_data():
    global dataset
    save_data_to_db(dataset)


default_args = {
    'owner': 'gemesil',
    'start_date': datetime(2023, 7, 18),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'scrape_process_dag',
    default_args=default_args,
    description='Scrapes and processes job listings',
    schedule_interval='@daily',
) as dag:

    scrape_task = PythonOperator(
        task_id='scrape_jobs',
        python_callable=scrape_jobs,
    )

    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        trigger_rule='all_success',
    )

    save_task = PythonOperator(
        task_id='save_data',
        python_callable=save_data,
        trigger_rule='all_success',
    )

    scrape_task >> process_task >> save_task
