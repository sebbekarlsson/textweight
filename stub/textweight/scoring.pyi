from collections.abc import Iterable
from textweight.common_types import ScoringFunction as ScoringFunction
from textweight.constants import DEFAULT_SCORING_FUNCTION as DEFAULT_SCORING_FUNCTION
from textweight.structures.scored import Scored as Scored

def score_candidates(text: str, candidates: Iterable[str], score_func: ScoringFunction[str] = ...) -> list[Scored[str]]: ...
def score_find_best(text: str, candidates: Iterable[str], score_func: ScoringFunction[str] = ...) -> Scored[str]: ...
