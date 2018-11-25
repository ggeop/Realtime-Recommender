from recommender.models import Word2Vec_model
from recommender.pre_processor import Cleaner, Tokenizer


class Feeder(object):
    def __init__(self, set_mode, input_format, model, documents=None):
        self.set_mode = set_mode
        self.input_format = input_format
        self.model = model
        self.documents = documents


class StaticFeeder(Feeder):
    def create_input(self):
        if self.model == 'Word2Vec':
            cleaner = Cleaner(documents=self.documents,
                              stop_list=Word2Vec_model.STOP_LIST,
                              lower_case=Word2Vec_model.LOWER_CASE,
                              lower_threshold=Word2Vec_model.LOWER_THRESHOLD)
            texts = cleaner.clean()

            tokenizer = Tokenizer(texts)
            if Word2Vec_model.DICTIONARY_FLAG:
                dictionary = tokenizer.create_dictionary()
            else:
                dictionary = None
            if Word2Vec_model.CORPUS_FLAG:
                corpus = tokenizer.create_corpus()
            else:
                corpus = None

            return texts, dictionary, corpus


class StreamingFeeder(Feeder):
    pass
