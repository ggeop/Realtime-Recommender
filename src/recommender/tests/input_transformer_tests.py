import unittest
import pandas as pd
import numpy as np

from recommender.input_transformer import JsonTransformer, DataframeTransformer


class JsonTransformerTests(unittest.TestCase):

    def test_correct_input(self):
        json_transformer = JsonTransformer({'target_key':'test text'}, 'target_key' )
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
        data = np.array([[1, 2],[3, 4]])
        self.dataframe = pd.DataFrame(data=data, columns=['Target_col', 'Col2'])

    def test_correct_input(self):
        dataframe_transformer = DataframeTransformer(self.dataframe, 'Target_col')
        self.assertEqual(dataframe_transformer.transform(), [1, 3])

    def test_wrong_column(self):
        with self.assertRaises(KeyError) as raises:
            dataframe_transformer = DataframeTransformer(self.dataframe, 'wrong_column')
            dataframe_transformer.transform()


if __name__ == '__main__':
    unittest.main()
