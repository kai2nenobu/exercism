import re


def abbreviate(words: str):
    return ''.join([
        word[0].upper() for word in re.split(r"[-_ ]+", words) if word[0].isalpha()
    ])
