# encoding:utf -8
"""
@version:3.7
@author:lc
@file:dataPreprocess
@time: 20:20
"""

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
import re


def sentence_to_words(text):
    text_without_punctuations = re.sub("[^a-zA-Z]", " ", text)  # substitute punctuations with whitespace

    token_words = text_without_punctuations.split()

    stops = set(stopwords.words("english"))  # remove stopwords
    text_without_stopwords = [w for w in token_words if w not in stops]

    sentence_stem = []  # stemming using PorterStemmer
    porter = WordNetLemmatizer()  # lemmatization
    for word in text_without_stopwords:
        sentence_stem.append(porter.lemmatize(word, pos='v'))
    return sentence_stem
# 以上模块用于去除text中的stopwords以及进行stemming处理

"""
另外一种将句子处理的方法：直接从nltk中导入相关的包，调用API将paragraph转换为words
from nltk.tokenize import word_tokenize
token_words = word_tokenize(sentence)
直接将sentence转换为一个word的list；
甚至如果sentence是一个text或者documentation，都能够直接转换为word的list
tokenize:不会去标点符号；
"""
def text_to_sentences(text):
    sentence = sent_tokenize(text) # 用于将文本分成一个一个的句子

    sentences = []
    for sen in sentence:
        if len(sen) > 0:
            sentences.append(sentence_to_words(sen))

    return sentences


