import math
from typing import overload

def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))

def sign(x: float | int) -> float:
    return -1.0 if x < 0.0 else 1.0

@overload
def clamp(v: int, minv: int, maxv: int) -> int: ...
@overload
def clamp(v: float, minv: float, maxv: float) -> float: ...
def clamp(v: float | int, minv: float | int, maxv: float | int) -> float | int:
    return max(minv, min(maxv, v))

def lerp(vfrom: float, vto: float, scale: float) -> float:
    return vfrom + (vto - vfrom) * scale

def sgt(a: float, b: float, s: float) -> float:
    h = clamp(0.5 + 0.5 * (a - b) / s, 0.0, 1.0)
    return lerp(0.0, 1.0, h*h*(3.0-2.0*h)) 

def slt(a: float, b: float, s: float) -> float:
    h = clamp(0.5 + 0.5 * (b - a) / s, 0.0, 1.0)
    return lerp(0.0, 1.0, h*h*(3.0-2.0*h))

def smin(a: float, b: float, k: float) -> float:
    h = clamp(0.5+0.5*(b - a) / k, 0.0, 1.0)
    return lerp(b, a, h) - k * h * (1.0 - h)

def smax(a: float, b: float, k: float) -> float:
    h = clamp(0.5+0.5*(b - a) / k, 0.0, 1.0)
    return lerp(a, b, h) + k * h * (1.0 - h)
