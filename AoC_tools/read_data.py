import re


def read_data(file, numbers=True, by_block=False, split=None):
    with open(file, 'r') as fic:
        if by_block:
            if split is not None:
                raise Exception("The split is not implemented yet for the reading by blocks.")
            if numbers:
                data = [[int(x) for x in block.split('\n') if x.isdigit()] for block in fic.read().split('\n\n')]
            else:
                data = [[x for x in block.split('\n') if x != ''] for block in fic.read().split('\n\n')]
        else:
            if split is None:
                if numbers:
                    data = [int(x) for x in fic.read().split('\n')[:-1] if x != '']
                else:
                    data = [x for x in fic.read().split('\n')[:-1]]
            else:
                if numbers:
                    data = [
                        [int(x) if x.isdigit() else x for x in line.split(split)]
                        for line in fic.read().split('\n')[:-1]
                    ]
                else:
                    data = [line.split(split) for line in fic.read().split('\n')[:-1]]
    return data


def smart_split(data, pattern):
    if type(data) == str:
        return re.split(pattern, data)
    else:
        return [re.split(pattern, line) for line in data]