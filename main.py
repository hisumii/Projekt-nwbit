import argparse

parser = argparse.ArgumentParser(description="Konwerter plików JSON/XML/YAML")
parser.add_argument('input_file', help='Plik wejściowy')
parser.add_argument('output_file', help='Plik wyjściowy')
args = parser.parse_args()
