from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import tokenize_and_stem, abstracts

# max_df: this is the maximum frequency within the documents a given feature can have to be used in the tfi-idf matrix
# min_idf: this could be an integer and the term would have to be in at least 5 of the documents to be considered
# TODO: 调高max_df, 调低min_df, 根据title看ngram_range的上限应该是几个词语组成词组
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1, 3))
tfidf_matrix = tfidf_vectorizer.fit_transform(abstracts)
# print(tfidf_matrix.shape)

# just a list of the features used in the tf-idf matrix. This is a vocabulary
terms = tfidf_vectorizer.get_feature_names()

from sklearn.metrics.pairwise import cosine_similarity
# dist is defined as 1 - the cosine similarity of each document.
# Cosine similarity is measured against the tf-idf matrix and can be used to generate a measure of similarity
# between each document and the other documents in the corpus (each synopsis among the synopses).
# Subtracting it from 1 provides cosine distance which I will use for plotting on a euclidean (2-dimensional) plane.
dist = 1 - cosine_similarity(tfidf_matrix)

from sklearn.manifold import MDS

MDS()

# convert two components as we're plotting points in a two-dimensional plane
# "precomputed" because we provide a distance matrix
# we will also specify `random_state` so the plot is reproducible.
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)

pos = mds.fit_transform(dist)  # shape (n_components, n_samples)

xs, ys = pos[:, 0], pos[:, 1]