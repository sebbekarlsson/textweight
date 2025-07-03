from textweight.similarity.jaro_winkler import jaro_winkler
from textweight.similarity.keyboard_distance import keyboard_similarity
from textweight.similarity.levenshtein import levenshtein_similarity


def combo_similarity(a: str, b: str) -> float:
    jaro = jaro_winkler(a, b)
    lev = levenshtein_similarity(a, b)
    keyboard = keyboard_similarity(a, b)

    return (jaro + lev + keyboard) * 0.3333333333333333
    
