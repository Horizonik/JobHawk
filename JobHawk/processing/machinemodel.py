import random

import pandas as pd
from nltk import WordNetLemmatizer
import re
import nltk
from nltk.corpus import stopwords
import spacy
from spacy.tokens import Doc, Span, Token
from word2number import w2n

# Download the required NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Load the pre-trained English language model in spaCy
nlp = spacy.load('en_core_web_sm')

# DATA PREPERATION
# todo call scraper here
job_descriptions = [
    """At least five years of proven experience as a Python backend developer experience designing and maintaining production systems in microservices environments Strong familiarity with cloud platforms such as AWS, Azure, or Google Cloud. Desirable qualifications include experience working in a small startup, familiarity with AWS CloudFormation, and expertise with CI/CD pipelines.""",
    """- Two years of managerial experience
    - 4 years of experience in backend development
    - Extensive experience in Python development
    - Experience in developing with SQL over Linux
    - Bachelor's degree in software engineering/computer science - an advantage
    - Experience working with DevOps technologies, Docker/K8s - an advantage
    """,
    'Our company is seeking a sales representative with excellent communication skills and a proven track record of meeting sales targets']


# DATA PREPROCESSING
def preprocess_job(job_description: str) -> str:
    job_description = job_description.lower()

    # Remove HTML tags and URLs
    job_description = re.sub('<[^<]+?>', '', job_description)
    job_description = re.sub(r'http\S+', '', job_description)

    # Tokenize the text into individual words
    words = nltk.word_tokenize(job_description)

    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    pattern = re.compile('^[a-zA-Z0-9_]*$')
    filtered_tokens = [w for w in words if w.lower() not in stop_words and pattern.match(w)]

    # Replace number words with numeric equivalents
    for i in range(len(filtered_tokens)):
        token = filtered_tokens[i]

        if not token.isdigit():
            try:
                token_as_digit = w2n.word_to_num(token)
                if token_as_digit is not None:
                    filtered_tokens[i] = str(token_as_digit)

            except ValueError:
                pass

    # Apply lemmatization to the words
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return " ".join(lemmatized_tokens)


preprocessed_jobs = [preprocess_job(job_description) for job_description in job_descriptions]
print(preprocessed_jobs)