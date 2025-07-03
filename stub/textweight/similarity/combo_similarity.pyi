from textweight.similarity.jaro_winkler import jaro_winkler as jaro_winkler
from textweight.similarity.keyboard_distance import keyboard_similarity as keyboard_similarity
from textweight.similarity.levenshtein import levenshtein_similarity as levenshtein_similarity

def combo_similarity(a: str, b: str) -> float: ...
