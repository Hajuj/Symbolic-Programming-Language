from unittest import TestCase

from hw11_crawling.pos_match import Sentences, PosExpr, find

report = "data/hydrogenics_report.txt"


class SentenceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = report

    def test_01_from_file(self):
        s = Sentences.from_file(self.path)
        tokens = [t for sent in s for t in sent]
        self.assertIn(('Selling', 'VBG'), tokens)
        self.assertIn(('Toronto', 'NNP'), tokens)


class PosExprTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sentences = Sentences.from_file(report)

    def test_02_from_string(self):
        m = PosExpr.from_string("NN VB NN")
        self.assertIn("NN", m.expressions)
        self.assertIn("VB", m.expressions)

    def test_03_match_expr(self):
        self.assertTrue(PosExpr.match_expr("*", "NN"))
        self.assertTrue(PosExpr.match_expr("*", "VB"))
        self.assertTrue(PosExpr.match_expr("NN", "NN"))
        self.assertTrue(PosExpr.match_expr("NN*", "NNPS"))
        self.assertFalse(PosExpr.match_expr("NN", "VB"))
        self.assertFalse(PosExpr.match_expr("NN*", "VBS"))

    def test_04_matches(self):
        def all_matches(expr):
            return [m for s in self.sentences for m in PosExpr.from_string(expr).matches(s)]
        self.assertIn([("Toronto", "NNP")], all_matches("NNP"))
        self.assertIn([("prior", "JJ"), ("year", "NN")], all_matches("JJ NN"))
        self.assertIn([("venture", "NN"), ("in", "IN"), ("Toronto", "NNP")], all_matches("NN IN NN*"))

    def test_05_find(self):
        self.assertIn("prior year", find(self.sentences, "JJ NN"))
        self.assertIn("$ 13.7 million", find(self.sentences, "$ CD CD"))
