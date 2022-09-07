import sys
import re

orig_cases = {
  "cases": [
    {"exe": "test_bin -a -b -gpu 3 -d -e, timeout  10"},
    {"exe": "test_bin -b -gpu   3 -d -e, timeout 20"},
    {"exe": "test_bin  -b -gpu -d -e, timeout  20"},
    {"exe": "test_bin -a -c -gpu  4  -d, timeout 30"},
    {"exe": "test_bin -b -gpu    3a -d   -e, timeout 20"},
    {"exe": "test_bin -b -gpu    13 -d   -e, timeout 20"}
  ]
}


def load_case_by_gpu(orig_cases):
    """
    parse the cases from orig_cases, and return new cases object in dict format with index by GPU number
    Note:
        1. GPU number is integer from 1 to 8, your code should ignore other invalid scenario
        2. those raw command has some redundant space, your code should format it to single space.
    GPU index:
       From case exe: "exe": "test_bin -a -b -gpu 3 -d -e", match '-gpu ?', then get the index '3'
    @example:
        new_cases = load_case_by_gpu(orig_cases)
            new_cases: python object
    """
    new_cases = {}
    data = orig_cases['cases']
    for x in data:
        x['exe'] = " ".join(x['exe'].split())
        key = re.search('-gpu\s+([1-8]) ', x['exe'])
        if key:
            gpu_idx = key.group(1)
            if gpu_idx not in new_cases:
                new_cases[gpu_idx] = [x]
            else:
                new_cases[gpu_idx].append(x)
    return new_cases


if __name__ == '__main__':
    new_cases = load_case_by_gpu(orig_cases)
    print(new_cases)


