import itertools
def is_pangram(sentence):
    sentence = str(sentence)
    final_set = set(c.lower() for c in sentence if c.isalpha())
    return len(final_set) == 26


