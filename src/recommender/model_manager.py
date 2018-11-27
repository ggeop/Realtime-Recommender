import os
import logging
from gensim.test.utils import get_tmpfile
from recommender.settings import GENSIM, MODEL_DUMPS_PATH
from recommender.models.Word2Vec_model import SIZE, WINDOW, MIN_COUNT, TOTAL_EXAMPLES, EPOCHS
from recommender.utils import SqlConnector
from recommender.input_transformer import DataframeTransformer, DocumentsTransformer
from recommender.settings import DATABASE

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class ModelManager(object):
    def __init__(self, model_name):
        self.model_name = model_name
        self.saved_model = self.model_name + '.model'
        logging.info('THE MODEL {} INITIALIZED SUCCESSFULLY!'.format(self.saved_model))

    def load_model(self):
        logging.info('SEARCH TO LOAD A TRAINED MODEL - {}'.format(self.saved_model))
        model_files = [f for f in os.listdir(MODEL_DUMPS_PATH)]
        if self.saved_model in model_files:
            logging.info('TRAINED MODEL EXISTS - {}'.format(self.saved_model))
            model_file = get_tmpfile(os.path.join(MODEL_DUMPS_PATH, self.saved_model))
            return GENSIM[self.model_name].load(model_file)

        logging.info('NO TRAINED MODEL EXISTS - {}'.format(self.saved_model))
        return None

    def create_model(self, texts=None, dictionary=None, corpus=None):
        logging.info('TRAIN NEW MODEL - {}'.format(self.saved_model))
        if self.model_name == 'LsiModel':
            logging.info('CREATE LsiModel')
            return GENSIM['LsiModel'](corpus=corpus,
                                      id2word=dictionary)
        if self.model_name == 'Word2Vec':
            sql_connection = SqlConnector()
            documents = sql_connection.selecting_query()
            documents = DataframeTransformer(documents, DATABASE['target_column']).transform()
            texts = DocumentsTransformer(self.model_name, documents).texts
            logging.info('CREATE Word2Vec MODEL!')
            return GENSIM['Word2Vec'](texts,
                                      size=SIZE,
                                      window=WINDOW,
                                      min_count=MIN_COUNT)
        else:
            raise ImportError('THE MODEL {} DOESNT EXISTS'.format(self.model_name))

    def train_model(self, model,  texts=None, corpus=None, dictionary=None):
        logging.info('TRAIN THE MODEL')
        if self.model_name == 'Word2Vec':
            model.train(texts,
                        total_examples=TOTAL_EXAMPLES,
                        epochs=EPOCHS)
        elif self.model_name == 'LsiModel':
            model.train(corpus=corpus,
                        id2word=dictionary)
        else:
            return None
        self.save_model(model)
        logging.info('MODEL TRAINED!')
        return model

    def save_model(self, model):
        temp_file = get_tmpfile(os.path.join(MODEL_DUMPS_PATH, self.saved_model))
        model.save(temp_file)
        logging.info('MODEL SAVED!')
