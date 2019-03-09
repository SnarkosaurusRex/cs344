"""
This module implements a Bayesian spam filter based on Paul Graham's "A Plan for Spam".
Part 1 of Homework 2 for CS 344

@author: ljh27
"""


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


def evaluate_msg(msg, probs):
    prod = 1
    comp_prod = 1
    for word in msg:
        if word in probs:
            prod *= probs[word]
            comp_prod *= (1 - probs[word])
        else:
            prod *= 0.4
            comp_prod *= 0.6
    spam_prob = prod / (prod + comp_prod)

    if spam_prob > 0.9:
        return ["SPAM", spam_prob]
    else:
        return ["Not spam", spam_prob]


#Test it out!
spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
ngood = len(ham_corpus)
nbad = len(spam_corpus)

good = parse_corpus(ham_corpus)
bad = parse_corpus(spam_corpus)
words = get_unique_words([ham_corpus, spam_corpus])
probs = create_probs_dict(words, good, bad, ngood, nbad)

print("good: " + str(good))
print("bad: " + str(bad))
print("\nprobs: ")
print(probs)


print("\n\n--- TESTS ---")
test_msg = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "Sam-I-am"]
test_result = evaluate_msg(test_msg, probs)
print(" Message: " + " ".join(test_msg))
print("\tResult: " + test_result[0] + " (Probability = " + str(test_result[1]) + ")")

test_msg2 = ["You", "can't", "have", "egg", "bacon", "spam", "and", "sausage", "without", "the", "spam"]
test_result2 = evaluate_msg(test_msg2, probs)
print("\n Message: " + " ".join(test_msg2))
print("\tResult: " + test_result2[0] + " (Probability = " + str(test_result2[1]) + ")")

test_msg3 = ["spam", "egg", "spam", "spam", "bacon", "and", "spam"]
test_result3 = evaluate_msg(test_msg3, probs)
print("\n Message: " + " ".join(test_msg3))
print("\tResult: " + test_result3[0] + " (Probability = " + str(test_result3[1]) + ")")
