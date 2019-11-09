import pandas as pd
filename = 'AAAI-14 Accepted Papers.csv'
file = open(filename, 'rb')
df = pd.read_csv(file, encoding='latin1', sep=',')

titles = df['title'].values.tolist()
authors = df['authors'].values.tolist()
groups = df['groups'].values.tolist()
keywords = df['keywords'].values.tolist()
topics = df['topics'].values.tolist()
abstracts = df['abstract'].values.tolist()

import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# load nltk's English stopwords as variable called 'stopwords'
stopwords = nltk.corpus.stopwords.words('english')

# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

import re

# here I define a tokenizer and stemmer which returns the set of stems in the text that it is passed

# tokenizes (splits the synopsis into a list of its respective words (or tokens) and also stems each token
def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

# tokenizes the synopsis only
def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

# use stemming/tokenizing and tokenizing functions to iterate over the list of synopses
# to create two vocabularies: one stemmed and one only tokenized.
# use extend so it's a big flat list of vocab
totalvocab_stemmed = []
totalvocab_tokenized = []
for i in abstracts:
    allwords_stemmed = tokenize_and_stem(i)  # for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed)  # extend the 'totalvocab_stemmed' list

    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)

# create a pandas DataFrame with the stemmed vocabulary as the index and the tokenized words as the column.
# The benefit of this is it provides an efficient way to look up a stem and return a full token.
# The downside here is that stems to tokens are one to many:
# the stem 'run' could be associated with 'ran', 'runs', 'running', etc.
vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)