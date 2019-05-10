% LPN! Ch. 7.4 - Practical Session

% Writing DCGs:
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


