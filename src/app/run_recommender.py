from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(--'input_file_format', type=str, required=True, help = 'Set the input format')
    agrs, unknown, = parser.parse_known_args()
    pass
