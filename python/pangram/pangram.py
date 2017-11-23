import itertools
def is_pangram(sentence):
    count = 0
    final_string = ''.join(ch for ch, _ in itertools.groupby(sentence))
    print final_string

if __name__ == '__main__':
    is_pangram("abcdddee")

