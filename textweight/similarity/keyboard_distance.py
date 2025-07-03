# pyright: basic


from functools import reduce
from textweight.maths.vector import VEC2
import math

type CoordTable = dict[str, VEC2]

def build_coordinate_table(layout: list[str]) -> CoordTable:
    def _get_char_coord(char: str) -> VEC2:
        for y, row in enumerate(layout):
            for x, col in enumerate(row):
                if col == char:
                    return VEC2(x, y)
        return VEC2(-1, -1)
    return {key: _get_char_coord(key) for key in ''.join(layout)}


def normalize_table(table: CoordTable) -> CoordTable:
    points = list(table.values())
    total = reduce(lambda a, b: a.add(b), points)
    center = total.scale(1.0 / float(len(points)))
    return {k: v.sub(center).unit() for k, v in table.items()}

KEYBOARD_LAYOUT: list[str] = [
    '1234567890-=',
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./"
]
KEYBOARD_LAYOUT_FLAT = ''.join(KEYBOARD_LAYOUT)
COORD_TABLE: CoordTable = normalize_table(build_coordinate_table(KEYBOARD_LAYOUT))

KEYBOARD_LAYOUT_SHIFT: list[str] = [
    '!@#$%^&*()_+',
    "QWERTYUIOP{}|",
    "asdfghjkl:\"",
    "zxcvbnm<>?"
]
KEYBOARD_LAYOUT_SHIFT_FLAT = ''.join(KEYBOARD_LAYOUT_SHIFT)
COORD_TABLE_SHIFT: CoordTable = normalize_table(build_coordinate_table(KEYBOARD_LAYOUT_SHIFT))


def _coord(a: str) -> VEC2:
    return COORD_TABLE.get(a, COORD_TABLE_SHIFT.get(a)) or VEC2(-1, -1)

def _shift(a: str) -> int: return 1 if a in KEYBOARD_LAYOUT_SHIFT_FLAT else 0

def keyboard_key_dot(a: str, b: str):
    return _coord(a).dot(_coord(b)) * (1.0 + float(abs(_shift(b) - _shift(a))))

def keyboard_key_distance(a: str, b: str):
    return _coord(a).distance(_coord(b)) * (1.0 +  float(abs(_shift(b) - _shift(a))))

def _max_distance():
    max_dist: float = -100.0
    for _i, a in enumerate(KEYBOARD_LAYOUT_FLAT):
        for _j, b in enumerate(KEYBOARD_LAYOUT_FLAT):
            dist = keyboard_key_distance(a, b) 
            max_dist = max(max_dist, dist)

    for _i, a in enumerate(KEYBOARD_LAYOUT_SHIFT_FLAT):
        for _j, b in enumerate(KEYBOARD_LAYOUT_SHIFT_FLAT):
            dist = keyboard_key_distance(a, b) 
            max_dist = max(max_dist, dist)
    
    return max_dist


MAX_DISTANCE: float = _max_distance()

def _sort(a: str, b: str) -> tuple[str, str]:
    la = len(a)
    lb = len(b)
    pair: list[str] = [a, b]
    longest_idx: int = 0 if la > lb else 1
    longest = pair[longest_idx] 
    shortest = pair[(longest_idx + 1) % 2]
    return (longest, shortest)


def keyboard_dot(a: str, b: str) -> float:
    longest, shortest = _sort(a, b)
    longlen = len(longest)
    shortlen = len(shortest)

    total: float = 0.0

    for li, longc in enumerate(longest):
        li_n = float(li) / float(longlen)
        si = round(li_n * shortlen)
        shortc = shortest[si]
        total += keyboard_key_dot(longc, shortc)
        
    return total 


def keyboard_distance(a: str, b: str) -> float:
    longest, shortest = _sort(a, b)
    longlen = len(longest)
    shortlen = len(shortest)

    total: float = 0.0

    for li, longc in enumerate(longest):
        li_n = float(li) / float(longlen)
        si = math.floor(li_n * shortlen)
        shortc = shortest[si]
        total += keyboard_key_distance(longc, shortc)
        
    return total / (MAX_DISTANCE * longlen) 


def keyboard_similarity(a: str, b: str) -> float:
    if a == b: return 1.0
    dist = keyboard_distance(a, b)
    if dist <= 0.0: return 1.0
    return 1.0 - dist
