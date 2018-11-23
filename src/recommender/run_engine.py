from argparse import ArgumentParser

from input_transformer import JsonTransformer, DataframeTransformer, TupleTransformer
from pre_processor import Vectorizer
from models import *

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(--'set_mode', type=str, required=True, help = 'Set engine mode type')
    parser.add_argument(--'input_file_format', type=str, required=True, help = 'Set the input format')
    parser.add_argument(--'set_model', type=str, required=True, help = 'Set the type of model')

    agrs, unknown, = parser.parse_known_args()
