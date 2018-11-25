from gensim import similarities


class ResultsCalculator(object):
    def __init__(self, model, dictionary=None, corpus=None):
        self.model = model
        self.dictionary = dictionary
        self.corpus = corpus

    def query(self, new_text):
        """Convert the query to LSI space"""
        vec_bow = self.dictionary.doc2bow(new_text)
        return self.model[vec_bow]

    def calculate_similarity(self, new_text):
        """Transform corpus to LSI space and index it"""
        vec_model = self.query(new_text)
        index = similarities.MatrixSimilarity(self.model[self.corpus])
        sims = index[vec_model]

        return sorted(enumerate(sims), key=lambda item: -item[1])
