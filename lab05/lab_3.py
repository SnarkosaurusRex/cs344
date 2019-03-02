'''
Exercise 5.3 for Lab 5, CS 344
Based on network.py by kvlinden.
Implements a Bayesian network for a two-cause happiness example.

@author: ljh27
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

happyNet = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])


# a.i. P(Raise | sunny)
# Sunny and Raise are (conditionally) independent, so they don't directly influence each other.
# Thus, P(Raise | sunny) = P(Raise) = False: 0.99, True: 0.01
print('P(Raise | sunny):')
print('\t' + enumeration_ask('Raise', dict(Sunny=T), happyNet).show_approx())

# a.ii. P(Raise | happy ∧ sunny)
print('\nP(Raise | happy ∧ sunny):')
print('\t' + enumeration_ask('Raise', dict(Happy=T, Sunny=T), happyNet).show_approx())


# b.i. P(Raise | happy)
print('\nP(Raise | happy):')
print('\t' + enumeration_ask('Raise', dict(Happy=T), happyNet).show_approx())

# b.ii. P(Raise | happy ∧ ¬sunny)
print('\nP(Raise | happy ∧ ¬sunny):')
print('\t' + enumeration_ask('Raise', dict(Happy=T, Sunny=F), happyNet).show_approx())
