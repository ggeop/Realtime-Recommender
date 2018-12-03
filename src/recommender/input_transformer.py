"""
This prepossessing step is about to getting the input data and
transform it in a common format (a list).
"""


class Transformer(object):
    def __init__(self,  target=None):
        self.target = target

    def transform(self, input_data):
        pass


class JsonTransformer(Transformer):
    def transform(self, input_data):
        return input_data[self.target]


class DataframeTransformer(Transformer):
    def transform(self, input_data):
        return list(input_data[self.target])


class DocumentsTransformer(object):
    def __init__(self):
        pass
