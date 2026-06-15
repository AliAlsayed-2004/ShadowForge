LEET_MAP = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1'],
    'o': ['o', '0'],
    's': ['s', '$', '5']
}

def leet(word):
    result = ['']
    for c in word:
        if c.lower() in LEET_MAP:
            result = [p + l for p in result for l in LEET_MAP[c.lower()]]
        else:
            result = [p + c for p in result]
    return result