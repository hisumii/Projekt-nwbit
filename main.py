import argparse
import traceback
import json
import yaml

parser = argparse.ArgumentParser(description="Konwerter plików JSON/XML/YAML")
parser.add_argument('input_file', help='Plik wejściowy')
parser.add_argument('output_file', help='Plik wyjściowy')
args = parser.parse_args()

if args.input_file.endswith('.json'):
    with open(args.input_file, 'r') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print("Nie udało się wczytać pliku JSON. ", traceback.format_exc())

    with open(args.output_file, 'w') as f:
        try:
            json.dump(data, f, indent=2)
        except Exception as e:
            print("Nie udało się zapisać pliku JSON. ", traceback.format_exc())
elif args.input_file.endswith('.yml') or args.input_file.endswith('.yaml'):
    with open(args.input_file, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except Exception as e:
            print("Nie udało się wczytać pliku YAML. ", traceback.format_exc())

    with open(args.output_file, 'w') as f:
        try:
            yaml.dump(data, f)
        except Exception as e:
            print("Nie udało się zapisać pliku YAML. ", traceback.format_exc())
elif args.input_file.endswith('.xml'):
    # wczytaj XML
else:
    print("Nieznany format pliku!")


