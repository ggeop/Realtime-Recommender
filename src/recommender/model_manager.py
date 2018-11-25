import os
import logging
from recommender.settings import GENSIM, MODEL_DUMPS_PATH
from recommender.models.Word2Vec_model import SIZE, WINDOW, MIN_COUNT


class ModelManager(object):
    def __init__(self, model_name, texts=None, corpus=None, dictionary=None, num_topics=None):
        self.model_name = model_name
        self.texts = texts
        self.dictionary = dictionary
        self.corpus = corpus
        self.num_topics = num_topics
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    def load_model(self):
        model_files = [f for f in os.listdir(MODEL_DUMPS_PATH)]

        saved_model = self.model_name + '.model'

        if saved_model in model_files:
            logging.info('Exist trained model')
            return GENSIM[self.model_name].load(saved_model)

        logging.info('No trained model')
        return None

    def create_model(self):
        if self.model_name == 'LsiModel':
            logging.info('Create LsiModel')
            return GENSIM['LsiModel'](corpus=self.corpus,
                                      id2word=self.dictionary)
        if self.model_name == 'Word2Vec':
            logging.info('Create Word2Vec')
            return GENSIM['Word2Vec'](self.texts,
                                      size=SIZE,
                                      window=WINDOW,
                                      min_count=MIN_COUNT)

    def train_model(self, model,  text=None, corpus=None, dictionary=None):
        if self.model_name == 'Word2Vec':
            trained_model = model.train(text, total_examples=1, epochs=1)
        elif self.model_name == 'LsiModel':
            trained_model = model.train(corpus=corpus, id2word=dictionary)
        else:
            return None
        trained_model.save(MODEL_DUMPS_PATH)
        return trained_model
