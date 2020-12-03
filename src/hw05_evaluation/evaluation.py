import random

hams = "reminder deadline meet thanks thanks for tip deadline approaching".split(" ")
spams = "hot stock tip meet hot single".split(" ")
list1 = [('ham', 'ham')] * 58 + [('spam', 'ham')] * 21 + [('ham', 'spam')] * 9 + [('spam', 'spam')] * 12
random.shuffle(list1)


def precision(k, classes):
    """ Calculate the precision of class `k` for the classifications in `classes`.
    Each element in classes is a tuple.  The first element in the tuple specifies
    the calssification of the classifier.  The second element specifies the real
    class. [2 points]
    >>> round(precision('spam', list1), 4)
    0.3636
    >>> round(precision('ham', list1), 4)
    0.8657
    >>> round(precision('spam', []), 4)
    0.0
    """
    pass


def recall(k, classes):
    """ Calculate the recall of class `k` for the classifications in `classes`.
    Each element in classes is a tuple.  The first element in the tuple specifies
    the calssification of the classifier.  The second element specifies the real
    class. [2 points]
    >>> round(recall('spam', list1), 4)
    0.5714
    >>> round(recall('ham', list1), 4)
    0.7342
    >>> round(recall('spam', []), 4)
    0.0
    """
    pass


def f1(k, classes):
    """ Calculate the F1-measure of class `k` for the classifications in `classes`.
    Each element in classes is a tuple.  The first element in the tuple specifies
    the calssification of the classifier.  The second element specifies the real
    class. [1 point]
    >>> round(f1('spam', list1), 4)
    0.4444
    >>> round(f1('ham', list1), 4)
    0.7945
    >>> round(f1('spam', []), 4)
    0.0
    """
    pass


class RelFreq:
    def __init__(self, ham, spam):
        """Initialize a RelFreq instance with a list of spam words and a list of ham words."""
    pass

    def get_rel_freq(self, word):
        """Returns the relative frequency for `word`. [1 point]
        >>> round(RelFreq(hams, spams).get_rel_freq('meet'), 4)
        0.1333
        >>> round(RelFreq(hams, spams).get_rel_freq('single'), 4)
        0.0667
        >>> round(RelFreq([], []).get_rel_freq('deadline'), 4)
        0.0
        """
    pass

    def get_rel_freq_ham(self, word):
        """Returns the relative frequency for `word` given ham. [1 point]
        >>> round(RelFreq(hams, spams).get_rel_freq_ham('meet'), 4)
        0.1111
        >>> round(RelFreq(hams, spams).get_rel_freq_ham('deadline'), 4)
        0.2222
        >>> round(RelFreq([], []).get_rel_freq_ham('deadline'), 4)
        0.0
        """
    pass

    def get_rel_freq_spam(self, word):
        """Returns the relative frequency for `word` given spam. [1 point]
        >>> round(RelFreq(hams, spams).get_rel_freq_spam('meet'), 4)
        0.1667
        >>> round(RelFreq(hams, spams).get_rel_freq_spam('hot') , 4)
        0.3333
        >>> round(RelFreq([], []).get_rel_freq_spam('deadline'), 4)
        0.0
        """
    pass
