'''
Lab 4: Exercise 4.1
Built off of kvlinden's joint.py

@author: ljh27
'''

from tools.aima.probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print('P(Cavity|Toothache):')
print(PC.show_approx())


# Exercise 4.1 b - Compute P(Cavity|catch)
'''Computed by hand:
    P(Cavity|catch) = P(Cavity^catch)/P(catch)
                    = (0.108 + 0.072)/(0.108 + 0.016 + 0.072 + 0.144)
                    = 0.18/0.34
                    ≈ 0.5294
'''
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print('\nP(Cavity|catch):')
print(PC.show_approx())


# Exercise 4.1 c
P = JointProbDist(['Coin1', 'Coin2'])
H, T = True, False  #Heads (H) corresponds to True, Tales (T) corresponds to False
P[H, H] = 0.25; P[H, T] = 0.25
P[T, T] = 0.25; P[T, H] = 0.25

# Compute P(Coin2|coin1=heads)
PC = enumerate_joint_ask('Coin2', {'Coin1': H}, P)
print('\n\nP(Coin2|coin1=heads):')
print(PC.show_approx())


# Yes, this answer confirms that the two coin flips are independent events
