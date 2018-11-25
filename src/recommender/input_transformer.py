import json


class Transformer(object):
    def __init__(self, input_data, target=None):
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
