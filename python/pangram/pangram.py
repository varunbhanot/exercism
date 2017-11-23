import itertools
def is_pangram(sentence):
    count = 0
    final_string = ''.join(ch for ch, _ in itertools.groupby(sentence))
    return len(final_string) == 26


