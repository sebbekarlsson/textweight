from collections.abc import Iterable

from textweight.common_types import ScoringFunction
from textweight.constants import DEFAULT_SCORING_FUNCTION
from textweight.structures.scored import Scored


def score_candidates(
    text: str,
    candidates: Iterable[str],
    score_func: ScoringFunction[str] = DEFAULT_SCORING_FUNCTION
) -> list[Scored[str]]:
    return sorted(
        [Scored[str](b, score_func(text, b)) for b in candidates if b != text],
        key=lambda s: s.score, reverse=True
    )

def score_find_best(
    text: str,
    candidates: Iterable[str],
    score_func: ScoringFunction[str] = DEFAULT_SCORING_FUNCTION
) -> Scored[str]:
    return score_candidates(text, candidates=candidates, score_func=score_func)[0] 
