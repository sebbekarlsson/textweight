from .scoring import score_candidates as score_candidates, score_find_best as score_find_best
from .similarity.jaro_winkler import jaro_winkler as jaro_winkler_similarity
from .similarity.keyboard_distance import keyboard_similarity as keyboard_similarity
from .similarity.levenshtein import levenshtein_similarity as levenshtein_similarity
from .structures.scored import Scored as Scored

__all__ = ['Scored', 'compare', 'levenshtein_similarity', 'jaro_winkler_similarity', 'keyboard_similarity', 'score_candidates', 'score_find_best']

def compare(a: str, b: str) -> float: ...
