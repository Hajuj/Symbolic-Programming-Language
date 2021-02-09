from collections import defaultdict

import nltk


class Sentences:
    def __init__(self, sentences):
        """Construct and instance of the class Sentence from a list of
        pos-tagged sentences ([[(word,tag),...],...])"""
        self.sentences = sentences

    def __iter__(self):
        return iter(self.sentences)

    def __getitem__(self, i):
        return self.sentences[i]

    @classmethod
    def from_file(cls, path):
        """Create an instance of the class Sentences from a
        path. Reads the file and pos-tags the sentences in the
        file. [2 point]"""
        h = open(path)
        sentences = nltk.sent_tokenize(h.read())
        h.close()
        tags = []
        for sentence in sentences:
            tokens = nltk.word_tokenize(sentence)
            pos_tags = nltk.pos_tag(tokens)
            tags.append(pos_tags)
        h.close()
        return cls(tags)


class PosExpr:
    def __init__(self, expressions):
        """Construct an instance of the class PosExpr from a list of
        expressions."""
        self.expressions = expressions

    @classmethod
    def from_string(cls, expr):
        """Create an instance of the class PosExpr from the given
        string.  [0 points]"""
        return cls(nltk.word_tokenize(expr))

    @staticmethod
    def match_expr(expr, pos):
        """This method returns True if expr matches pos. An expression
        'XX' matches if pos equals 'XX', the expression '*' matches
        any pos and an expression XX* matches if pos starts with 'XX'
        or is equal to 'XX'.  [2 points]"""
        if expr == "*":
            return True
        elif len(expr) == len(pos) or "*" in expr:
            if expr[0] == expr[1] and pos[0] == pos[1]:
                return True
            elif expr[0] != expr[1] and pos[0] != pos[1]:
                return True
        else:
            return False

    def matches(self, sentence):
        """This method returns the list of matches in a pos-tagged
        sentence (list of (word,pos)-pairs). A match is a list of
        (word, pos)-pairs, where the tags in the sentence matched the
        expression mask provided by PosExpr for all possible
        positions.  [4 points]"""
        if len(self.expressions == 0):
            return []
        matches = []
        n = len(self.expressions)
        for i in range(0, len(sentence)):
            if PosExpr.match_expr(self.expressions[-1], sentence[i][1]):
                if PosExpr.match_all(self.expressions[0:-1], sentence[i - n + 1:i]):
                    matches.append(sentence[i - n + 1:i + 1])
        return matches

    @staticmethod
    def match_all(expressions, tuples):
        if len(expressions) != len(tuples):
            return False

        for i in range(0, len(expressions)):
            if not PosExpr.match_expr(expressions[i], tuples[i][1]):
                return False
        return True

def find(sentences, expr):
    """Return a list of strings that match the given expression. E.g.
    `find_string(sentences, "JJ NN") should return the list        [...,"prior year",...].  [2 points]"""
    m = PosExpr.from_string(expr)
    return [" ".join([w for w, _ in ms]) for s in sentences for ms in m.matches(s)]
