from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import defaultdict

def train_keyword_model(descriptions):
    vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english')
    x = vectorizer.fit_transform(descriptions)

    model = KMeans(n_clusters=5)
    model.fit(x)

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
