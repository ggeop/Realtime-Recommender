import unittest

from recommender.input_transformer import JsonTransformer


class JsonTransformerTests(unittest.TestCase):

    def test_input_json(self):
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


class DataframeTransformer(unittest.TestCase):
    pass


class TupleTransformer(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
