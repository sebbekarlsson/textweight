from collections.abc import Callable

type Numeric = float | int
type ScoringFunction[T] = Callable[[T, T], Numeric]
