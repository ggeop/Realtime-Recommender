import logging
from gensim import corpora
from collections import defaultdict
from recommender.settings import THRESHOLD

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class Cleaner(object):
    def __init__(self, documents, stop_list=None, lower_case=False, lower_threshold=False):
        """
        Clean function:
        -Split the documents to list with words
        -Transform capital to lower
        -Remove stopwords
        -Remove words with frequency lower than the threshold
        """
        self.documents = documents
        self.stop_list = stop_list
        self.lower_case = lower_case
        self.lower_threshold = lower_threshold
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    def clean(self):
        if self.stop_list and self.lower_case:
            texts = [[word for word in document.lower().split() if word not in self.stop_list]
                     for document in self.documents]
        elif self.stop_list and not self.lower_case:
            texts = [[word for word in document.split() if word not in self.stop_list]
                     for document in self.documents]
        elif not self.stop_list and self.lower_case:
            texts = [[word for word in document.lower().split()] for document in self.documents]
        else:
            texts = [[word for word in document.split()] for document in self.documents]

        return texts

    @staticmethod
    def filter(texts):
        """texts format [['..', '..'],['..'],[],...]"""
        frequency = defaultdict(int)
        for text in texts:
            for token in text:
                frequency[token] += 1

        texts = [[token for token in text if frequency[token] > THRESHOLD]
                 for text in texts]

        return texts


class Tokenizer(object):
    def __init__(self, texts):
        self.texts = texts

    def create_dictionary(self):
        return corpora.Dictionary(self.texts)

    def create_corpus(self):
        dictionary = self.create_dictionary()
        return [dictionary.doc2bow(text) for text in self.texts]