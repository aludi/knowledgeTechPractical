from pyswip import Prolog

#import Tkinter as tk
#from Tkinter import *

#or
#from Test import newtestvar
import tkinter as tk
from tkinter import *
import Gui



### LINK TO GITHUB REPO: https://github.com/aludi/knowledgeTechPractical


### Pick 3 games that you like (from our list) and 1 game that you don't -> complexity rating.
### Instapkosten, vaste groep of niet (0,1)? 
# we will help blabal
# game for yourself or game for other?
# 3 games yes, 1 game no, (or noob)
# easier or harder than mean?max?min? game selected?
# budget max?
# vaste groep of niet?
# cooperative vs non-cooperative vs doesn't matter (0,1)
# how many players?
# age of players?
# how much time do you want to spend learning the rules?/watching youtube?
# how long should it take?
# potential genres



def question1():
	print("I'm clicking stuff")
	
def load_knowledge_base():		#implementing knowledge base in separate function
	#               game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)
	prolog.assertz("game(spacecorp, 2, 4, 30, 12, science_fiction)")
	prolog.assertz("game(luna, 2, 4, 60, 12, fantasy)")
	prolog.assertz("game(betrayal_legacy, 2, 5, 45, 12, adventure)")
	prolog.assertz("game(madeup1, 2, 30, 45, 12, adventure)")
	prolog.assertz("game(madeup2, 2, 5, 5, 4, adventure)")
	prolog.assertz("game(madeup3, 1, 2, 10, 5, strategy)")
	prolog.assertz("game(madeup4, 2, 5, 5, 4, adventure)")
	prolog.assertz("game(madeup5, 1, 2, 10, 5, strategy)")
	
	## testing new predicate below
	prolog.assertz("game(madeup5, 1, 2, 10, 5, 5, family, 10, T, T, strategy)")
	### to add: complexity, TYPE, budget, rec players, cooperative, vaste-groep (campaign games)), list-of-genres.


def queryOld(numberOfPlayers, genre, minAge):		#querying based on 2 things
	return prolog.query(
	"A is {}, Z = {}, M is {}, game(X, B, C,_,N,Z), numPlay(A, B, C), minimumAge(M, N)."
	.format(numberOfPlayers, genre, minAge)) #inference rule
	
def queryNew(numberOfPlayers, genre, minAge):		#querying based on 2 things
	return prolog.query(
	"A is {}, Z = {}, M is {}, game(X, B, C,_,N,Z), numPlay(A, B, C), minimumAge(M, N)."
	.format(numberOfPlayers, genre, minAge)) #inference rule




prolog = Prolog()
kb = load_knowledge_base()		#loading the knowledge base
gui = Gui
#test = newtestvar


#rule for min/max
prolog.assertz("numPlay(A,MIN, MAX):- A >= MIN, A =< MAX")
# rule for min age
prolog.assertz("minimumAge(M, N):- N >= M")


	#game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)

#unsubtle way of selecting for 

numberOfPlayers = input("with how many players do you want to play?\n")
print("you want to play with ", numberOfPlayers, "players")

budget = input("what is your budget?\n")
print("your budget is ", budget, "euros")

typeGame = input("what is your game-type?\n")
print("your game-type is ", typeGame)

coop = input("cooperative? T/F\n")
print(coop)

camp = input("campaign?\n")
print(camp)

minAge = input("what is the minimum age of the players?\n")
print("your min age is ", minAge)

stringQuery ='''A is {},
 M = {},
  B = {},
   T = {}, 
   CO = {},
    CA = {},
    game(Name, MinP, MaxP, Rime, Minage, Complexity, T, C, CO, CA, Listgenre),
     C < B,
      numPlay(A, MinP, MaxP), minimumAge(M, Minage)'''.format(numberOfPlayers, minAge, budget, typeGame, coop, camp)

y = prolog.query(stringQuery)

for soln in y:
	print("you can play:", (soln["Name"]))
	

'''
prolog.query(

	"A is {},  game(Name, MinP, MaxP, Rime, Minage, Complexity, Type, Budget, CooperativeTF, CampaignTF, Listgenre), numPlay(A, MinP, MaxP),". numberOfPlayers

	game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)
	"A is {}, Z = {}, M is {}, game(X, B, C,_,N,Z), numPlay(A, B, C), minimumAge(M, N)."
	.format(numberOfPlayers, genre, minAge)) #inference rule

x= 0
for soln in queryOld(numberOfPlayers, genre, minAge):
	print("you can play:", (soln["X"]))
	x = 1
if x == 0:
	print("sorry, we couldn't find any games for you")

'''

## retracting facts?
## only asserting facts when gui prompts or something?

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
