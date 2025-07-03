def jaro(s1: str, s2: str) -> float:
    if s1 == s2: return 1.0

    len1, len2 = len(s1), len(s2)
    if len1 <= 0 or len2 <= 0: return 0.0

    match_dist = max(len1, len2) // 2 - 1
    s1_matches = [False] * len1
    s2_matches = [False] * len2
    matches = 0
    for i, c1 in enumerate(s1):
        start = max(0, i - match_dist)
        end = min(i + match_dist + 1, len2)
        for j in range(start, end):
            if not s2_matches[j] and c1 == s2[j]:
                s1_matches[i] = s2_matches[j] = True
                matches += 1
                break

    if matches <= 0: return 0.0

    transpositions = sum(
        1 for c1, c2 in
        zip(
            [s1[i] for i in range(len1) if s1_matches[i]],
            [s2[i] for i in range(len2) if s2_matches[i]]
        ) if c1 != c2
    ) / 2

    return (
        (matches / len1)
        + (matches / len2)
        + ((matches - transpositions) / matches)
    ) / 3.0

def jaro_winkler(s1: str, s2: str, prefix_scaling: float = 0.1, common_prefix_length: int = 4) -> float:
    jaro_dist = jaro(s1, s2)

    prefix_len = 0
    for i in range(min(len(s1), len(s2), common_prefix_length)):
        if s1[i] == s2[i]: prefix_len += 1
        else: break

    return jaro_dist + (prefix_len * prefix_scaling * (1.0 - jaro_dist))

def jaro_winkler_default(s1: str, s2: str) -> float: return jaro_winkler(s1, s2)
