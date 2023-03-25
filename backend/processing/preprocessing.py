import re

import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from word2number import w2n
from googletrans import Translator

nltk.load('stopwords')
nltk.load('wordnet')


def preprocess_job(job_description: str) -> str:
    job_description = job_description.lower().strip()

    if contains_hebrew(job_description):
        job_description = translate_to_english(job_description)

    job_description = remove_unwanted_characters(job_description)

    # Tokenize the text into individual words
    words = nltk.word_tokenize(job_description)

    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    pattern = re.compile('^[a-zA-Z0-9_]*$')
    filtered_tokens = [w for w in words if w not in stop_words and pattern.match(w)]

    # Replace number words with numeric equivalents
    filtered_tokens = numbers_to_words(filtered_tokens)

    # Apply lemmatization to the words
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return " ".join(lemmatized_tokens)


def translate_to_english(hebrew_text, source_language='he', target_language='en') -> str:
    """Translates hebrew text to english text"""

    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(hebrew_text, src=source_language, dest=target_language)
    return translation.text


def numbers_to_words(filtered_tokens: list) -> list:
    """
    Receives list of words and numbers, converts the numbers to english words.
    Ex: '5' to 'five'.
    """

    for i in range(len(filtered_tokens)):
        token = filtered_tokens[i]

        if not token.isdigit():
            try:
                token_as_digit = w2n.word_to_num(token)
                if token_as_digit is not None:
                    filtered_tokens[i] = str(token_as_digit)

            except ValueError:
                continue

    return filtered_tokens


def contains_hebrew(text):
    hebrew_regex = re.compile(r'[\u0590-\u05FF]')
    return bool(hebrew_regex.search(text))


def remove_unwanted_characters(text: str) -> str:
    """
    Regex pattern breakdown:
    1. Remove HTML tags
    2. Remove URLs starting with 'http'
    3. Remove any character that is not a space, newline, alphanumeric, or specific accented characters
    4. Remove specific special characters: '/', '\', '×', '^', ']', '[', '÷'
    """

    combined_pattern = r'<[^<]+?>' + '|' + \
                       r'http\S+' + '|' + \
                       r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+' + '|' + \
                       r'[\\/×\^\]\[÷]'
    return re.sub(combined_pattern, ' ', text)
