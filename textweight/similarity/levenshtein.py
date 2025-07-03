def levenshtein_distance(a: str, b: str) -> int:
    la, lb = len(a), len(b)
    if la <= 0 or lb <= 0:
        return 0

    # Initialize the matrix
    matrix = [[0] * (lb + 1) for _ in range(la + 1)]

    for i in range(la + 1):
        for j in range(lb + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(
                    matrix[i][j - 1],
                    matrix[i - 1][j],
                    matrix[i - 1][j - 1]
                ) + 1

    return matrix[la][lb]


def levenshtein_distance_normalized(a: str, b: str) -> float:
    la, lb = len(a), len(b)
    if la <= 0 or lb <= 0:
        return 0.0

    dist = levenshtein_distance(a, b)
    max_length = max(la, lb)
    return dist / max_length

def levenshtein_similarity(a: str, b: str) -> float:
    return 1.0 - levenshtein_distance_normalized(a, b)
