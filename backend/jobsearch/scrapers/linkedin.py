import requests
import os
import json
import pandas as pd
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'JobHawk'}


def get_job_listings(keywords: str) -> list[dict] | None:
    url = f'https://www.linkedin.com/jobs/search?keywords={keywords}'
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error retrieving page: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    job_listings = soup.select('ul.jobs-search__results-list li')

    if not job_listings:
        print("No results for keywords")
        return None

    jobs = []
    for job in job_listings:
        title = job.select_one('h3.base-search-card__title').text.strip()
        company_element = job.select_one('h4.base-search-card__subtitle a')
        company = company_element.text.strip() if company_element and company_element.text.strip() else None
        location = job.select_one('span.job-search-card__location').text.strip()
        description_page = job.find('a')
        url = description_page.get('href') if description_page else None
        description = get_job_description(url) if url else None

        job_info = {
            'title': title,
            'company': company,
            'location': location,
            'description': description,
            'url': url
        }
        jobs.append(job_info)

    return jobs


def get_job_description(description_page_url: str) -> str | None:
    response = requests.get(description_page_url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    job_description_container = soup.find("script", {"type": "application/ld+json"})
    if job_description_container:
        json_data = json.loads(job_description_container.string)
        job_description = json_data.get("description")
        if job_description:
            cleaned_description = BeautifulSoup(job_description, 'html.parser').get_text(separator=' ')
            return cleaned_description

    job_description_container = soup.find("div", class_="show-more-less-html__markup")
    if job_description_container:
        cleaned_description = job_description_container.get_text(separator=' ').strip()
        return cleaned_description

    return None


def jobs_to_dataframe(job_listings: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(job_listings)
    df.fillna('-', inplace=True)
    return df


def get_jobs_data(keywords: str) -> pd.DataFrame | None:
    job_listings = get_job_listings(keywords)

    if job_listings:
        df = jobs_to_dataframe(job_listings)
        print(f"Worker {os.getpid()} finished processing keyword: {keywords}")
        return df

    return pd.DataFrame()


def get_jobs_for_keyword(keyword: str, location: str) -> pd.DataFrame:
    return get_jobs_data(f"{keyword}&location={location}")


def save_data_to_excel(df, file_path):
    with pd.ExcelWriter(file_path) as writer:
        df.to_excel(writer, index=False)
