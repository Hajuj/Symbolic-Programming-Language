from unittest import TestCase

from src.hw04_text_search.text_vectors import TextDocument, DocumentCollection, SearchEngine


class DocumentCollectionTest(TestCase):
    def setUp(self):
        test_doc_list = [TextDocument(text_and_id[0], text_and_id[1]) for text_and_id in
                         [("the cat sat on a mat", "doc1"),
                          ("a rose is a rose", "doc2")]]
        self.small_collection = DocumentCollection.from_document_list(test_doc_list)

        # TODO: uncomment in case tests need access to whole document collection.
        # this_dir = os.path.dirname(os.path.abspath(__file__))
        # document_dir = os.path.join(this_dir, os.pardir, 'data/enron/enron1/ham/')
        # self.large_collection = DocumentCollection.from_dir(document_dir, ".txt")

    def test_unknown_word_cosine(self):
        """ Return 0 if cosine similarity is called for documents with only out-of-vocabulary words. """
        # Document that only contains words that never occurred in the document collection.
        query_doc = TextDocument(text="unknownwords", id=None)
        # Some document from collection.
        collection_doc = self.small_collection.docid_to_doc["doc1"]
        # Similarity should be zero (instead of undefined).
        self.assertEqual(self.small_collection.cosine_similarity(query_doc, collection_doc), 0.)


class TextDocumentTest(TestCase):
    # TODO: Unittests for TextDocument go here.
    def setUp(self):
        self.text_id1 = ("the nice boy ate a chocolate bar", "doc1")
        self.text_id2 = ("", "doc2")
        self.text_id3 = ("a dog is not a dog", "doc3")

    def test_constructor(self):
        doc1 = TextDocument(self.text_id1[0], self.text_id1[1])
        expected_dict1 = {"the": 1, "nice": 1, "boy": 1, "ate": 1, "a": 1, "chocolate": 1, "bar": 1}
        self.assertEqual(doc1.token_counts, expected_dict1)
        doc2 = TextDocument(self.text_id2[0], self.text_id2[1])
        expected_dict2 = {None}
        self.assertEqual(doc2.token_counts, expected_dict2)

    def test_from_file_method(self):
        doc1 = TextDocument.from_file("./hw04_text_search/test1.txt")
        token_set = set(doc1.token_counts.keys())
        expected_token_set = {'trump', 'will', 'not', 'be', 'the', 'u.s.', 'president',
                              "anymore", '.', "(", ")"}
        self.assertEqual(token_set, expected_token_set)

        doc2 = TextDocument.from_file("./hw04_text_search/test2.txt")
        self.assertEqual(doc2.token_counts["app"], 2)
        self.assertTrue("terminal" in doc2.token_counts)


class SearchEngineTest(TestCase):
    # TODO: Unittests for SearchEngine go here.
    def setUp(self):
        self.fun = SearchEngine(SearchEngine.collection)

        self.collection = DocumentCollection.from_dir("./hw04_text_search/enron", ".txt")
        self.search_engine = SearchEngine(self.collection)

    def test_ranked_documents(self):
        #edited from_dir() to search all subdirectories
        search_query = "cage ranch"
        results = (self.search_engine.ranked_documents(search_query))
        expected_doc_id = "./hw04_text_search/enron/enron1/ham/0066.1999-12-27.farmer.ham.txt"
        ids = []

        for res in results:
            ids.append(str(res[0].id))
        self.assertTrue(expected_doc_id in ids)

    def test_line_breaks(self):
        for snippet in self.fun.snippets("document", SearchEngine.doc_collection.docid_to_doc["doc1"]):
            self.assertTrue("\n" not in snippet)

    def test_query_multiple(self):
        for snippet in self.fun.snippets("document", SearchEngine.collection.docid_to_doc["doc1"]):
            self.string1 = [snippet]
        for snippet in self.fun.snippets("document document", SearchEngine.collection.docid_to_doc["doc1"]):
            self.string2 = [snippet]
        self.assertEqual(self.string1, self.string2)
