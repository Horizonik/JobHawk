import pandas as pd
import spacy
from collections import Counter

from .preprocessing import preprocess_job

nlp = spacy.load('en_core_web_sm')

"""
Calculates the requirements for the job based on the description and title,
Use the calculate_requirements() func to start the chain of calculations
"""


def extract_skills(text: str) -> list:
    doc = nlp(text)
    skills = []
    for ent in doc.ents:
        if ent.label_ == 'PRODUCT' or ent.label_ == 'ORG':
            skills.append(ent.text.lower())
    return skills


def extract_keywords(text: str) -> list[str]:
    doc = nlp(text)
    keywords = []
    for token in doc:
        if token.is_stop is False and token.is_punct is False and (token.pos_ == 'NOUN' or token.pos_ == 'ADJ'):
            keywords.append(token.text.lower())
    return keywords


def extract_title(job_title: str) -> str:
    doc = nlp(job_title)
    title = ''
    for token in doc:
        if token.is_title:
            title += token.text + ' '
    return title.strip()


def rank_skills(description: str, job_title: str) -> list[str]:
    """
    Uses multiple different extractions and ranks the words that came up
    based on how many times they came up, the top 5 words are taken as requirements
    """

    skills = extract_skills(description)
    keywords = extract_keywords(description)
    title = extract_title(job_title)
    matches = Counter(skills + keywords + title.split())
    ranked = matches.most_common()
    top5 = [x[0] for x in ranked[:5]]
    return top5


def calculate_requirements(dataset: pd.DataFrame) -> pd.DataFrame:
    """Adds a requirements' column, that contains the requirements extracted with nlp"""

    dataset['description'] = dataset['description'].apply(lambda job_desc: preprocess_job(job_desc, False))
    dataset['requirements'] = dataset.apply(lambda row: rank_skills(row['description'], row['title']), axis=1)
    return dataset
