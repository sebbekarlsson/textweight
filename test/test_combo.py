from textweight.scoring import score_candidates
from textweight.similarity.combo_similarity import combo_similarity
from textweight.validation_utils import generate_test_candidates

def _find_best(word: str, words: list[str]):
    candidates = [(b, combo_similarity(word, b)) for b in words if b != word]
    return sorted(candidates, key=lambda pair: pair[1], reverse=True)

def _find_best_one(word: str, words: list[str]) -> tuple[str, float]:
    return _find_best(word, words)[0]

def _find_best_word(word: str, words: list[str]) -> str:
    return _find_best_one(word, words)[0]

def test_levenshtein_similarity():
    words = [
        'car',
        'dog',
        'cat',
        'horse',
        'apple',
        'banana',
        'large',
        'small',
        'drink',
        'food',
        'zoo',
        'hello',
        'hallo',
        'world',
        'curled',
        'green',
        'purple',
        'orange',
        'cookie',
        'lake',
        'take',
        'hate',
        'male',
        'female',
        'man',
        'woman',
        'boy',
        'girl',
        'blue',
        'pink',
        'time',
        'date',
        'plate',
        '<div>',
        '<span>',
        '!@#$%^&*()_',
        '1234567890-=',
        'number',
        'thunder',
        'scream',
        'cream',
        'ice cream',
        'seen',
        'look',
        'think',
        'wink',
        'link',
        'sink',
        'frog',
        'fog',
        'electricity',
        'city',
        'town',
        'garlic',
        'water',
        'walking',
        'talking',
        'parking',
        'warning!',
        'farming',
        'darling',
        'important!'
    ]



    assert _find_best_word('car', words) == 'cat'
    assert _find_best_word('hello', words) == 'hallo'
    assert _find_best_word('scream', words) == 'cream'


    for word, candidates in generate_test_candidates(words):
        print(word)
        for i, cand in enumerate(score_candidates(word, candidates, score_func=combo_similarity)):
            print(f'  .{i+1} - {cand.value} | {cand.score}')
            if i >= 5: break
