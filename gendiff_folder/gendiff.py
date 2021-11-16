import json


def generate_diff(file1, file2):
    file3 = {}
    for key, value in file1.items():
        if key in file2.keys():
            if value in file2.values():
                file3[f'  {key}'] = value
            if value not in file2.values():
                file3[f'- {key}'] = value
        if value not in file2.values():
            file3[f'- {key}'] = value
    for key, value in file2.items():
        if value not in file1.values():
            file3[f'+ {key}'] = value
    diff = ['{'] + sorted({'{}: {}'.format(key,value) for key,value in file3.items()}, key=lambda x: x[2] + x[0], reverse=True) + ['}']
    return '\n'.join(diff)


def read_json(file):
    return json.load(open(file))
