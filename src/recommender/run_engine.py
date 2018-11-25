import logging
from argparse import ArgumentParser
from gensim.test.utils import common_texts
from recommender.model_manager import ModelManager

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def main():
    parser = ArgumentParser()

    parser.add_argument('--set_mode', type=str, required=True, help='Set engine mode type')
    parser.add_argument('--input_format', type=str, required=True, help='Set the input format')
    parser.add_argument('--model', type=str, required=True, help='Set the type of model')

    args, unknown, = parser.parse_known_args()

    logging.info('RECOMMENDER STARTS..')
    if args.set_mode == 'static':
        logging.info('MODEL MODE = {} AND MODEL= {}'.format(args.set_mode, args.model))
        model_manager = ModelManager(model_name='Word2Vec', texts=common_texts)
        model = model_manager.load_model()
        if not model:
            model = model_manager.create_model()
            model_manager.train_model(model, common_texts)
            logging.info('MODEL IS READY!')


if __name__ == '__main__':
    main()
