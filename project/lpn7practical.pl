% LPN! Ch. 7.4 - Practical Session

% PART 1: Keyboard Exercises
%  #1
s(Z):-  np(X),  vp(Y),  append(X,Y,Z).
np(Z):-  det(X),  n(Y),  append(X,Y,Z).
vp(Z):-  v(X),  np(Y),  append(X,Y,Z).
vp(Z):-  v(Z).
det([the]).
det([a]).
n([woman]).
n([man]).
v([shoots]).


%  #2
s(X,Z):-  np(X,Y),  vp(Y,Z).
np(X,Z):-  det(X,Y),  n(Y,Z).
vp(X,Z):-    v(X,Y),  np(Y,Z).
vp(X,Z):-    v(X,Z).
det([the|W],W).
det([a|W],W).
n([woman|W],W).
n([man|W],W).
v([shoots|W],W).


%  #3
s  -->  np,vp.
np  -->  det,n.
vp  -->  v,np.
vp  -->  v.
det  -->  [the].
det  -->  [a].
n  -->  [woman].
n  -->  [man].
v  -->  [shoots].



% PART 2: Writing DCGs
%  #1
s --> [].
s --> l,s.
l --> [a,a].


%  #2
s --> t.
s --> x,s,y.
x --> [a].
y --> [d].

t --> [].
t --> g,t,h.
g --> [b,b].
h --> [c,c].


%  #3
prop  -->  [p].
prop  -->  [q].
prop  -->  [r].

prop  --> [not],prop.
prop  --> ['('],prop,[and],prop,[')'].
prop  --> ['('],prop,[or],prop,[')'].
prop  --> ['('],prop,[implies],prop,[')'].


