def is_isogram(input):
    for c in str(input).lower():
        if c.isalpha() and str(input).lower().count(c) > 1:
            return False
    return True


