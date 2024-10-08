from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math
from collections import Counter


def dot(dictA, dictB):
    return sum([dictA.get(tok) * dictB.get(tok, 0) for tok in dictA])


def normalized_tokens(text):
    return [token.lower() for token in word_tokenize(text)]


class TextDocument:
    def __init__(self, text, id=None, category=None):
        self.text = text
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id
        self.category = category

    @classmethod
    def from_file(cls, filename, category):
        with open(filename, 'r', encoding="ISO-8859-1") as myfile:
            text = myfile.read().strip()
        return cls(text, filename, category)


class DocumentCollection:
    def __init__(self, term_to_df, term_to_docids, docid_to_doc, doc_to_category):
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc
        # TextDocument to category
        self.doc_to_category = doc_to_category

    @classmethod
    def from_dir(cls, dir):
        files = [(os.path.join(root, name), os.path.relpath(root, dir)) for root, dirs, f in os.walk(dir, topdown=False)
                 for name in f]
        docs = [TextDocument.from_file(f, cat) for f, cat in files]
        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        doc_to_category = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            doc_to_category[doc] = doc.category
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc, doc_to_category)

    def tfidf(self, counts):
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N / self.term_to_df[tok]) for tok, tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, weightedA, weightedB):
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        return dotAB / (normA * normB)


class KNNClassifier:
    def __init__(self, n_neighbors=1):
        self.n_neighbors = n_neighbors
        self.doc_collection = None
        self.vectorsOfDoc_collection = None

    def fit(self, doc_collection):
        self.doc_collection = doc_collection
        self.vectorsOfDoc_collection = [(doc, self.doc_collection.tfidf(doc.token_counts))
                                        for doc in self.doc_collection.docid_to_doc.values()]

    def calculate_similarities(self, vecTestDoc, vectorsOfTrainDocs):
        # TODO calculate similarities between test and train documents and label them [(similarity, label),...]
        similarities = []

        for doc in vectorsOfTrainDocs:
            similarity = self.doc_collection.cosine_similarity(vecTestDoc, doc[1])
            label = doc[0].category
            similarities.append((similarity, label))

        return similarities

    def order_nearest_to_farthest(self, distances):
        # TODO order the labeled points from nearest to farthest
        sorted_distances = sorted(distances, key=lambda x: x[0], reverse=True)
        return sorted_distances

    def labels_k_closest(self, sorted_distances):
        # TODO find the labels for the k closest points
        result = []
        all = sorted_distances[0:self.n_neighbors]
        for (similarity, category) in all:
            result.append(category)
        return result

    def choose_one(self, labels):
        # TODO reduce k until you find a unique winner
        i = self.n_neighbors
        all_list = Counter(labels)
        most_list = all_list.most_common(i)
        while len(most_list) > 1 and most_list[1][1] == most_list[0][1]:
            if i > 2:
                i -= 1
            else:
                break
        return most_list[0][0]

    def classify(self, test_file):
        # TODO classify test document
        test_doc = TextDocument.from_file(test_file, 'unknowcat')
        fit = self.calculate_similarities(self.doc_collection.tfidf(test_doc.token_counts),
                                          self.vectorsOfDoc_collection)
        distance = self.labels_k_closest(self.order_nearest_to_farthest(fit))
        return self.choose_one(distance)

    def get_accuracy(self, gold, predicted):
        # TODO calculate accuracy
        correct = 0
        for x in range(len(gold)):
            if gold[x] == predicted[x]:
                correct += 1
        return (correct / float(len(gold))) * 100.0
