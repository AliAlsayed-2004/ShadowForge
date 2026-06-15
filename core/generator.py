import itertools

def apply_patterns(words, numbers, symbols, use_symbols):

    results = []

    for w in words:
        results.append(w)
        results.append(w.capitalize())
        results.append(w.upper())

        for n in numbers:
            results.append(w + n)
            results.append(n + w)

        if use_symbols:
            for s in symbols:
                results.append(w + s)
                results.append(s + w)

        for a, b in itertools.permutations(words, 2):
            results.append(a + b)

    return results