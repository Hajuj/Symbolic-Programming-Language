# This exercise contains 5 Tasks to practice a powerful feature of Python: comprehensions.
# With these, multiple-line for-loop constructions can be expressed in expressive one-liners.


def multiply_by(x, list1):
    """
    Multiplies each value in list1 by x and returns it as a new list.
    """
    return [y*x for y in list1]


def check_division(x, list1):
    """
    Takes a list and returns a list indicating whether or not each element in the original list can be divided by x.
    (e.g check_division(3, [1,2,3]) -> [False, False, True])
    """
    return [(y % x == 0) for y in list1]


def div_less(set1):
    """
    Return a new set only containing numbers that can`t be divided by any other number (except itself)
    from the original set.
    """
    return set1 - {x for x in set1 for y in set1 if x % y == 0 and x != y}


def map_zip(list1, list2):
    """
    It should return a dictionary mapping the 'nth' element in list1 to the 'nth' element in list2.
    Make use of the 'zip()' function in your dictionary comprehension, that can handle lists of different sizes
    automatically.
    """
    return dict(zip(list1, list2))


def word_to_length(list1):
    """
    Returns a dictionary mapping all words with at least 3 characters to their number of characters.
    """
    return {word: len(word) for word in list1 if len(word) >= 3}
