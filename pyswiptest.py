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
	prolog.consult("startingKB.pl")
	# game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)
	### to add: complexity, TYPE, budget, rec players, cooperative, vaste-groep (campaign games)), list-of-genres.


prolog = Prolog()
kb = load_knowledge_base()		#loading the knowledge base
gui = Gui


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

coop = input("cooperative? true/false\n")
print(coop)

camp = input("campaign? true/false\n")
print(camp)

minAge = input("what is the minimum age of the players?\n")
print("your min age is ", minAge)

stringQuery ='''
A is {},
 M = {},
  B = {},
   T = {}, 
   CO = {},
    CA = {},
    game(Name, MinP, MaxP, Time, Minage, Complexity, T, C, CO, CA, Listgenre),
     C < B,
      numPlay(A, MinP, MaxP), minimumAge(M, Minage)'''.format(numberOfPlayers, minAge, budget, typeGame, coop, camp)

y = prolog.query(stringQuery)

x= 0
for soln in y:
	print("you can play:", (soln["Name"]))
	x = 1
if x == 0:
	print("sorry, we couldn't find any games for you")	

