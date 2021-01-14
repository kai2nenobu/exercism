point_to_letters = {
    1: {'a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'},
    2: {'d', 'g'},
    3: {'b', 'c', 'm', 'p'},
    4: {'f', 'h', 'v', 'w', 'y'},
    5: {'k'},
    8: {'j', 'x'},
    10: {'q', 'z'}
}
letter_to_point = {
    letter: point for point, letters in point_to_letters.items() for letter in letters
}


def score(word: str):
    return sum([letter_to_point.get(letter, 0) for letter in word.lower()])

