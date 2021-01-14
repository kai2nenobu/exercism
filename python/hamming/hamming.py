def distance(strand_a: str, strand_b: str):
    if len(strand_a) != len(strand_b):
        raise ValueError("Two strands must have the same length.")
    return sum([0 if a == b else 1 for a, b in zip(strand_a, strand_b)])
