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