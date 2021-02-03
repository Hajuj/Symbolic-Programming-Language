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
        if p ==div[len(div)-1]:
            str+=  p.get_text()
        else:
            str += (p.get_text() + "\n")
    return str


def get_headline(html):
    # TODO return the headline of html
    soup = bs4.BeautifulSoup(html, 'html.parser')

    return soup.title.text



def get_normalized_tokens(text):
    # TODO tokenize the text with NLTK and return list of lower case tokens without stopwords
    pass


def get_pos_dict(tokens):
    # TODO return a dictionary of homographs (a dictionary of words and their possible POS)
    pass


def filter_dict_homographs(word_dict_h):
    # TODO delete an entry from dictionary, if not a homograph
    pass


def find_homographs(tokens):
    # TODO return a dictionary which holds homographs
    pass
