from nltk import word_tokenize


def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
    tokens = word_tokenize(text.toLower())
    return tokens


def countWords(text):
    tokens = normalized_tokens(text)
    dic = {}
    for token in tokens:
        if token in dic:
            dic[token] += 1
        else:
            dic[token] = 1
    return dict


class TextDocument:
    def __init__(self, text, id=None):
        """ This creates a TextDocument instance with a string, a dictionary and an identifier. """
        self.text = text
        self.word_to_count = countWords(text)
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

        string = open(self, "r").read()
        if len(string) >= 25:
            string = string[::23] + "..."
        return string

    from_file("example_document1.txt").__str__()

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
        num = 0
        tokens1 = normalized_tokens(self)
        tokens2 = normalized_tokens(other_doc)
        i = 0

        for token in tokens1:
            if token == tokens2[i]:
                num += 1
            i += 1

        return num
