import logging
from argparse import ArgumentParser
from recommender.model_manager import ModelManager
from recommender.model_feeder import StaticFeeder

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def main():
    parser = ArgumentParser()

    parser.add_argument('--set_mode', type=str, required=False, help='Set engine mode type')
    parser.add_argument('--input_format', type=str, required=False, help='Set the input')
    parser.add_argument('--model', type=str, required=False, help='Set the type of model')

    args, unknown, = parser.parse_known_args()

    logging.info('RECOMMENDER STARTS..')
    logging.info('MODEL MODE = {} AND MODEL= {}'.format(args.set_mode, args.model))
    model_manager = ModelManager()
    logging.info('APPLICATION STARTS..')
    if args.set_mode == 'static':
        feeder = StaticFeeder(model_manager=model_manager)
        feeder.run()


if __name__ == '__main__':
    main()
