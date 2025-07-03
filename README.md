# textweight
Less strict string comparisons


## Basic Usage
```python
from textweight import compare

compare("hello", "hallo")  # 0.88
compare("hello", "world")  # 0.4666666666666666
compare("dog", "cat")      # 0.0
compare("think", "drink")  # 0.7333333333333334
compare("apple", "orange") # 0.5777777777777778
compare("late", "lake")    # 0.8666666666666667
compare("rain", "pain")    # 0.8333333333333334
compare("nice", "rice")    # 0.8333333333333334
compare("garlic", "bread") # 0.41111111111111115
compare("same", "same")    # 1.0
```
`compare` returns a "similarity" score from 0.0 -> 1.0.

## Other Methods
```python
from textweight import levenshtein_similarity, jaro_winkler_similarity, keyboard_similarity

levenshtein_similarity("hello", "hellu")  # 0.8
jaro_winkler_similarity("hello", "hellu")  # 0.92
keyboard_similarity("hello", "hellu")     # 0.9809291331384145
```
These also returns a "similarity" score from 0.0 -> 1.0.  
`keyboard_similarity` is a bit different, it's calculating the distance between keys on the keyboard  
to produce the score.
