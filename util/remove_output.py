import os
import sys
import json

if __name__ == '__main__':
    fpath = sys.argv[1]
    dname, fname = os.path.split(os.path.abspath(fpath))

    # backup_dir = os.path.join(dname, 'backup')
    #
    # if not os.path.exists(backup_dir):
    #     os.makedirs(backup_dir)
    #
    # backup_file = os.path.join(backup_dir, fname)

    with open(fpath, 'r') as f:
        json_file = json.load(f)

    # with open(backup_file, 'w') as f:
    #     json.dump(json_file, f)

    # Remove empty cells
    cells = [cell for cell in json_file['cells']
            if cell['source'] != []]

    for cell in cells:
        # Remove the execution counts
        cell['execution_count'] = None

        # Clear the outputs
        cell['outputs'] = []

    json_file['cells'] = cells

    # Warning: Replaces the original file. Not safe
    with open(fpath, 'w') as f:
        json.dump(json_file, f)
