import re


def count_words(sentence: str):
    lower_sentence = sentence.lower()
    word_regex = re.compile(r"[a-z0-9]+'?[a-z0-9]*")
    word_counts = {}
    for match in word_regex.finditer(lower_sentence):
        word = re.sub("'$", "", match.group(0))  # Remove a trailing apostrophe
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
