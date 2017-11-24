from itertools import groupby
def decode(string):
    string = str(string)
    return_string = ''
    current_digit = 0
    for c in string:
        if c.isdigit():
            current_digit = (int(current_digit) *10) +  int(c)
        elif current_digit == 0:
            return_string+=c
        else:
            return_string+=c*int(current_digit)
            current_digit = 0
    return return_string


def encode(string):
    return ''.join(map(lambda g: helper(g), [list(g) for k, g in groupby(string)]))

def helper(g):
    return g[0] if len(g) == 1 else str(len(g)) + g[0]


if __name__ == '__main__':
    print(decode(encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB')))

