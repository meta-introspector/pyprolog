window(main, -2, 2.0, 20, 72).
window(error, 15, 4.0, 20, 78).
customer('John Jones', boston, good_credit).
customer('Sally Smith', chicago, good_credit).
test(Y) :- Y is 5 + 2 * 3 - 1.
test2 :- Z is 6/2, write(Z).
/*test3 :- Q is 10.*/
dog(1).
whatdog :- dog(X), write(X).
%test4(D) :- Y is 1, dog(Y).