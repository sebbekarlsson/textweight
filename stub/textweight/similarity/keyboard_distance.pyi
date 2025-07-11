from _typeshed import Incomplete
from textweight.maths.vector import VEC2 as VEC2

type CoordTable = dict[str, VEC2]
def build_coordinate_table(layout: list[str]) -> CoordTable: ...
def normalize_table(table: CoordTable) -> CoordTable: ...

KEYBOARD_LAYOUT: list[str]
KEYBOARD_LAYOUT_FLAT: Incomplete
COORD_TABLE: CoordTable
KEYBOARD_LAYOUT_SHIFT: list[str]
KEYBOARD_LAYOUT_SHIFT_FLAT: Incomplete
COORD_TABLE_SHIFT: CoordTable

def keyboard_key_dot(a: str, b: str): ...
def keyboard_key_distance(a: str, b: str): ...

MAX_DISTANCE: float

def keyboard_dot(a: str, b: str) -> float: ...
def keyboard_distance(a: str, b: str) -> float: ...
def keyboard_similarity(a: str, b: str) -> float: ...
