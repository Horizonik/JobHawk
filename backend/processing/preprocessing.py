import re

import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from word2number import w2n

nltk.load('stopwords')
nltk.load('wordnet')


def preprocess_job(job_description: str) -> str:
    job_description = job_description.lower().strip()

    # Remove HTML tags and URLs
    job_description = re.sub('<[^<]+?>', '', job_description)
    job_description = re.sub(r'http\S+', '', job_description)
    job_description = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+', '', job_description)
    job_description = re.sub(r'[\\/×\^\]\[÷]', ' ', job_description)

    # Tokenize the text into individual words
    words = nltk.word_tokenize(job_description)

    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    pattern = re.compile('^[a-zA-Z0-9_]*$')
    filtered_tokens = [w for w in words if w not in stop_words and pattern.match(w)]

    # Replace number words with numeric equivalents
    for i in range(len(filtered_tokens)):
        token = filtered_tokens[i]

        if not token.isdigit():
            try:
                token_as_digit = w2n.word_to_num(token)
                if token_as_digit is not None:
                    filtered_tokens[i] = str(token_as_digit)

            except ValueError:
                continue

    # Apply lemmatization to the words
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return " ".join(lemmatized_tokens)
