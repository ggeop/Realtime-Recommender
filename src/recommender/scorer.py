from similarity_calculator import SimilarityCalculator
from models.model_1 import *

class Scorer(object):
    def __init__(self,new_input, input, target):
        self.similarity_calculator = SimilarityCalculator(new_input, input, target)
        similarities = self.similarity_calculator.calculte_similarity()

    def calculate_score(self)
        index = similarities.argsort(axis=None)[-NUMBER_OF_RECOMMENDATIONS:]
        return similarities[index]
