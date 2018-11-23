

class ModelManager(object):
    def __init__(self, model):
        self.model = model

    def load_model(self):
        path = get_tmpfile("word2vec.model")
        self.model.load('saved')

    def train_model(self):
        self.trained_model = self.model(train_text, size=100, window=5, min_count=1, workers=4)

    def save_model(self):
        self.trained_model.save("word2vec.model")
