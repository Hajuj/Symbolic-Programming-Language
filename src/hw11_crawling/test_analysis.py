from unittest import TestCase
from hw11_crawling.analyze_article import *


class AnalysisTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "http://www.nytimes.com/2013/04/07/automobiles/autoreviews/hybrid-drivers-wanted.html?_r=0"
        cls.html = get_html(cls.url)
        cls.text = get_text(cls.html)
        cls.headline = get_headline(cls.html)
        cls.tokens_normalized = get_normalized_tokens(cls.text)
        cls.tagsDict = get_pos_dict(cls.tokens_normalized)

    def test_01_get_text(self):
        last_paragraph = self.text.split("\n")[-1]
        self.assertEqual(last_paragraph, "Advertisement")

    def test_02_get_headline(self):
        self.assertEqual(self.headline, "Hybrid Drivers Wanted")

    def test_03_get_normalized_tokens(self):
        self.assertEqual(self.tokens_normalized[:4], ['advertisement', 'supported', 'behind', 'wheel'])

    def test_04_pos_dict(self):
        print(self.tagsDict)
        self.assertEqual(self.tagsDict["driving"], {'NN', 'VBG'})
        self.assertEqual(len(self.tagsDict), 514)

    def test_05_filter_dict_homographs(self):
        filter_dict_homographs(self.tagsDict)
        self.assertEqual(len(self.tagsDict), 24)

    def test_06_homographs(self):
        homographs = find_homographs(self.tokens_normalized)
        self.assertTrue("light" in homographs)
        self.assertTrue("diesel" in homographs)
        self.assertTrue("pure" in homographs)
