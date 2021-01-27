import nltk
from nltk.corpus import udhr


class LangModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        # TODO return ConditionalFrequencyDistribution of words in the UDHR corpus conditioned on each language
        # hint: use nltk.ConditionalFreqDist
        cfd = nltk.ConditionalFreqDist(
            (lang, word.lower())
            for lang in self.languages
            for word in udhr.words(lang + '-Latin1'))
        return cfd

    def guess_language(self, language_model_cfd, text):
        """Returns the guessed language for the given text"""

        # TODO for each language calculate the overall score of a given text
        # based on the frequency of words accessible by language_model_cfd[language].freq(word) and then
        # identify most likely language for a given text according to this score
        res = {}
        tokenizer = nltk.word_tokenize(text)
        for lang in language_model_cfd.conditions():
            score = 0
            for word in tokenizer:
                score += language_model_cfd[lang][word]
                res[lang] = score
        res = [lang for lang, word in sorted(res.items(), key=lambda x: x[1], reverse=True)]
        return res[0]
