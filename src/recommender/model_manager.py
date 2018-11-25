import os
import logging
from gensim.test.utils import get_tmpfile
from recommender.settings import GENSIM, MODEL_DUMPS_PATH
from recommender.models.Word2Vec_model import SIZE, WINDOW, MIN_COUNT, TOTAL_EXAMPLES, EPOCHS


class ModelManager(object):
    def __init__(self, model_name, texts=None, corpus=None, dictionary=None, num_topics=None):
        self.model_name = model_name
        self.saved_model = self.model_name + '.model'
        self.texts = texts
        self.dictionary = dictionary
        self.corpus = corpus
        self.num_topics = num_topics
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    def load_model(self):
        model_files = [f for f in os.listdir(MODEL_DUMPS_PATH)]
        if self.saved_model in model_files:
            logging.info('EXIST TRAINED MODEL - {}'.format(self.saved_model))
            model_file = get_tmpfile(os.path.join(MODEL_DUMPS_PATH, self.saved_model))
            return GENSIM[self.model_name].load(model_file)

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

    def train_model(self, model,  texts=None, corpus=None, dictionary=None):
        if self.model_name == 'Word2Vec':
            model.train(texts,
                        total_examples=TOTAL_EXAMPLES,
                        epochs=EPOCHS)
        elif self.model_name == 'LsiModel':
            model.train(corpus=corpus,
                        id2word=dictionary)
        else:
            return None
        temp_file = get_tmpfile(os.path.join(MODEL_DUMPS_PATH, self.saved_model))
        model.save(temp_file)
        return model
