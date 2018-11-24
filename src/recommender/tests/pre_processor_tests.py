import unittest

from recommender.pre_processor import Cleaner


class CleanerTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.documents = ['Test documents', 'Stop list words']
        self.stop_list = ['stop', 'list', 'words']

    def test_stop_list_lower(self):
        cleaner = Cleaner(documents=self.documents,
                          stop_list=self.stop_list,
                          lower_case=True)

        self.assertEqual(cleaner.clean(), [['test', 'documents'], []])

    def test_stop_list(self):
        cleaner = Cleaner(documents=self.documents,
                          stop_list=self.stop_list,
                          lower_case=False)

        self.assertEqual(cleaner.clean(), [['Test', 'documents'], ['Stop']])

    def test_sort(self):
        cleaner = Cleaner(documents=self.documents,
                          lower_case=True)

        self.assertEqual(cleaner.clean(), [['test', 'documents'], ['stop', 'list', 'words']])

    def test_no_stop_list_no_sort(self):
        cleaner = Cleaner(documents=self.documents)

        self.assertEqual(cleaner.clean(), [['Test', 'documents'], ['Stop', 'list', 'words']])


class FilterTests(unittest.TestCase):

    def test_filter_below_threshold(self):
        documents = ['word1 word2', 'word1']
        cleaner = Cleaner(documents=documents)
        texts = cleaner.clean()
        self.assertEqual(cleaner.filter(texts),[[], []])

    def test_filter_above_threshold(self):
        documents = ['word1 word1 word2', 'word1']
        cleaner = Cleaner(documents=documents)
        texts = cleaner.clean()
        self.assertEqual(cleaner.filter(texts),[['word1', 'word1'], ['word1']])


if __name__ == '__main__':
    unittest.main()