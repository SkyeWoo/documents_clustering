from sklearn.cluster import KMeans
from tfidf import tfidf_matrix, terms
from sklearn.externals import joblib

# TODO: 调高
num_clusters = 22
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
# joblib.dump(km, 'doc_cluster_22.pkl')  # TODO
km = joblib.load('doc_cluster_22.pkl')
clusters = km.labels_.tolist()

# Here is some fancy indexing and sorting on each cluster to identify which are the top n (I chose n=6) words that are
# nearest to the cluster centroid. This gives a good sense of the main topic of the cluster.
from preprocess import vocab_frame, labels, dic
import pandas as pd
papers = {'labels': labels, 'cluster': clusters}
frame = pd.DataFrame(papers, index=[clusters], columns=['labels', 'cluster'])
# print(frame['cluster'].value_counts())
print("Top terms per cluster:")
# sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
dic_rate = {}
for i in range(num_clusters):
    dic_rate_temp = {}
    print("Cluster %d words:" % i, end='')

    for ind in order_centroids[i, :6]:  # TODO: replace 6 with n words per cluster
        print(' %s' % vocab_frame.loc[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print()

    print("Cluster %d labels:" % i, end='')
    for label in frame.loc[i]['labels'].values.tolist():
        print(' %s,' % label, end='')
        for k in label:
            dic_rate_temp[k] = dic_rate_temp.get(k, 0) + 1

    # max cluster rate
    for t in dic_rate_temp:
        if dic_rate_temp[t] > dic_rate.get(k, 0):
            dic_rate[t] = dic_rate_temp[t]
    print()

# metric
import math
loss = 0
for t in dic_rate:
    rate = dic_rate[t] / dic[t]
    loss += - rate * math.log2(rate) - (1-rate) * math.log2(1 - rate)

loss /= len(dic)
print(loss)