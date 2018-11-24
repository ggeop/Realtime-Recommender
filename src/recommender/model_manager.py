import logging
from gensim import similarities
from recommender.settings import *


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
        else:
            logging.info('No trained model')
            return None

    def create_model(self):

        if self.model_name == 'LsiModel':
            return GENSIM['LsiModel'](corpus=self.corpus,
                                      id2word=self.dictionary)
        if self.model_name == 'Word2Vec':
            return GENSIM['Word2Vec'](self.texts,
                                      size=100,
                                      window=5,
                                      min_count=1)
            # TODO: ADD size, window, min_count to model configuration

    '''Convert the query to LSI space'''
    def query(self, new_text):
        vec_bow = self.dictionary.doc2bow(new_text)
        return self.model[vec_bow]

    '''Transform corpus to LSI space and index it'''
    def calculate_similarity(self, new_text):
        vec_model = self.query(new_text)
        index = similarities.MatrixSimilarity(self.model[self.corpus])
        sims = index[vec_model]

        '''Return the sorted similarities'''
        return sorted(enumerate(sims), key=lambda item: -item[1])