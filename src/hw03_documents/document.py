from nltk import word_tokenize


def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
    tokens = word_tokenize(text.lower())
    return tokens


def count(text):
    tokens = normalized_tokens(text)
    dic = dict()
    for word in tokens:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


class TextDocument:
    def __init__(self, text, id=None):
        """ This creates a TextDocument instance with a string, a dictionary and an identifier. """
        self.text = text
        self.word_to_count = count(text)
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDocument instance by reading a file. """
        text = open(filename, "r").read()
        return cls(text, filename)

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """
        string = self.text
        if len(string) > 25:
            string = string[:22] + "..."
        return string

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
        tokens1 = normalized_tokens(self.text)
        tokens2 = normalized_tokens(other_doc.text)
        return len(set(tokens2) & set(tokens1))
