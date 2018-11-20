import unittest

from .tests import RealtimeRecommenderTestCase
from app import input_transformer


class JsonTransformerTests(RealtimeRecommenderTestCase):

     def test_input_json(self):
         self.json_transformer = JsonTransformer({'target':'test text'}, 'target' )
         self.assertEqual(json_transformer.transform(), ['test text'])

    def test_wrong_key(self):
        pass

    def  test_null_value(self):
        pass


class DataframeTransformer(RealtimeRecommenderTestCase):
    pass


class TupleTransformer(RealtimeRecommenderTestCase):
    pass


if __name__ == '__main__':
    unittest.main()
