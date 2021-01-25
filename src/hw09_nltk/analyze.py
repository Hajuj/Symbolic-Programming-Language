import nltk
from nltk import FreqDist
from nltk import word_tokenize


class Analyzer(object):
    def __init__(self, path):
        """reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution """
        h = open(path)
        self.text = nltk.word_tokenize(h.read())
        self.token_counts = nltk.FreqDist(self.text)

    def numberOfTokens(self):
        """returns number of tokens in the text """
        return len(self.text)

    def vocabularySize(self):
        """returns a list of the vocabulary of the text """
        return len(self.token_counts)

    def lexicalDiversity(self):
        """returns the lexical diversity of the text """
        return self.numberOfTokens() / self.vocabularySize()

    def getKeywords(self):
        """return words as possible key words, that are longer than seven characters, that occur more than seven
        times (sorted alphabetically) """
        return sorted([keyword for (keyword, wert) in self.token_counts.items() if len(keyword) > 7 and wert > 7])

    def numberOfHapaxes(self):
        """returns the number of hapaxes in the text"""
        return len(self.token_counts.hapaxes())

    def avWordLength(self):
        """returns the average word length of the text"""
        laenge = 0
        for wort in self.token_counts:
            laenge += len(wort)
        return laenge / self.vocabularySize()

    def topSuffixes(self):
        """returns the 10 most frequent 2-letter suffixes in words
            (restrict to words of length 5 or more)"""
        sufCount = nltk.FreqDist([wort[-2:] for wort in self.token_counts if len(wort) >= 5])
        sorted_counts = [suffix for suffix, count in sorted(sufCount.items(), key=lambda x: x[1], reverse=True)]
        return sorted_counts[:10]

    def topPrefixes(self):
        """returns the 10 most frequent 2-letter prefixes in words
            (restrict to words of length 5 or more)"""
        preCount = nltk.FreqDist([wort[:2] for wort in self.token_counts if len(wort) >= 5])
        sorted_counts = [prefix for prefix, count in sorted(preCount.items(), key=lambda x: x[1], reverse=True)]
        return sorted_counts[:10]

    def tokensTypical(self):
        """returns first 5 tokens of the (alphabetically sorted) vocabulary
        that contain both often seen prefixes and suffixes in the text. As in topPrefixes()
        and topSuffixes(), Prefixes and Suffixes are 2 characters long."""
        topPre = self.topPrefixes()
        topSuf = self.topSuffixes()
        typicalTokens = [top for top in self.token_counts if top[-2:] in topSuf and top[:2] in topPre]
        return sorted(typicalTokens)[:5]
