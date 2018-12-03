import unittest
import pandas as pd
import numpy as np

from recommender.input_transformer import JsonTransformer, DataframeTransformer


class DataframeTransformerTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        data = np.array([[1, 2], [3, 4]])
        self.dataframe = pd.DataFrame(data=data, columns=['Target_col', 'Col2'])

    def test_correct_input(self):
        dataframe_transformer = DataframeTransformer('Target_col')
        self.assertEqual(dataframe_transformer.transform(self.dataframe), [1, 3])

    def test_wrong_column(self):
        pass


class DocumentsTransformerTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.documents = ['word1 word2', 'word3']

    def test_sting_input_no_spaces(self):
        pass

if __name__ == '__main__':
    unittest.main()
