% LPN! Ch. 7.3 - Exercises

% Exercise 7.1
%  Corresponding ordinary Prolog rules:
foo([choo|A], A).
foo(A, B) :-
    foo(A, C),
    foo(C, B).
bar(A, B) :-
    mar(A, C),
    zar(C, B).
s(A, B) :-
    foo(A, C),
    bar(C, D),
    wiggle(D, B).
mar(A, B) :-
    me(A, C),
    my(C, B).
zar(A, B) :-
    blar(A, C),
    car(C, B).
blar([a|A], A).
me([i|A], A).
wiggle([toot|A], A).
wiggle(A, B) :-
    wiggle(A, C),
    wiggle(C, B).
my([am|A], A).
car([train|A], A).

% First three responses to the query s(X,[]):
%  X = [choo, i, am, a, train, toot] ;
%  X = [choo, i, am, a, train, toot, toot] ;
%  X = [choo, i, am, a, train, toot, toot, toot]


% Exercise 7.2
s --> [a,b].
s --> l,s,r.
l --> [a].
r --> [b].


% Exercise 7.3
s --> [].
s --> l,s,r.
l --> [a].
r --> [b,b].

