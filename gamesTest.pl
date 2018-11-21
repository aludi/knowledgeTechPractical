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


newgame(nieuw, numPlay(A, B, C)).
