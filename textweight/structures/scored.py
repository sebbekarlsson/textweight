from dataclasses import dataclass, field

@dataclass
class Scored[T]:
    value: T = field()
    score: float | int = field(default=0)
