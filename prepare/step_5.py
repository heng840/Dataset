import json
import os

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def align_json_files(file_paths):
    # Read the JSON files
    json_data = [read_json_file(file_path) for file_path in file_paths]

    # Get the common UUIDs
    common_uuids = set(json_data[0].keys())
    for data in json_data[1:]:
        common_uuids &= set(data.keys())

    # Filter the JSON data based on common UUIDs
    aligned_data = [{} for _ in range(len(file_paths))]
    for uuid in common_uuids:
        for i, data in enumerate(json_data):
            aligned_data[i][uuid] = data[uuid]

    return aligned_data

# Specify the input and output folder paths
input_folder = '/home/chenyuheng/chenyuheng/LIKN/my_MLAMA_not_aligned'
output_folder = '/home/chenyuheng/chenyuheng/LIKN/Aligned_my_MLAMA'

# Get the file paths of the JSON files in the input folder
file_paths = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith('.json')]

# Align the JSON files
aligned_data = align_json_files(file_paths)

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Write the aligned data to the output folder
for i, file_path in enumerate(file_paths):
    filename = os.path.basename(file_path)
    output_file_path = os.path.join(output_folder, filename)
    write_json_file(output_file_path, aligned_data[i])