'''
Exercise 5.1 for Lab 5, CS 344
Based on network.py by kvlinden.
Implements the Bayesian network shown in the text, Figure 14.2.

@author: ljh27
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burgNet = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])


# i. P(Alarm | burglary ∧ ¬earthquake)
# According to the table given in Figure 14.2, this should be 0.94
print('P(Alarm | burglary ∧ ¬earthquake):')
print('\t' + enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burgNet).show_approx())

# ii. P(John | burglary ∧ ¬earthquake)
# According to the example calculation we did in class, this should be True: 0.85, False: 0.15
print('\nP(John | burglary ∧ ¬earthquake):')
print('\t' + enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burgNet).show_approx())

# iii. P(Burglary | alarm)
# According to the example calculation we did in class, this should be True: 0.374, False: 0.6267
print('\nP(Burglary | alarm):')
print('\t' + enumeration_ask('Burglary', dict(Alarm=T), burgNet).show_approx())

# iv. P(Burglary | john ∧ mary)
# Compute P(Burglary | John and Mary both call).
print('\nP(Burglary | John and Mary both call):')
print('\tenumeration_ask: ' + enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burgNet).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print('\telimination_ask: ' + elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burgNet).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print('\tgibbs_ask: ' + gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burgNet).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.
