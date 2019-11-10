# encoding:utf -8
"""
@version:3.7
@author:lc
@file:tfidf
@time: 20:26
"""
import pandas as pd
import sklearn
from joblib.numpy_pickle_utils import xrange
import dataPreprocess
from sklearn.cluster import DBSCAN
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv("D:\\CoursesOfMaster\\informationTheoryAndEncoding\\groupwork1\\AAAI-14AcceptedPapers.csv",
                       header=0, encoding='latin-1')

    papers = data["keywords"] + data["title"] + data["abstract"]
    paper_repre = []
    num_papers = len(papers)

    for i in xrange(0, num_papers):
        paper_repre.append(dataPreprocess.sentence_to_words(papers[i]))
        paper_repre[i] = " ".join(paper_repre[i])
    tfidf = sklearn.feature_extraction.text.TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, use_idf=True,  ngram_range=(1, 3))
    tfidf_vectors = tfidf.fit_transform(paper_repre)  # tfidf的输入必须是一个一个的句子，在这里，计算出了每一篇文章对应的值
    tfidf_vectors = tfidf_vectors.toarray()  # tfidf的返回值是一个稀疏矩阵，要将稀疏矩阵转换为稠密矩阵才能够用tsne降维

    result_cluster = DBSCAN(eps=0.7, min_samples=2).fit(tfidf_vectors)

    tsne = TSNE(n_components=2)  # tsne降维
    dia = tsne.fit_transform(tfidf_vectors)

    fig = plt.figure(figsize=(10, 10))  # 可视化
    plt.scatter(x=dia[:, 0], y=dia[:, 1], marker="x", c=[i for i in result_cluster.labels_])
    plt.show()


