import json
import os
import re
from collections import defaultdict


def process_jsonl_files(folder_path):
    filtered_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".jsonl"):
            relation = os.path.splitext(filename)[0]
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    data = json.loads(line)
                    pattern = data.get("pattern")
                    if pattern:
                        if re.search(r"\[Y\](?=[\.,\s]*$)", pattern):
                            filtered_data.append({
                                "relation": relation,
                                "pattern": pattern
                            })
    grouped_data = defaultdict(list)
    for data in filtered_data:
        grouped_data[data["relation"]].append(data)

    final_data = []
    for relation, data_list in grouped_data.items():
        if len(data_list) > 1:
            final_data.extend(data_list)

    return final_data

folder_path = "/home/chenyuheng/chenyuheng/LIKN/graphs_json"
output_file_step_1 = "/home/chenyuheng/chenyuheng/LIKN/my_mlama/en_fr/en/final_template.jsonl"
def step_1():
    filtered_data = process_jsonl_files(folder_path)

    with open(output_file_step_1, 'w') as file:
        for data in filtered_data:
            json.dump(data, file)
            file.write('\n')


def read_relations_from_file(file_path):
    relations = set()
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            relations.add(data["relation"])
    return relations

def process_new_jsonl_file(file_path, relations):
    filtered_data = []
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            if data["relation"] in relations:
                filtered_data.append({
                    "relation": data["relation"],
                    "pattern": data["template"]
                })
    return filtered_data

relations_to_keep = read_relations_from_file(output_file_step_1)

new_jsonl_file = "/home/chenyuheng/chenyuheng/LIKN/my_mlama/ja_ko/ko/templates.jsonl"
filtered_data = process_new_jsonl_file(new_jsonl_file, relations_to_keep)

# 将过滤后的数据保存到新的jsonl文件
output_file_step_2 = "/home/chenyuheng/chenyuheng/LIKN/my_mlama/ja_ko/ko/tmp.jsonl"
with open(output_file_step_2, 'w') as file:
    for data in filtered_data:
        json.dump(data, file)
        file.write('\n')
