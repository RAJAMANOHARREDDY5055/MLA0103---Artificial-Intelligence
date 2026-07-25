%--------------------------
% Facts
%--------------------------

man(marcus).

pompeian(marcus).

ruler(caesar).

tried_to_assassinate(marcus, caesar).

%--------------------------
% Rules
%--------------------------

roman(X) :-
    pompeian(X).

person(X) :-
    man(X).

loyal_to(X, someone) :-
    person(X).

not_loyal_to(X, Y) :-
    person(X),
    ruler(Y),
    tried_to_assassinate(X, Y).

hates(X, caesar) :-
    roman(X),
    not_loyal_to(X, caesar).

loyal_to(X, caesar) :-
    roman(X),
    \+ hates(X, caesar).