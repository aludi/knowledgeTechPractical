from pyswip import Prolog
prolog = Prolog()

prolog.assertz("father(michael,john)")
prolog.assertz("father(michael,gina)")
list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
for soln in prolog.query("father(X,Y)"):
    print(soln["X"], "is the father of", soln["Y"])
# michael is the father of john
# michael is the father of gina


#knowledge base:
prolog.assertz("game(spacecorp, 2, 4, 30, twaalf, science_fiction)")
prolog.assertz("game(luna, 2, 4, 60, twaalf, fantasy)")
prolog.assertz("game(betrayal_legacy, 2, 5, 45, twaalf, adventure)")
prolog.assertz("game(madeup1, 2, 30, 45, twaalf, adventure)")
prolog.assertz("game(madeup2, 2, 5, 5, vijf, adventure)")
prolog.assertz("game(madeup3, 1, 2, 10, vijf, strategy)")

#rule for min/max
prolog.assertz("numPlay(A,MIN, MAX):- A >= MIN, A =< MAX")

#list(prolog.query("A is 4, game(X, B, C,_,_,_), numPlay(A, B, C)"))

numberOfPlayers = input("with how many players do you want to play?\n")
print("you want to play with:", numberOfPlayers, "players\n")
for soln in prolog.query("A is {}, game(X, B, C,_,_,_), numPlay(A, B, C)".format(numberOfPlayers)):
	print("you can play:", (soln["X"]))


'''
/* queries: 
* to select a game where number of players is 5: A is 5, game(X, B, C,_,_,_), numPlay(A,B,C).
* to find the genre of the game luna: game(luna,_,_,_,_,X).
*
* Format of game.6: game(name, minNumPlayers, maxNumPlayers, minPlayTime, age, category)
*/


numPlay(A,MIN, MAX):- A >= MIN, A =< MAX.
game(spacecorp, 2, 4, 30, twaalf, science_fiction).
game(luna, 2, 4, 60, twaalf, fantasy).
game(betrayal_legacy, 2, 5, 45, twaalf, adventure).
game(madeup1, 2, 30, 45, twaalf, adventure).
game(madeup2, 2, 5, 5, vijf, adventure).
game(madeup3, 1, 2, 10, vijf, strategy).

'''
