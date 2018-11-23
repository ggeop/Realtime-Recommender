from gensim.corpora import Dictionary


class ModelManager(object):
    def __init__(self, model):
        self.dictionary = None

    def create_dictionary(self, text_list):
        self.dictionary = Dictionary([text_list])

    def update_dictionary(self,new_documents):
        self.dictionary.add_documents([new_documents])