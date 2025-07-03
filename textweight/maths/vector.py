import dataclasses
from dataclasses import field as FIELD
import math
from textweight.maths.functions import sign 


@dataclasses.dataclass
class VEC2:
    x: float | int = FIELD(default=0.0)
    y: float | int = FIELD(default=0.0)

    def dot(self, b: 'VEC2') -> float:
        return self.x * b.x + self.y * b.y

    def mag(self) -> float:
        return math.sqrt(math.pow(self.x, 2.0) + math.pow(self.y, 2.0))

    def distance(self, b: 'VEC2') -> float:
        return math.sqrt(math.pow(self.x - b.x, 2.0) + math.pow(self.y - b.y, 2.0))

    def distance_manhattan(self, b: 'VEC2') -> float:
         return abs(self.x - b.x) + abs(self.y - b.y)

    def distance_hypot(self, b: 'VEC2') -> float:
        return math.hypot(b.x - self.x, b.y - self.y)

    def distance_dot(self, b: 'VEC2') -> float:
        diff = b.sub(self)
        return diff.dot(diff)

    def unit(self) -> 'VEC2':
        mag = self.mag()
        if mag < 0.000000000001:
            return VEC2(sign(self.x) * 0.5, sign(self.y) * 0.5)
        return VEC2(self.x / mag, self.y / mag)

    def add(self, b: 'VEC2') -> 'VEC2':
        return VEC2(self.x + b.x, self.y + b.y)

    def sub(self, b: 'VEC2') -> 'VEC2':
        return VEC2(self.x - b.x, self.y - b.y)

    def mul(self, b: 'VEC2') -> 'VEC2':
        return VEC2(self.x * b.x, self.y * b.y)

    def div(self, b: 'VEC2') -> 'VEC2':
        return VEC2(self.x / b.x, self.y / b.y)

    def scale(self, s: float | int) -> 'VEC2':
        return VEC2(self.x * float(s), self.y * float(s))



@dataclasses.dataclass
class VEC3:
    x: float | int = FIELD(default=0.0)
    y: float | int = FIELD(default=0.0)
    z: float | int = FIELD(default=0.0)

    def dot(self, b: 'VEC3') -> float:
        return self.x * b.x + self.y * b.y + self.z * b.z

    def mag(self) -> float:
        return math.sqrt(math.pow(self.x, 2.0) + math.pow(self.y, 2.0) + math.pow(self.z, 2.0))

    def distance(self, b: 'VEC3') -> float:
        return math.sqrt(math.pow(self.x - b.x, 2.0) + math.pow(self.y - b.y, 2.0) + math.pow(self.z - b.z, 2.0))


    def unit(self) -> 'VEC3':
        mag = self.mag()
        if mag < 0.000000000001:
            return VEC3(sign(self.x) * 0.333, sign(self.y) * 0.333, sign(self.z) * 0.333)
        return VEC3(self.x / mag, self.y / mag, self.z / mag)

    def add(self, b: 'VEC3') -> 'VEC3':
        return VEC3(self.x + b.x, self.y + b.y, self.z + b.z)

    def sub(self, b: 'VEC3') -> 'VEC3':
        return VEC3(self.x - b.x, self.y - b.y, self.z - b.z)

    def mul(self, b: 'VEC3') -> 'VEC3':
        return VEC3(self.x * b.x, self.y * b.y, self.z * b.z)

    def div(self, b: 'VEC3') -> 'VEC3':
        return VEC3(self.x / b.x, self.y / b.y, self.z / b.z)

    def scale(self, s: float | int) -> 'VEC3':
        return VEC3(self.x * float(s), self.y * float(s), self.z * float(s))
