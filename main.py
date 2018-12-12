from pyswip import Prolog

import tkinter as tk
from tkinter import *

from PrologInteraction import *

import guiTutorial as gui


#initiate a root and an instance of the class Gui
root = Tk()
GUI = gui.Gui(root)


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

	
def load_knowledge_base():		#implementing knowledge base in separate function
	prolog.consult("startingKB.pl")
	# game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)
	### to add: complexity, TYPE, budget, rec players, cooperative, vaste-groep (campaign games)), list-of-genres.


prolog = Prolog()
#kb = load_knowledge_base()		#loading the knowledge base
prologThing = PrologInteraction()


#hard-coded test of prologinteraction class
game1 = "madeup6"
prologThing.getAllProperties(game1)
game2 = "madeup5"
game3 = "madeup6"
listGame = [game1, game2, game3]
val = prologThing.getAverageComplexity(listGame)
print(val)
prologThing.searchGameByAverageComplexity(val, prolog)

#getting the answers from the Gui
prologThing.setNumPlay(GUI.getNumPlayers())
prologThing.setGame1(GUI.getGame1())
prologThing.setBudget(GUI.getMaxPrice())
prologThing.setType(GUI.getGameType())
prologThing.setCoop(GUI.getCoop())
prologThing.setCamp(GUI.getCampaign())
prologThing.setMinAge("0")

prologThing.stringQuery(prolog)
prologThing.printSol()



#rule for min/max
#prolog.assertz("numPlay(A,MIN, MAX):- A >= MIN, A =< MAX")
# rule for min age
#prolog.assertz("minimumAge(M, N):- N >= M")


#game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)

#unsubtle way of selecting for 
'''
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
'''
'''
stringQuery =''''''
A is {},
 M = {},
  B = {},
   T = {}, 
   CO = {},
    CA = {},
    game(Name, MinP, MaxP, Time, Minage, Complexity, T, C, CO, CA, Listgenre),
     C < B,
      numPlay(A, MinP, MaxP), minimumAge(M, Minage)''''''.format(numberOfPlayers, minAge, budget, typeGame, coop, camp)
y = prolog.query(stringQuery)
x= 0
for soln in y:
	print("you can play:", (soln["Name"]))
	x = 1
if x == 0:
	print("sorry, we couldn't find any games for you")	'''
