def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    descending_scores = sorted(scores, reverse=True)
    return descending_scores[0:3]
