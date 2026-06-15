def filter_length(words, min_len, max_len):
    return [w for w in words if min_len <= len(w) <= max_len]