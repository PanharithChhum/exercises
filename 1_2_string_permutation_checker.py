from collections import defaultdict

def check_permutation(str1, str2):
    dict1, dict2 = defaultdict(int), defaultdict(int)
    for char1, char2 in zip(str1, str2):
        dict1[char1] += 1
        dict2[char2] += 1
    if dict1 == dict2:
        return True
    else:
        return False

print check_permutation("abcdef","fedcba")