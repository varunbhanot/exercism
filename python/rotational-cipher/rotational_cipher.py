import string
def rotate(text, key):
    key = key % 26
    low, up = string.ascii_lowercase, string.ascii_uppercase
    mapping = dict(zip(low + up, low[key:] + low[:key] + up[key:] + up[:key]))
    return ''.join(mapping[ch] if ch in mapping else ch for ch in text)

if __name__ == '__main__':
    rotate('abcdefghijklmnopqrstuvwxyz',13)