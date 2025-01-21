import json
import csv
import sys


def convert_jsonl_to_csv(input_file, output_file):
    # Read JSONL and get all possible fields
    with open(input_file, "r") as f:
        data = [json.loads(line) for line in f]

    if not data:
        print("No data found in input file")
        return

    # Get all unique keys from all records
    fieldnames = set()
    for record in data:
        fieldnames.update(record.keys())
    fieldnames = sorted(list(fieldnames))

    # Write to CSV
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python jsonl_to_csv.py input.jsonl output.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        convert_jsonl_to_csv(input_file, output_file)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
