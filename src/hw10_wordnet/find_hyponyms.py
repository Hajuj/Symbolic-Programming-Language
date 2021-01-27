import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

class HyponymSearcher(object):
    def __init__(self, text_path):

        self.noun_lemmas = []

        with open(text_path, mode = 'r') as file:
            text = file.read()
            sentence_splitter = nltk.sent_tokenize(text)
            tokens_splitter = nltk.word_tokenize(text)
            pos_tagging = nltk.pos_tag(tokens_splitter)
            lemmatizer = WordNetLemmatizer()
            nouns = [tag[0] for tag in pos_tagging if tag[1].startswith("N")]
            self.noun_lemmas = [lemmatizer.lemmatize(lemma, wordnet.NOUN) for lemma in nouns]

    def hypernymOf(self,synset1, synset2):
        if synset1 == synset2 or synset2 in synset1.hypernyms():
            return True
        for hypernym in synset1.hypernyms():
            if synset2 == hypernym:
                return True
            if self.hypernymOf(hypernym, synset2):
                return True
        return False

    def get_hyponyms(self,hypernym):
        hyponym = []
        for lemmas in self.noun_lemmas:
            for synset3 in wordnet.synsets(lemmas):
                if self.hypernymOf(synset3, hypernym):
                    hyponym.append(lemmas)
        return set(hyponym)