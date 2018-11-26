import unittest
from gensim import models
from gensim.test.utils import common_dictionary, common_corpus
from recommender.model_manager import ModelManager


class LoadModelTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass


class CreateModelTests(unittest.TestCase):

    def test_create_BoW_model(self):
        pass

    def test_create_Lsi_model(self):
        pass


if __name__ == '__main__':
    unittest.main()
