def is_isogram(string: str) -> bool:
    lower_string = string.lower()
    letter_occurrence = {}
    for idx, letter in enumerate(lower_string):
        if letter in letter_occurrence:
            letter_occurrence[letter].append(idx)
        else:
            letter_occurrence[letter] = [idx]
    for letter, indices in letter_occurrence.items():
        # Ignore hyphens and spaces
        if letter in ['-', ' ']:
            continue
        if len(indices) > 1:
            return False
    return True
