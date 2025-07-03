from collections.abc import Iterable

def _generate_test_pairs(words: list[str]) -> Iterable[tuple[str, str]]:
    for i, a in enumerate(words):
        for j, b in enumerate(words):
            if i == j: continue
            yield a, b
            
def generate_test_pairs(words: list[str]) -> list[tuple[str,str]]:
    return list(_generate_test_pairs(words))

def _generate_test_candidates(words: list[str]) -> Iterable[tuple[str, list[str]]]:
    for a in words:
        yield a, [b for b in words if b != a]

def generate_test_candidates(words: list[str]) -> list[tuple[str, list[str]]]:
    return list(_generate_test_candidates(words))
