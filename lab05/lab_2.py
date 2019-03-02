'''
Exercise 5.2 for Lab 5, CS 344
Based on network.py by kvlinden.
Implements a Bayesian network for a two-test cancer example.

@author: ljh27
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

cancerNet = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2}),
    ])


# a. P(Cancer | positive results on both tests)
print('P(Cancer | positive results on both tests):')
print('\t' + enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancerNet).show_approx())

# b. P(Cancer | a positive result on test 1, but a negative result on test 2)
print('\nP(Cancer | a positive result on test 1, but a negative result on test 2):')
print('\t' + enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancerNet).show_approx())
