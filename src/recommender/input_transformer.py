import json

'''
This prepossessing step is about to getting the input data and
transform it in a common format (a list).
'''


class Transformer(object):
    def __init__(self, input, target=None):
        self.input = input
        self.target = target
        # TODO: ADD LOGGER

    def transform(self):
        return self.input


class JsonTransformer(Transformer):
    def transform(self):
        return self.input[self.target]


class DataframeTransformer(Transformer):
    def transform(self):
        return list(self.input[self.target])
