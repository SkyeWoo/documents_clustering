import pandas as pd
import re
filename = 'AAAI-14 Accepted Papers.csv'
file = open(filename, 'rb')
df = pd.read_csv(file, encoding='latin1', sep=',')
papers = df['title'] + " " + df['keywords'] + " " + df['abstract']
groups = df['groups'].apply(str)
pattern = re.compile(r'[(](.*?)[)]', re.S)
labels = [re.findall(pattern, w) for w in groups]
dic = {}
for k1 in labels:
    for k in k1:
        dic[k] = dic.get(k, 0) + 1
# print(dic)
# print(len(dic)) # 22

import nltk
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
stopwords = nltk.corpus.stopwords.words('english')
# print(stopwords[:10])
stopwords.extend(['use', 'using', 'used', 'proposed', 'propose', 'proposing', 'results', 'resulting', 'result',
                  'method', 'paper', 'models', 'model', 'methods', 'algorithm', 'approach', 'approaches'])

# get the property of words
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


# use lemmatizing/tokenizing functions to iterate over the list of papers
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
for i in papers:
    allwords_lemmatized = tokenize_and_lemmatize(i)
    totalvocab_lemmatized.extend(allwords_lemmatized)

# create a pandas DataFrame with the lemmatized vocabulary as the index and the tokenized words as the column.
# the lemmatization 'run' could be associated with 'ran', 'runs', 'running', etc.
vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index=totalvocab_lemmatized)
# print(vocab_frame.head())
