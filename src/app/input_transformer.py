import json

'''
This preprocessing step is about to getting the input data and
transform it in a common format.
'''
class Transformer(object):
    def __init__(self, input, target = None):
        self.input = input
        self.target = target
        # TODO: ADD LOGGER

class JsonTransformer(Transformer):
    def transform(self):
        return self.input[self.target]

class DataframeTransformer(Transformer):
    def transform(self):
        return self.input[self.target]

class TupleTransformer(Transformer):
    def transform(self):
        return list(self.input)
