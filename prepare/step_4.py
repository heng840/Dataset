import json
import os


def read_jsonl_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return data


def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def fill_template(template_data, content_data):
    output_data = {}

    for item in content_data:
        sub_label = item['sub_label']
        obj_label = item['obj_label']
        relation_name = item['relation']
        uuid = item['uuid']

        sentences = []
        for template in template_data:
            if template['relation'] == relation_name:
                pattern = template['pattern']
                sentence = pattern.replace('[X]', sub_label).replace('[Y]', '')
                sentences.append(sentence.strip())

        output_data[uuid] = {
            'sentences': sentences,
            'relation_name': relation_name,
            'obj_label': obj_label
        }

    return output_data


# Specify the file paths
template_file = '/home/chenyuheng/chenyuheng/LIKN/my_mlama/ja_ko/ko/final_template_aligned.jsonl'
content_folder = '/home/chenyuheng/chenyuheng/LIKN/my_mlama/ja_ko/ko'
output_file = '/home/chenyuheng/chenyuheng/LIKN/Final_my_MLAMA/ko.json'

# Read the template file
template_data = read_jsonl_file(template_file)

# Process each content file
output_data = {}
for filename in os.listdir(content_folder):
    if filename.startswith('P') and filename.endswith('.jsonl'):
        relation_name = os.path.splitext(filename)[0]
        content_file = os.path.join(content_folder, filename)

        # Read the content file
        content_data = read_jsonl_file(content_file)

        # Add the relation name to each content item
        for item in content_data:
            item['relation'] = relation_name

        # Fill the content into the template
        relation_output = fill_template(template_data, content_data)

        # Merge the output data
        output_data.update(relation_output)

# Write the output to a JSON file
write_json_file(output_file, output_data)