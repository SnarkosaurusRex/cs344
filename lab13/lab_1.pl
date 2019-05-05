% --- LAB 13 ---
% Exercise 13.1

% a.i. - LPN! Exercise 3.2:
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

in(X,Y) :- directlyIn(X,Y).
in(X,Y) :- directlyIn(X,Z), in(Z,Y).


% a.ii. - LPN! Exercise 4.5:
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([G|Gn],[E|En]) :- tran(G,E), listtran(Gn,En).


% b.) Prolog implements modus ponens using rules in the form head:- body. If body is a stated fact or can be inferred from the knowledge base, Prolog infers that head is true.
%		example: Given the knowledge base
%			a.
%			b :- a.
%		then the query
%			b.
%		would return True.
