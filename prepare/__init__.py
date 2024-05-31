import json

def read_jsonl_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return data

def write_jsonl_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')

def remove_duplicate_patterns(data):
    unique_data = []
    relation_patterns = {}

    for item in data:
        relation = item['relation']
        pattern = item['pattern']

        if relation not in relation_patterns:
            relation_patterns[relation] = set()

        if pattern not in relation_patterns[relation]:
            relation_patterns[relation].add(pattern)
            unique_data.append(item)

    return unique_data

# Specify the input and output file paths
input_file = 'input.jsonl'
output_file = 'output.jsonl'

# Read the input jsonl file
data = read_jsonl_file(input_file)

# Remove duplicate patterns within each relation
unique_data = remove_duplicate_patterns(data)

# Write the unique data to the output jsonl file
write_jsonl_file(output_file, unique_data)