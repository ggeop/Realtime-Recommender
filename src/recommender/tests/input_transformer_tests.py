import unittest
import pandas as pd
import numpy as np

from recommender.input_transformer import JsonTransformer, DataframeTransformer, DocumentsTransformer


class JsonTransformerTests(unittest.TestCase):

    def test_correct_input(self):
        json_transformer = JsonTransformer({'target_key': 'test text'}, 'target_key')
        self.assertEqual(json_transformer.transform(), 'test text')

    def test_wrong_key(self):
        with self.assertRaises(KeyError) as raises:
            json_transformer = JsonTransformer({'target_key': 'test text'}, 'wrong_key')
            json_transformer.transform()

    def test_null_value(self):
        with self.assertRaises(KeyError) as raises:
            json_transformer = JsonTransformer({'target_key': 'test text'}, ' ')
            json_transformer.transform()


class DataframeTransformerTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        data = np.array([[1, 2], [3, 4]])
        self.dataframe = pd.DataFrame(data=data, columns=['Target_col', 'Col2'])

    def test_correct_input(self):
        dataframe_transformer = DataframeTransformer(self.dataframe, 'Target_col')
        self.assertEqual(dataframe_transformer.transform(), [1, 3])

    def test_wrong_column(self):
        with self.assertRaises(KeyError) as raises:
            dataframe_transformer = DataframeTransformer(self.dataframe, 'wrong_column')
            dataframe_transformer.transform()


class DocumentsTransformerTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.documents = ['word1 word2', 'word3']

    def test_correct_input_Word2Vec(self):
        model = 'Word2Vec'
        document_transformer = DocumentsTransformer(model, self.documents)
        self.assertEqual(document_transformer.texts, [['word1', 'word2'], ['word3']])

    def test_sting_input_Word2Vec(self):
        model = 'Word2Vec'
        string_documents = 'word1, word2, word3'
        document_transformer = DocumentsTransformer(model, string_documents)
        self.assertEqual(document_transformer.texts, [['word1,', 'word2,', 'word3']])

    def test_sting_input_no_spaces(self):
        model = 'Word2Vec'
        string_documents = 'word1,word2,word3'
        document_transformer = DocumentsTransformer(model, string_documents)
        self.assertEqual(document_transformer.texts, [['word1,word2,word3']])

    def test_dict_output_in_Word2Vec(self):
        model = 'Word2Vec'
        string_documents = 'word1,word2,word3'
        document_transformer = DocumentsTransformer(model, string_documents)
        self.assertEqual(document_transformer.dictionary, None)

    def test_corpus_output_in_Word2Vec(self):
        model = 'Word2Vec'
        string_documents = 'word1,word2,word3'
        document_transformer = DocumentsTransformer(model, string_documents)
        self.assertEqual(document_transformer.corpus, None)


if __name__ == '__main__':
    unittest.main()
