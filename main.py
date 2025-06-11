import argparse
import traceback
import json

parser = argparse.ArgumentParser(description="Konwerter plików JSON/XML/YAML")
parser.add_argument('input_file', help='Plik wejściowy')
parser.add_argument('output_file', help='Plik wyjściowy')
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    try:
        data = json.load(f)
    except Exception as e:
        print("Nie udało się wczytać pliku JSON. ", traceback.format_exc())