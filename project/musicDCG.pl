% Measures
m4_4 --> w.
m3_4 --> dh.
m2_4 --> h.

% Wholes
w --> [w] ; [wr].
w --> h,h.
w --> dh,q ; q,dh.

% Dotted Halves
dh --> [dh] ; [dhr].
dh --> h,q ; q,h.

% Halves
h --> [h] ; [hr].
h --> q,q.
h --> dq,e ; e,dq.

% Dotted Quarters
dq --> [dq] ; [dqr].
dq --> q,e ; e,q.

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
