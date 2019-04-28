% Exercise 12.1
% Part a

% i.1.) killer is a property of the name butch (zed)
killer(butch).

% i.2.) married is a property of mia and marsellus (fact)
married(mia, marsellus).

% i.3.) dead is a property of zed (fact)
dead(zed).

% i.4.) This one needs to be a rule because it has a condition and a result. Giving Mia a foot massage is the condition, so that's the body of the rule. Marsellus killing somebody is the effect, so that's the head of the rule. A variable (X) is used for the argument because it could be anybody.
marsellusKills(X):- givesMiaFootMassage(X).

% i.5.) Being a good dancer is the condition, so that's the body of the rule. Being loved by Mia is the effect, so that's the head of the rule. A variable (X) is used for the argument because it could be anybody.
miaLoves(X):- isGoodDancer(X).

% i.6.) This one has two possible conditions and needs an "or", which is represented by a semicolon. The two conditions are being nutritious and being tasty, so that's the body of the rule. Being eaten by Jules is the effect, so that's the head of the rule. A variable (X) is used for the argument because it could be anything.
julesEats(X):- isNutritious(X); isTasty(X).

% ii.1.) yes - this is an expicitly stated fact in the given knowledge base
% ii.2.) no - the knowledge base has no information about a witch property
% ii.3.) no - the knowledge base has no information about hermione
% ii.4.) no - the knowledge base has no information about a witch property or hermione
% ii.5.) yes - the knowledge base explicitly states that harry has a wand, and prolog can infer that harry has a broom from the stated fact that harry is a quidditch player, and since prolog can chain together uses of modus ponens it can thus also infer that harry is a wizard because harry has a broom and harry has a wand
% ii.6.) Y = ron - the first item in the knowledge base states that ron is a wizard, so that is the first value that prolog unifies with Y (if a ; were added, prolog would then return Y = harry as well)
% ii.7.) no - there are no possible unifications


% Part b
% Prolog implements modus ponens using rules in the form head:- body. If body is a stated fact or can be inferred from the knowledge base, Prolog infers that head is true. For instance, if the knowledge base includes "listens2Music(mia)." and "playsAirGuitar(mia):- listens2Music(mia).", then Prolog would use modus ponens to infer that playsAirGuitar(mia) is true.


% Part c
% Horn clauses are able to use variables, but propositional logic cannot. Propositional logic might, however, tend to make more visual sense to a reader.


% Part d
% Prolog supports this distinction in that the facts and rules used in knowledge bases would be the TELL operation, and queries would be the ASK operation.
