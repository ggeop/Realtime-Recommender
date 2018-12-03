

class ResultsCalculator(object):
    def __init__(self, dataset, result_column, vectorizer, similarity_measure, number_of_recommendations):
        self.dataset = dataset
        self.result_column = result_column
        self.similarity_measure = similarity_measure
        self.vectorizer = vectorizer
        self.number_of_recommendations = number_of_recommendations

    def query(self, train_tdm, new_text):
        test_tdm = self.vectorizer.transform(new_text)
        result, score = self.calculate_similarity(train_tdm, test_tdm)
        return result, score

    def calculate_similarity(self, train_tdm, test_tdm):
        similarities = self.similarity_measure(train_tdm, test_tdm)

        '''Extract the most close organization from the sorted list'''
        index = similarities.argsort(axis=None)[-self.number_of_recommendations:]

        '''Extract the similarity score'''
        score = similarities[index]

        '''Return the organization name'''
        return self.dataset[self.result_column][index][::-1], score[::-1]
