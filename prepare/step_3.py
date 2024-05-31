import json
import os

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

def filter_duplicates_and_single_patterns(data):
    filtered_data = []
    relation_patterns = {}

    for item in data:
        relation = item['relation']
        pattern = item['pattern']

        if relation not in relation_patterns:
            relation_patterns[relation] = []

        relation_patterns[relation].append(pattern)

    for relation, patterns in relation_patterns.items():
        if len(patterns) > 1:
            # Remove duplicate patterns within each relation
            unique_patterns = list(set(patterns))

            if len(unique_patterns) > 1:
                for pattern in unique_patterns:
                    filtered_data.append({'relation': relation, 'pattern': pattern})

    return filtered_data

def align_relations(filtered_data):
    all_relations = None

    for data in filtered_data.values():
        relations = set(item['relation'] for item in data)

        if all_relations is None:
            all_relations = relations
        else:
            all_relations = all_relations.intersection(relations)

    aligned_data = {}

    for file_path, data in filtered_data.items():
        aligned_data[file_path] = [item for item in data if item['relation'] in all_relations]

    return aligned_data

# Specify the file paths of the jsonl files
file_paths = ['/home/chenyuheng/chenyuheng/LIKN/my_mlama/en_fr/en/final_template.jsonl',
              '/home/chenyuheng/chenyuheng/LIKN/my_mlama/en_fr/fr/final_template.jsonl',
              '/home/chenyuheng/chenyuheng/LIKN/my_mlama/fi_hu/fi/final_template.jsonl',
              '/home/chenyuheng/chenyuheng/LIKN/my_mlama/fi_hu/hu/final_template.jsonl',
              '/home/chenyuheng/chenyuheng/LIKN/my_mlama/ja_ko/ja/final_template.jsonl',
              '/home/chenyuheng/chenyuheng/LIKN/my_mlama/ja_ko/ko/final_template.jsonl',
              ]

# Remove duplicate patterns within each file
unique_data = {}
for file_path in file_paths:
    data = read_jsonl_file(file_path)
    unique_data[file_path] = remove_duplicate_patterns(data)

# Filter out relations with single patterns for each file
filtered_data = {}
for file_path, data in unique_data.items():
    filtered_data[file_path] = filter_duplicates_and_single_patterns(data)

# Align the relations across all files using filtered_data
aligned_data = align_relations(filtered_data)

# Write the aligned data back to the jsonl files
for file_path, data in aligned_data.items():
    output_file_path = os.path.splitext(file_path)[0] + '_aligned.jsonl'
    write_jsonl_file(output_file_path, data)