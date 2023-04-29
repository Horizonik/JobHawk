import re
import time

import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from word2number import w2n
from googletrans import Translator

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()


def to_lower(text: str) -> str:
    return text.lower().strip()


def preprocess_job(job_description: str, convert_to_lower=True) -> str:
    if convert_to_lower:
        job_description = to_lower(job_description)

    job_description = remove_script_leftovers(job_description)

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
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return " ".join(lemmatized_tokens)


def translate_to_english(hebrew_text, source_language='he', target_language='en') -> str:
    """Translates Hebrew text to English text"""

    translator = Translator(service_urls=['translate.google.com'])
    retries = 5
    for attempt in range(retries):  # Retry up to 5 times
        try:
            translation = translator.translate(hebrew_text, src=source_language, dest=target_language)
            return translation.text
        except Exception as e:
            print(f"Translation error: {e}")
            print(f"Retrying in {attempt + 1} seconds...")
            time.sleep(attempt + 1)
    # Raise an error if translation fails after 5 retries
    raise Exception("Failed to translate text after 5 retries.")


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


def remove_script_leftovers(text):
    regex = r"\b(?:p\.?|li\.?|ul\.?|span\.?|lt\.?|br\.?|gt\.?|strong\.?|summary\.?|nbsp\.?|amp\.?)\b[^.]*\."
    return re.sub(regex, "", text, flags=re.IGNORECASE)
