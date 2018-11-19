import json

'''
This preprocessing step is about to getting the input data and
transform it in a common format.
'''

class JsonTransformer(object):
    def __init__(self, array, target):
        self.document = json.loads(array)
        return self.document[target]

class DataframeTransformer(object):
    def __init__(self, dataframe, target):
        return dataframe[target]

class TupleTransformer(object):
    def __init__(self, tuple):
        return list(tuple)
