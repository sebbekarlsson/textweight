from textweight.similarity.jaro_winkler import jaro_winkler


def _find_best(word: str, words: list[str]):
    candidates = [(b, jaro_winkler(word, b)) for b in words if b != word]
    return sorted(candidates, key=lambda pair: pair[1], reverse=True)

def _find_best_one(word: str, words: list[str]) -> tuple[str, float]:
    return _find_best(word, words)[0]

def _find_best_word(word: str, words: list[str]) -> str:
    return _find_best_one(word, words)[0]






def test_jaro_winkler():
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
        'look'
    ]


    assert _find_best_word('car', words) == 'cat'
    assert _find_best_word('hello', words) == 'hallo'
    assert _find_best_word('scream', words) == 'cream'
