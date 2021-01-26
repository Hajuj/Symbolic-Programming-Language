from nltk.corpus import wordnet as wn
from itertools import combinations
from collections import Counter


def leave_odd_man_out(words):
    # TODO find the odd man in the list of words: use get_similarity_scores() method
    combinations(words, 2)
    counter = Counter(words)
    res = [(x, y) for x in counter for y in counter if x is not y]
    sim_score = get_similarity_scores(res)
    return min(sim_score, key=lambda x: x[1])[0].split("-")[1]


def get_similarity_scores(pairs):
    # TODO 1. iterate over all combinations of synsets formed by the synsets of the words in the word pair
    # TODO 2. determine the maximum similarity score
    # TODO 3. save max_line in results in form ("pair1-pair2", similarity_value) e.g.('car-automobile', 1.0)
    # TODO 4. return results in order of decreasing similarity
    results = []
    for pair in pairs:
        max_score = 0.0
        max_line = ()  # should look like "('food-fruit', 0.1)"
        syn1 = wn.synsets(pair[0])
        syn2 = wn.synsets(pair[1])
        for synset1 in syn1:
            for synset2 in syn2:
                sim_score = synset1.path_similarity(synset2)
                if sim_score is not None and sim_score > max_score:
                    max_score = sim_score
                    max_line = (pair[0] + "-" + pair[1], max_score)
        results.append(max_line)
    return results
