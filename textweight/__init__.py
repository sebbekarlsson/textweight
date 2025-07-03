from .constants import DEFAULT_SCORING_FUNCTION
from .scoring import score_candidates, score_find_best
from .structures.scored import Scored
from .similarity.jaro_winkler import jaro_winkler as jaro_winkler_similarity
from .similarity.levenshtein import levenshtein_similarity
from .similarity.keyboard_distance import keyboard_similarity

def compare(a: str, b: str) -> float:
    return DEFAULT_SCORING_FUNCTION(a, b)


__all__ = [
    'Scored',
    'compare',
    'levenshtein_similarity',
    'jaro_winkler_similarity',
    'keyboard_similarity',
    'score_candidates',
    'score_find_best'
]





