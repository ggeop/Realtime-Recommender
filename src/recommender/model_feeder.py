import logging
from recommender.input_transformer import InputTransformer

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class StaticFeeder(object):
    def __init__(self, set_mode, input_format, model_name, model, model_manager):
        self.set_mode = set_mode
        self.input_format = input_format
        self.model_name = model_name
        self.model = model
        self.model_manager = model_manager

    def run(self):
        logging.info('WAITING FOR USER INPUT..')
        user_input = input('INSERT TO THE MODEL: ')
        input_transformer = InputTransformer(self.model_name, user_input)

        self.model_manager.train_model(self.model, texts=input_transformer.texts)
