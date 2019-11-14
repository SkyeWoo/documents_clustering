# encoding:utf -8
"""
@version:3.7
@author:lc
@file:Entropy
@time: 18:21
"""
import numpy as np
from sklearn.cluster import DBSCAN
from tfidf import tfidf_matrix
import pandas as pd
from sklearn import metrics
from scipy.spatial.distance import minkowski

# tfidf_matrix = tfidf_matrix.toarray()
# result = DBSCAN(eps=0.1, min_samples=4, metric='cosine').fit(tfidf_matrix)

# df = pd.DataFrame(tfidf_matrix)
# df['labels'] = result.labels_
# silhouette = metrics.silhouette_score(tfidf_matrix, df['labels'])  # computing the silhouette score for each cluster

# tfidf_matrix= tfidf_matrix.toarray()
eps = np.arange(0.1, 4, 0.05)
num = np.arange(4, 20, 1)

max_score = 0
max_eps = 0
max_num = 0
eps_num_silhouette = []
score = []


for i in eps:
    for j in num:
        try:
            db = DBSCAN(eps=i, min_samples=j, metric='cityblock').fit(tfidf_matrix)
            labels = db.labels_
            silhouette = metrics.silhouette_score(tfidf_matrix, labels, metric='cityclock')
            score.append(silhouette)
            eps_num_silhouette.append([i, j, silhouette])
            if silhouette > max_score:
                max_score = silhouette
                max_eps = i
                max_num = j
        except:
            db = ''

eps_num_silhouette = pd.DataFrame(eps_num_silhouette, columns=['eps', 'min_num', 'silhouette'])

# print(eps_num_silhouette)
print(max_score)  # 0.2412 _'cosine'  # 0.1137 _欧式距离  # 0.1452_'manhattan'
print(max_num)  # 4_'cosine'          # 19 _欧式距离      # 4_'manhattan'
print(max_eps)  # 0.3_'cosine'         # 0.65_欧式距离    #1.9_'manhattan'






