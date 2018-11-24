import unittest
from gensim import models
from gensim.test.utils import common_dictionary, common_corpus
from recommender.model_manager import ModelManager


class LoadModelTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    # def test_no_saved_model(self):
    #     model_manager = ModelManager('Word2Vec')
    #     self.assertEqual(model_manager.load_model(), None)


class CreateModelTests(unittest.TestCase):

    def test_create_BoW_model(self):
        texts = [['word1', 'word2'], ['word3']]
        model_manager = ModelManager('Word2Vec')
        model = models.Word2Vec(texts, size=100, window=5, min_count=1).__class__
        self.assertEqual(model, model_manager.create_model().__class__)

    def test_create_Lsi_model(self):
        model_manager = ModelManager('LsiModel',corpus=common_corpus, dictionary=common_dictionary )
        model = models.LsiModel(corpus=common_corpus, id2word=common_dictionary).__class__
        self.assertEqual(model, model_manager.create_model().__class__)


if __name__ == '__main__':
    unittest.main()