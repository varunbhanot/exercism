import re
def hey(phrase):
    question_pattern = re.compile('[a-z]*[?]$',re.IGNORECASE)
    saying_pattern = re.compile('[a-z]+$',re.IGNORECASE)
    phrase = str(phrase)
    if phrase.isupper():
        return "Whoa, chill out!"
    elif re.match(question_pattern,phrase):
        return "Sure."
    elif not re.match(saying_pattern,phrase):
        return "Fine. Be that way!"
    else:
        return "Whatever."
    pass