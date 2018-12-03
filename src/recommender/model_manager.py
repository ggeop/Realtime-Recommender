import os
import logging
import pickle
from gensim.test.utils import get_tmpfile
from sklearn.feature_extraction.text import TfidfVectorizer
from recommender.settings import MODEL_DUMPS_PATH
from recommender.models.tfidf_model_1 import args, model_name

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class ModelManager(object):
    def __init__(self):
        self.vectorizer = TfidfVectorizer(**args)
        self.model_name = model_name
        self.saved_model = self.model_name + '.model'
        logging.info('THE MODEL {} INITIALIZED SUCCESSFULLY!'.format(self.model_name))

    def create_model(self, input_text):
        logging.info('CREATE MODEL - {}..'.format(self.saved_model))
        model = self.load_model()
        if not model:
            vec = self.vectorizer.fit_transform(input_text)
            logging.info('MODEL CREATED - {}..'.format(self.model_name))
            self.save_model(vec)
            return vec

    def load_model(self):
        logging.info('SEARCH TO LOAD A TRAINED MODEL - {}'.format(self.model_name))
        model_files = [f for f in os.listdir(MODEL_DUMPS_PATH)]
        if self.saved_model in model_files:
            logging.info('TRAINED MODEL EXISTS - {}'.format(self.model_name))
            model_file = get_tmpfile(os.path.join(MODEL_DUMPS_PATH, self.model_name))
            return pickle.loads(model_file)

        logging.info('NO TRAINED MODEL EXISTS - {}'.format(self.model_name))
        return None

    def save_model(self, model):
        temp_file = get_tmpfile(os.path.join(MODEL_DUMPS_PATH, self.model_name))
        pickle.dumps(temp_file)
        logging.info('MODEL SAVED!')
