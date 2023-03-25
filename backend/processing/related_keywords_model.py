import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import defaultdict

# Download NLTK stopwords
import nltk

from backend.processing.preprocessing import preprocess_job
from backend.scrapers.linkedin import get_jobs_data

nltk.download('stopwords')
nltk.download('punkt')


def train_keyword_model(descriptions):
    vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
    X = vectorizer.fit_transform(descriptions)

    # Train K-means clustering model
    model = KMeans(n_clusters=5)
    model.fit(X)

    # Get top keywords for each cluster
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()
    cluster_keywords = defaultdict(list)

    for i in range(model.n_clusters):
        for ind in order_centroids[i, :10]:
            cluster_keywords[i].append(terms[ind])

    return model, cluster_keywords, vectorizer


def find_related_keywords(keyword, model, cluster_keywords, vectorizer):
    query = vectorizer.transform([keyword])
    cluster = model.predict(query)[0]

    related_keywords = {
        keyword: [word for word in cluster_keywords[cluster] if word != keyword.lower()]
    }

    return related_keywords


if __name__ == '__main__':
    keywords = "fullstack&location=Israel"
    df = get_jobs_data(keywords)
    existing_data = pd.read_excel('data.xlsx', dtype=str).astype(str)

    if not df.empty:
        combined_data = pd.concat([existing_data, df], axis=0, ignore_index=True)
        combined_data = combined_data.drop_duplicates()
        combined_data = combined_data.reset_index(drop=True)
        combined_data.to_excel('data.xlsx', index=False)

        combined_data['description'] = combined_data['description'].apply(preprocess_job)
        combined_data['title'] = combined_data['title'].apply(preprocess_job)
        combined_data['title_and_description'] = combined_data['title'] + ' ' + combined_data['description']

        # Train the model
        model, cluster_keywords, vectorizer = train_keyword_model(combined_data['title_and_description'].tolist())

        # Find related keywords
        related_keywords = find_related_keywords("fullstack", model, cluster_keywords, vectorizer)
        print(related_keywords)
