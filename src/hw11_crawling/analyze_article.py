import string

import nltk
import urllib.request
import bs4
from collections import defaultdict


def get_html(url):
    return urllib.request.urlopen(url).read().decode("utf-8")


def get_text(html):
    # TODO create the list of clean paragraphs (no HTML markup) from the given html
    # TODO return paragraphs as a string. Hint: join the list of paragraphs by newline
    soup = bs4.BeautifulSoup(html, 'html.parser')
    div = soup.find_all('p')
    str = ""
    for p in div:
            str += (p.get_text() + "\n")
    str = str[:-1]
    return str


def get_headline(html):
    # TODO return the headline of html
    soup = bs4.BeautifulSoup(html, 'html.parser')

    return soup.title.string.split("-", 1)[0][:-1]


def get_normalized_tokens(text):
    # TODO tokenize the text with NLTK and return list of lower case tokens without stopwords
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.word_tokenize(text)
    filtered_text = [w.lower() for w in word_tokens if w not in stop_words]
    return filtered_text
    pass


def get_pos_dict(tokens):
    # TODO return a dictionary of homographs (a dictionary of words and their possible POS)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_text = [w.lower() for w in tokens if w not in stop_words]
    pos_tags = nltk.pos_tag(filtered_text)

    alltags = defaultdict(set)

    for word, tag in pos_tags:
        alltags[word].add(tag)

    return alltags

def filter_dict_homographs(word_dict_h):
    # TODO delete an entry from dictionary, if not a homograph
    for word in list(word_dict_h):
        tag = word_dict_h[word]
        if len(tag) < 2:
             word_dict_h.pop(word)
    return word_dict_h



def find_homographs(tokens):
    # TODO return a dictionary which holds homographs
    tags = get_pos_dict(tokens)
    filter_dict_homographs(tags)
    homographs = dict(tags)
    return homographs

