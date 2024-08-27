import re
import sys

from typing import Tuple, Dict, List


def read_config(config_file: str) -> Dict[str, str]:
    with open(config_file, 'r') as file:
        return {a[0]: a[1] for line in file if (a := line.strip().split('='))}


def replace_in_text(text_file: str, replacements: Dict[str, str]) -> List[Tuple[str, int]]:
    res = []
    with open(text_file, 'r') as file:
        for line in file:
            line = line.strip()
            total_replacements = 0
            for key in sorted(replacements.keys(), key=len, reverse=True):
                line, count = re.subn(re.escape(key), replacements[key], line)
                total_replacements += count
            res.append((line, total_replacements))
        res.sort(key=lambda x: x[1], reverse=True)
        return res


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <config_file> <text_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    text_file = sys.argv[2]

    config = read_config(config_file)
    result = replace_in_text(text_file, config)

    for i in result:
        print(i[0])
