# encoding:utf -8
"""
@version:3.7
@author:lc
@file:tfidf
@time: 20:26
"""
from tfidf import tfidf_matrix
from sklearn.cluster import DBSCAN
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

tfidf_vectors = tfidf_matrix.toarray()  # tfidf的返回值是一个稀疏矩阵，要将稀疏矩阵转换为稠密矩阵才能够用tsne降维

result_cluster = DBSCAN(eps=0.7, min_samples=2).fit(tfidf_vectors)

tsne = TSNE(n_components=2)  # tsne降维
dia = tsne.fit_transform(tfidf_vectors)

fig = plt.figure(figsize=(10, 10))  # 可视化
plt.scatter(x=dia[:, 0], y=dia[:, 1], marker="x", c=[i for i in result_cluster.labels_])
plt.show()