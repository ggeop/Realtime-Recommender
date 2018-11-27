from recommender.models import Word2Vec_model
from recommender.pre_processor import Cleaner, Tokenizer


class Transformer(object):
    def __init__(self, input_data=None, target=None):
        """
        This prepossessing step is about to getting the input data and
        transform it in a common format (a list).
        """
        self.input_data = input_data
        self.target = target

    def transform(self):
        return self.input_data


class JsonTransformer(Transformer):
    def transform(self):
        return self.input_data[self.target]


class DataframeTransformer(Transformer):
    def transform(self):
        return list(self.input_data[self.target])


class DocumentsTransformer(object):
    def __init__(self, model, documents):
        models = {'Word2Vec_model': Word2Vec_model}
        saved_model = model + '_model'
        self.cleaner = Cleaner(documents=documents,
                               stop_list=models[saved_model].STOP_LIST,
                               lower_case=models[saved_model].LOWER_CASE,
                               lower_threshold=models[saved_model].LOWER_THRESHOLD)
        if models[saved_model].TEXT_FLAG:
            self.texts = self.cleaner.clean()
        tokenizer = Tokenizer(self.texts)
        if models[saved_model].DICTIONARY_FLAG:
            self.dictionary = tokenizer.create_dictionary()
        else:
            self.dictionary = None
        if models[saved_model].CORPUS_FLAG:
            self.corpus = tokenizer.create_corpus()
        else:
            self.corpus = None
