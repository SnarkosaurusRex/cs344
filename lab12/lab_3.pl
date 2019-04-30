% Prolog program based on Monty Python's "Burn the witch" scene

% KNOWLEDGE BASE:
floatsInWater(wood).
floatsInWater(duck).
weighsSameAsDuck(woman).
burn(wood).
burn(X):- witch(X).
witch(X):- wood(X).
wood(X):- floatsInWater(X).
floatsInWater(X):- weighsSameAsDuck(X).

% QUERY:
?- witch(woman).
