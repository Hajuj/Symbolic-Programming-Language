import math
import os
from collections import defaultdict

from nltk import FreqDist, word_tokenize


def dot(dictA, dictB):
    """Returns the dot-product of the values of two dictionaries which are
    given in the form of vectors. The product can be calculated depending on the
    keys that the dictionaries have.

    --- dot-product of two non-empty vectors ---
    >>> dot({"rajna":1, "shady": 1, "hazhuzh":1, "habibiz":1, "group":1}, {"group":1, "habibiz":1})
    2

    >>> dot({1:4, 2:2, 3:0}, {1:6, 2:9, 3:6})
    42

    --- product of two null(empty) vectors---
    >>> dot({},{})
    0
        """
    return sum([dictA.get(tok) * dictB.get(tok, 0) for tok in dictA])


def normalized_tokens(text):
    """Returns a list of lowercase tokens of the given text
    --- test ---
    >>> normalized_tokens("He asked if he was allowed to have a break before completing the next task")
    ['he', 'asked', 'if', 'he', 'was', 'allowed', 'to', 'have', 'a', 'break', 'before', 'completing', 'the', 'next', 'task']
    >>> normalized_tokens("")
    []
    """
    return [token.lower() for token in word_tokenize(text)]


# TODO: Docstring documentation for all member functions (including constructors) Ex.3.2
class TextDocument:
    """ this is a class that will represent the Text Document

    Attributes
    ---------
    text: string -> the text for the TextDocument-Object
    id : string -> beliebige ID für den TextDocument-Object

    Methods and functions
    ---------------------
    from_file(cls, filename): a method that creates a TextDocument object from a file

    """

    def __init__(self, text, id=None):  #Dict should be {None} if text is empty
        """ Here will be implemented the constructor for the TextDocument class.
      There will also be stored a dictionary with the frequency of the tokens for the text (self.token_counts)
      :param: text: string -> the text for the TextDocument-Object
      :param: id : string -> beliebige ID für den TextDocument-Object

          """
        self.text = text

        if text == "":
            self.token_counts = {None}
        else:
            self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id

    @classmethod
    def from_file(cls, filename): #surrounds each word with ()
        """ Creates a TextDocument object from a file by first opening the textfile
        in read only mode, removing the whitespace characters and then calling the
        constructor with the given text and ID attributes

        :param: filename -> gives information about the path of the file that will be imported


        """
        with open(filename, 'r') as myfile:
            text = myfile.read().strip().split()

            new_text = ""
            for word in text:
                new_text += "(" + word + ")"

        return cls(new_text, filename)


# TODO: Docstring documentation for all member functions (including constructors) Ex.3.2
class DocumentCollection:
    """this is a class that will represent the collection of certain
    data from different documents

    Methods and functions
    ---------------------
    """

    def __init__(self, term_to_df, term_to_docids, docid_to_doc):
        """
        the class constructor will be implemented here which helps
        collecting and mapping certain useful information.

        :param term_to_df: a dictionary that maps terms from documents to the amount of documents they appear in
        :param term_to_docids: a dictionary that maps each term to a set of all documents they appear in
        :param docid_to_doc: a dictionary that maps document id's to TextDocuments
        """
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc

    @classmethod
    def from_dir(cls, dir, file_suffix):
        """
        this method collects document files from a specific folder
        and uses them to create a DocumentCollection object.
        :param dir: the path where document files are stored
        :param file_suffix: the file suffix of the document files
        :return:
        """
        files = [(dir + "/" + f) for f in os.listdir(dir) if f.endswith(file_suffix)]
        docs = [TextDocument.from_file(f) for f in files]
        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        """
        a method that creates a DocumentCollection Object from a list of documents
        :param docs: the list of documents that are about to be imported
        :return:
        """
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc)

    def docs_with_all_tokens(self, tokens):
        """
        Searches a DocumentCollection for documents that contain a certain set of tokens from a query
        First it creates a (nested) list for each token from the query with the document ID's for the documents
        they appear in, then uses intersection to find only the IDs for the documents that all tokens appear in.
        :param tokens: list of tokens
        :return: returns docids for the appeared documents
        """
        docids_for_each_token = [self.term_to_docids[token] for token in tokens]
        docids = set.intersection(*docids_for_each_token)
        return [self.docid_to_doc[id] for id in docids]

    def tfidf(self, counts):
        """
        The intention of this method is to return the "term frequency–inverse document frequency" vector
        for the DocumentCollection.
        Creates a dictionary representing a Vector that maps Tokens to their TF-IDF value (a weighting factor used to
        reflect the importance of a term). The returned vector contains only those values that also appear in "counts"
        :param counts: dictionary used to reduce vector
        :return:
        """
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N / self.term_to_df[tok]) for tok, tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, docA, docB):
        """
        returns the cosine similarity of two documents from a DocumentCollection
        depending on the angle between the TF-IDF vectors of two Documents.
        :param docA: the first document to be compared
        :param docB: the second document to be compared
        :return:
        """
        weightedA = self.tfidf(docA.token_counts)
        weightedB = self.tfidf(docB.token_counts)
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        if (normA * normB) == 0:
            return 0
        else:
            return dotAB / (normA * normB)


# TODO: Docstring documentation for all member functions (including constructors) Ex.3.2
class SearchEngine:
    def __init__(self, doc_collection):
        """
        this is a constructor for the SearchEngine class, which creates an instance of the class for a DocumentCollection
        :param doc_collection: the parameter of the DocumentCollection on which the SearchEngine should operate on
        """
        self.doc_collection = doc_collection

    def ranked_documents(self, query):
        """
        Ranks by cosine similarity a list of documents to a search query in a descending order
        :param query: a tokens string list for the search
        :return:
        """
        query_doc = TextDocument(query)
        query_tokens = query_doc.token_counts.keys()
        docs = self.doc_collection.docs_with_all_tokens(query_tokens)
        docs_sims = [(doc, self.doc_collection.cosine_similarity(query_doc, doc)) for doc in docs]
        return sorted(docs_sims, key=lambda x: -x[1])

    def snippets(self, query, document, window=50):
        """
        searches a DocumentCollection for text-snippets containing tokens from a query
        :param query: tokens string for the search
        :param document: the document the text-snippets should be extracted from
        :param window: the number of Characters before and after the tokens found in the document for the text-snippet
        :return:
        """
        tokens = normalized_tokens(query)
        text = document.text
        for token in tokens:
            start = text.lower().find(token.lower())
            if -1 == start:
                continue
            end = start + len(token)
            left = "..." + text[start - window:start]
            middle = "[" + text[start: end] + "]"
            right = text[end:end + window] + "..."
            yield left + middle + right
