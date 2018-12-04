import logging
from sklearn.metrics.pairwise import cosine_similarity
from recommender.input_transformer import DataframeTransformer
from recommender.utils import SqlConnector, DATABASE
from recommender.resuts_calculator import ResultsCalculator
from recommender.pre_processor import Cleaner
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class StaticFeeder(object):
    def __init__(self, model_manager, set_mode=None, input_format=None):
        self.set_mode = set_mode
        self.input_format = input_format
        self.model_manager = model_manager

    def run(self):
        sql_connection = SqlConnector()
        input_df = sql_connection.selecting_query()
        dataframe_transformer = DataframeTransformer(DATABASE['target_column'])
        input_text = dataframe_transformer.transform(input_df)
        train_tdm = self.model_manager.create_model(input_text)
        logging.info('WAITING FOR USER INPUT..')
        documents = input('INSERT TO THE MODEL: ')
        results_calculator = ResultsCalculator(dataset=input_df,
                                               result_column=DATABASE['target_column'],
                                               vectorizer=self.model_manager.vectorizer,
                                               similarity_measure=cosine_similarity,
                                               number_of_recommendations=3)

        result, score = results_calculator.query(train_tdm, [documents])
        print(result)

