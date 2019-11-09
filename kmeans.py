from sklearn.cluster import KMeans
from tfidf import tfidf_matrix, terms
from sklearn.externals import joblib

# TODO: 调高
num_clusters = 5
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
# joblib.dump(km, 'doc_cluster.pkl')
km = joblib.load('doc_cluster.pkl')
clusters = km.labels_.tolist()

# Here is some fancy indexing and sorting on each cluster to identify which are the top n (I chose n=6) words that are
# nearest to the cluster centroid. This gives a good sense of the main topic of the cluster.
from preprocess import vocab_frame, titles, authors, groups, keywords, topics, abstracts
import pandas as pd
papers = {'titles': titles, 'authors': authors, 'groups': groups,
          'keywords': keywords, 'topics': topics, 'abstracts': abstracts, 'cluster': clusters}
frame = pd.DataFrame(papers, index=[clusters], columns=['titles', 'authors', 'groups', 'keywords', 'topics', 'cluster'])
# print(frame['cluster'].value_counts())

print("Top terms per cluster:")
# sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1]

for i in range(num_clusters):
    print("Cluster %d words:" % i, end='')

    for ind in order_centroids[i, :6]:  # TODO: replace 6 with n words per cluster
        print(' %s' % vocab_frame.loc[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print()

    print("Cluster %d titles:" % i, end='')
    for title in frame.loc[i]['titles'].values.tolist():
        print(' %s,' % title, end='')
    print()