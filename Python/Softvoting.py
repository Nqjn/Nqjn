
def soft_voting(probability_distributions: list[list[float]]) -> list[float]:
    return [sum(col) / len(probability_distributions) for col in
    zip(*probability_distributions)]

# Testy:
print(soft_voting([[0.5, 0.4, 0.1], [0.2, 0.5, 0.3], [0.4, 0.3, 0.3]]))  # [0.366666666, 0.4, 0.233333333333]
