import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import defaultdict

from backend.processing.preprocessing import preprocess_job
from backend.processing.requirements_handler import calculate_requirements


def train_keyword_model(descriptions):
    vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
    x = vectorizer.fit_transform(descriptions)

    # Train K-means clustering model
    model = KMeans(n_clusters=5)
    model.fit(x)

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
    dataset = pd.read_excel('../data.xlsx', dtype=str).astype(str)

    if not dataset.empty:
        # preprocessing
        dataset['description'] = dataset['description'].apply(preprocess_job)
        dataset['title'] = dataset['title'].apply(preprocess_job)

        # model training
        dataset['title_and_description'] = dataset['title'] + ' ' + dataset['description']
        model, cluster_keywords, vectorizer = train_keyword_model(dataset['title_and_description'].tolist())

        # Add related keywords column
        dataset['related_keywords'] = dataset['title'].apply(lambda job_title: find_related_keywords(job_title, model, cluster_keywords, vectorizer))

        # add requirements column
        dataset = calculate_requirements(dataset)

        # save new data
        # dataset = dataset.drop_duplicates()
        dataset = dataset.reset_index(drop=True)
        dataset.to_excel('updated_data.xlsx', index=False)
