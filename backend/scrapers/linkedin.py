import os

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import concurrent.futures
from functools import partial

headers = {'User-Agent': 'JobHawk'}


def get_job_listings(keywords: str) -> list[dict] | None:
    url = f'https://www.linkedin.com/jobs/search?keywords={keywords}'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error retrieving page: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    job_listings = soup.select('ul.jobs-search__results-list li')

    if not job_listings:
        print("No results for keywords")
        return None

    # extract data for every job listing and save in list of dicts
    jobs = [
        {
            'title': job.select_one('h3.base-search-card__title').text.strip(),
            'company': company_element.text.strip() if (company_element := job.select_one(
                'h4.base-search-card__subtitle a')) and company_element.text.strip() else None,
            'location': job.select_one('span.job-search-card__location').text.strip(),
            'description': get_job_description(job.find('a').get('href')) if (description_page := job.find('a')) and (
                href := description_page.get('href')) else None,
        }
        for job in job_listings
    ]

    return jobs


def get_job_description(description_page_url: str) -> str | None:
    response = requests.get(description_page_url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    # Try to get the job description from the JSON-LD script tag
    job_description_container = soup.find("script", {"type": "application/ld+json"})
    if job_description_container:
        json_data = json.loads(job_description_container.string)
        job_description = json_data.get("description")
        if job_description:
            return job_description

    # Try to get the job description from the div element containing the description
    job_description_container = soup.find("div", class_="show-more-less-html__markup")
    if job_description_container:
        return job_description_container.text.strip()

    return None


def jobs_to_dataframe(job_listings: list[dict]) -> pd.DataFrame:
    """Convert job listings list into a dataframe"""

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


if __name__ == '__main__':
    keywords_list = ["fullstack", "data%20scientist", "machine%20learning", "backend", "frontend", "data", "engineer",
                     "developer", "software"]
    location = "Israel"

    existing_data = pd.read_excel('data.xlsx', dtype=str).astype(str)
    combined_data = existing_data.copy()

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        func = partial(get_jobs_for_keyword, location=location)
        results = list(executor.map(func, keywords_list))

    for df in results:
        if not df.empty:
            combined_data = pd.concat([combined_data, df], axis=0, ignore_index=True)

    combined_data = combined_data.drop_duplicates()
    combined_data = combined_data.reset_index(drop=True)
    combined_data.to_excel('data.xlsx', index=False)
