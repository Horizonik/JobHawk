from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import defaultdict


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


# if __name__ == '__main__':
#
#     keywords_list = ["fullstack%20engineer", "data%20scientist", "machine%20learning", "backend%20developer", "frontend%20developer", "data", "engineer", "developer", "software", "data%20analyst", "QA", "automation", "django", "react", "java", "c#", "python"]
#     location = "Israel"
#
#     # dataset = pd.read_excel('../data.xlsx', dtype=str).astype(str)
#     # combined_data = existing_data.copy()
#     dataset = pd.DataFrame(columns=['title', 'company', 'location', 'description', 'url'])
#
#     try:
#         with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
#             func = partial(get_jobs_for_keyword, location=location)
#             results = list(executor.map(func, keywords_list))
#
#         for df in results:
#             if not df.empty:
#                 dataset = pd.concat([dataset, df], axis=0, ignore_index=True)
#
#         dataset = dataset.drop_duplicates()
#         dataset = dataset.reset_index(drop=True)
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         save_data_to_excel(dataset, '../crashed_data.xlsx')
#
#     if not dataset.empty:
#         # preprocessing
#         dataset['description'] = dataset['description'].apply(preprocess_job)
#         dataset['title'] = dataset['title'].apply(preprocess_job)
#
#         # model training
#         dataset['title_and_description'] = dataset['title'] + ' ' + dataset['description']
#         model, cluster_keywords, vectorizer = train_keyword_model(dataset['title_and_description'].tolist())
#
#         # Add related keywords column
#         dataset['related_keywords'] = dataset['title'].apply(lambda job_title: find_related_keywords(job_title, model, cluster_keywords, vectorizer))
#
#         # add requirements column
#         dataset = calculate_requirements(dataset)
#
#         # save new data
#         # dataset = dataset.drop_duplicates()
#         dataset = dataset.reset_index(drop=True)
#         save_data_to_excel(dataset, '../data.xlsx')
