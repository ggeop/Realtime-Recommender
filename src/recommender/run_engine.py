import logging
from argparse import ArgumentParser
from recommender.model_manager import ModelManager
from recommender.model_feeder import StaticFeeder

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def main():
    parser = ArgumentParser()

    parser.add_argument('--set_mode', type=str, required=True, help='Set engine mode type')
    parser.add_argument('--input_format', type=str, required=True, help='Set the input format')
    parser.add_argument('--model', type=str, required=True, help='Set the type of model')

    args, unknown, = parser.parse_known_args()

    logging.info('RECOMMENDER STARTS..')
    logging.info('MODEL MODE = {} AND MODEL= {}'.format(args.set_mode, args.model))
    if args.set_mode == 'static':
        feeder = StaticFeeder(args.set_mode, args.input_format, args.model)
        model_input = feeder.create_input()
    model_manager = ModelManager(model_name=args.model, texts=model_input[0], dictionary=model_input[1], corpus=model_input[2])
    model = model_manager.load_model()
    if not model:
        model = model_manager.create_model()
        model_manager.train_model(model, texts=model_input[0], dictionary=model_input[1], corpus=model_input[2])
        logging.info('MODEL IS READY!')


if __name__ == '__main__':
    main()
