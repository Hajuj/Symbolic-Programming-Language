import string
import numpy as np
import random

class Reader:

    def __init__(self, path):
        self.path = path
        self.punctuation = set(string.punctuation)
        self.courses = self.get_lines()
        self.vocabulary = self.get_vocabulary()
        self.vector_spaced_data = self.data_to_vectorspace()

    def get_lines(self):
        lines = []
        with open(self.path, "r") as f:
            line = f.readline()
            while line != "":
                lines.append(line.strip())
                line = f.readline()

        return lines

    def normalize_word(self,word):
        word.translate(None, string.punctuation)
        return word.lower()


    def get_vocabulary(self):
        wordsInFile = [self.normalize_word(x) for x in self.get_lines()]
        vocabulary = set()
        for elem in wordsInFile:
            vocabulary = vocabulary.union(elem.split(' '))
        return sorted(vocabulary)

    def vectorspaced(self,course):
        vek = [(x in self.normalize_word(course).split(' ')) for x in self.vocabulary]
        return list(map(int,vek))

    def data_to_vectorspace(self):
        return [self.vectorspaced(course) for course in self.courses if course]


class Kmeans:
    """performs k-means clustering"""

    def __init__(self, k):
        self.k = k
        self.means = None

    def distance(self, x,y):
        sum = 0
        for i in range(len(x)):
            sum += (x[i] - y[i])**2
        return np.sqrt(sum)

    def classify(self,input):
        return min(range(self.k), key=lambda i: self.distance(input, self.means[i]))

    def vector_mean(self,vectors):
        output = []
        for i in zip(*vectors):
            output = [*output, np.mean(i, axis=None)]
        return output

    def train(self, inputs):
        # choose k random points as the initial means
        self.means = random.sample(inputs, self.k)#step 1

        #uncomment the following line and use the given means for the unittest
        self.means = [inputs[32], inputs[67], inputs[46]]

        assignments = None
        iter = 0
        while iter != 100:
            # find new assignments
            assignments = list(map(self.classify, inputs))

            # compute new means based on the new assignments
            for i in range(self.k):
                # find all the points assigned to cluster i
                i_points = [p for p, a in zip(inputs,assignments) if a == i]
                if i_points:
                    # make sure i_points is not empty so don't divide by 0
                    self.means[i] = self.vector_mean(i_points)
            iter += 1
