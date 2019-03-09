"""
Implements a Bayesian network for Figure 14.12a
Part 2 of Homework 2 for CS 344
(based on network.py by kvlinden)

@author: ljh27
"""

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py)
cloudyNet = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.10, F: 0.50}),
    ('Rain', 'Cloudy', {T: 0.80, F: 0.20}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.90, (F, T): 0.90, (F, F): 0.00})
    ])


# Part 2d
# i. P(Cloudy)
print('P(Cloudy):')
print('\t' + enumeration_ask('Cloudy', dict(), cloudyNet).show_approx())

# ii. P(Sprinkler | cloudy)
print('\nP(Sprinkler | cloudy):')
print('\t' + enumeration_ask('Sprinkler', dict(Cloudy=T), cloudyNet).show_approx())

# iii. P(Cloudy | sprinkler ∧ ¬rain)
print('\nP(Cloudy | sprinkler ^ ¬rain):')
print('\t' + enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), cloudyNet).show_approx())

# iv. P(WetGrass | cloudy ∧ sprinkler ∧ rain)
print('\nP(WetGrass | cloudy ∧ sprinkler ∧ rain):')
print('\t' + enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), cloudyNet).show_approx())

# v. P(Cloudy | ¬WetGrass)
print('\nP(Cloudy | ¬WetGrass):')
print('\t' + enumeration_ask('Cloudy', dict(WetGrass=F), cloudyNet).show_approx())
