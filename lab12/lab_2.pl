% Exercise 12.2
% Part a

% i.1.) unifies

% i.2.) does not unify

% i.8.) unifies (X = bread)

% i.9.) unifies (X = sausage, Y = bread)

% i.14.) does not unify


% ii.1.) unsatisfied - house_elf is a predicate, not a constant

% ii.2.) unsatisfied - the knowledge base has no information about harry

% ii.3.) unsatisfied - wizard isn't a constant

% ii.4.) satisfied - the knowledge base explicitly states that 'McGonagall' is a witch, so by instantiating X = 'McGonagall' in the rule magic(X):- witch(X). it can infer that 'McGonagall' is indeed magic

% ii.5.) satisfied - the query uses Hermione with a capital H, making it a variable, which means it could be instantiated to 'McGonagall', which would be satisfied as explained in the previous question 


% Part b
% Presumably it would have to use some flavor of unification (or something like it, at least) in order to recognize which rule(s) could be applied (i.e. given A, it would have to unify A with parts of rules to figure out which rule(s) involved an A)


% Part c
% Yes, Prolog inferencing must use resolution to evaluate what values are possible for a variable (i.e. to figure out how to respond to a query)
