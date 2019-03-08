"""
spamFilter.py implements a Bayesian spam filter based on Paul Graham's A Plan for Spam.
Part 1 of Homework 2 for CS 344

@author: ljh27
"""

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask


def parse_corpus(corpus):
    corpus_dict = {}
    for message in corpus:
        for word in message:
            #force lowercase
            word = word.lower()

            #if the word is already in the dict, increment its count by 1
            if word in corpus_dict:
                corpus_dict[word] += 1

            #otherwise, add the word to the dict and set its count to 1
            else:
                corpus_dict[word] = 1

    return corpus_dict


def get_unique_words(corpus_list):
    unique_words = []
    for corpus in corpus_list:
        for message in corpus:
            for word in message:
                word = word.lower()
                if word not in unique_words:
                    unique_words.append(word)
    return unique_words


def create_probs_dict(words, good, bad, ngood, nbad):
    probs_dict = {}
    for word in words:
        if word in good:
            g = 2 * good[word]
        else:
            g = 0
        if word in bad:
            b = bad[word]
        else:
            b = 0

        #use a minimum count threshold of 1
        if g+b > 1:
            probs_dict[word] = max(0.01, min(0.99, min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))))
        else:
            probs_dict[word] = 0

    return probs_dict


#Set up some test data
spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
ngood = len(ham_corpus)
nbad = len(spam_corpus)

good = parse_corpus(ham_corpus)
bad = parse_corpus(spam_corpus)
words = get_unique_words([ham_corpus, spam_corpus])
probs = create_probs_dict(words, good, bad, ngood, nbad)

print('good: ')
print(good)
print('\nbad: ')
print(bad)
print('\nUnique words: ')
print(words)
print('\nprobs: ')
print(probs)


# courses = ['cs108', 'cs112', 'cs212', 'cs214', 'cs232', 'cs262', 'cs342']
# faculty = ['adams', 'plantinga', 'bailey', 'schuurman']
# classtimes = ['mwf0900', 'mwf1030', 'mwf1130', 'mwf1230']
# classrooms = ['nh253', 'sb382']
# slots = create_timeroom_slots(classtimes, classrooms)
# domains = create_domains(courses, assignments, slots)
# neighbors = create_nonreflexive_neighbors(courses)

#Run it!
# solution = min_conflicts(CSP(courses, domains, neighbors, schedule_constraint))
#
# print('Variables: ' + str(courses))
# print('Domains:')
# for d in domains:
#     print("\t{0}: {1}".format(d, domains[d]))
# print('Neighbors (non-reflexive):')
# for n in neighbors:
#     print("\t{0}: {1}".format(n, neighbors[n]))
# print('Solution:')
# for s in solution:
#     print("\t{0}: {1}".format(s, solution[s]))
# # print(solution)
