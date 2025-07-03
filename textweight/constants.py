from textweight.common_types import ScoringFunction
from textweight.similarity.jaro_winkler import jaro_winkler_default


DEFAULT_SCORING_FUNCTION: ScoringFunction[str] = jaro_winkler_default
