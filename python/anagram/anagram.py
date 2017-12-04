def detect_anagrams(word, candidates):
    sorted_word = sorted(word)
    return list(candidate for candidate in candidates if sorted(candidate)==sorted_word)

