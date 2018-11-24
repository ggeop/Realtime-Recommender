import logging
from gensim import models


class ModelManager(object):
    def __init__(self, model, corpus =None, dictionary=None, num_topics = None):
        self.model = model
        self.dictionary = dictionary
        self.corpus = corpus
        self.num_topics = num_topics
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


    def train_model(self):
        model_name = self.model

        if model_name == 'Lsi':
            models.model_name(corpus=self.corpus,
                              id2word=self.dictionary,
                              num_topic = self.num_topics)

