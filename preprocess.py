import pandas as pd
filename = 'AAAI-14 Accepted Papers.csv'
file = open(filename, 'rb')
df = pd.read_csv(file, encoding='latin1', sep=',')
papers = df['title'] + " " + df['keywords'] + " " + df['abstract']
titles = df['title'].values.tolist()
keywords = df['keywords'].values.tolist()
abstracts = df['abstract'].values.tolist()

import nltk
import re
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
# load nltk's English stopwords as variable called 'stopwords'
stopwords = nltk.corpus.stopwords.words('english')

# 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


totalvocab_tokenized = []
def tokenize_and_lemmatize(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token) and (token not in stopwords):
            filtered_tokens.append(token)
    tagged_sent = pos_tag(filtered_tokens)
    wnl = WordNetLemmatizer()
    lemmas_sent = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # 词形还原
    totalvocab_tokenized.extend(filtered_tokens)
    return lemmas_sent


totalvocab_lemmatized = []
# use stemming/tokenizing and tokenizing functions to iterate over the list of synopses
# to create two vocabularies: one stemmed and one only tokenized.
# use extend so it's a big flat list of vocab
for i in papers:
    allwords_lemmatized = tokenize_and_lemmatize(i)
    totalvocab_lemmatized.extend(allwords_lemmatized)

# create a pandas DataFrame with the stemmed vocabulary as the index and the tokenized words as the column.
# The benefit of this is it provides an efficient way to look up a stem and return a full token.
# The downside here is that stems to tokens are one to many:
# the stem 'run' could be associated with 'ran', 'runs', 'running', etc.
vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index=totalvocab_lemmatized)
# print(vocab_frame.head())
