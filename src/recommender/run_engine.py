import logging
from argparse import ArgumentParser
from recommender.model_manager import  ModelManager

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--set_mode', type=str, required=True, help='Set engine mode type')
    parser.add_argument('--input_format', type=str, required=True, help='Set the input format')
    parser.add_argument('--model', type=str, required=True, help='Set the type of model')

    args, unknown, = parser.parse_known_args()

    if args.set_mode == 'static':

        model_manager = ModelManager(args.model)
        initialized_model = model_manager.load_model()
        if not initialized_model:
            initialized_model = model_manager.create_model()

        initialized_model.train(['new_text'])
