from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(--'input_file_format', type=str, required=True, help = 'Set the input format')
    parser.add_argument(--'set_model', type=str, required=True, help = 'Set the type of model')

    agrs, unknown, = parser.parse_known_args()
    pass
