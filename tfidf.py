from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import tokenize_and_lemmatize, papers

# max_df: maximum frequency within the documents a given feature can have to be used in the tfi-idf matrix
# min_idf: an integer and the term would have to be in at least 5 of the documents to be considered
# TODO: 调高max_df, 调低min_df, 根据title看ngram_range的上限应该是几个词语组成词组
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_lemmatize, ngram_range=(1, 6))
# Fraudulent Support Telephone Number Identification Based on Co-occurrence Information on the Web
# The Complexity of Reasoning with FODD and GFODD(Generalized First Order Decision Diagrams)
# ReLISH: Reliable Label Inference via Smoothness Hypothesis

tfidf_matrix = tfidf_vectorizer.fit_transform(papers)
# just a list of the features used in the tf-idf matrix. This is a vocabulary
terms = tfidf_vectorizer.get_feature_names()
# print(tfidf_matrix.shape)
