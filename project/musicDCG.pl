% Measures
m4_4 --> w.
m3_4 --> dh.
m2_4 --> h.
m2_2 --> w.
m6_8 --> dh.
m9_8 --> w,e ; e,w ; dh,dq ; dq,dh.

% Wholes
w --> [w] ; [wr].
w --> h,h.
w --> dh,q ; q,dh.

% Dotted Halves
dh --> [dh] ; [dhr].
dh --> h,q ; q,h.
dh --> dq,dq.
dh --> e,h,e.

% Halves
h --> [h] ; [hr].
h --> q,q.
h --> dq,e ; e,dq.
h --> s,dq,s.
h --> de,q,s.

% Dotted Quarters
dq --> [dq] ; [dqr].
dq --> q,e ; e,q.
dq --> s,q,s.
dq --> de,de.

% Quarters
q --> [q] ; [qr].
q --> e,e.
q --> de,s ; s,de.

% Dotted Eighths
de --> [de] ; [der].
de --> e,s ; s,e.

% Eighths
e --> [e] ; [er].
e --> s,s.

% Sixteenths
s --> [s] ; [sr].
