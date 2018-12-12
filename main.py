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
prologThing = PrologInteraction()


#hard-coded test of prologinteraction class
game1 = "madeup6"
prologThing.getAllProperties(game1)
game2 = "madeup5"
game3 = "madeup6"
listGame = [game1, game2, game3]
val = prologThing.getAverageComplexity(listGame)


# returns a list of all games in the knowledge-base
listNameGames = prologThing.getNamesGamesInList()

# returns a list of all types of games in the knowledge-base
listTypeGames = prologThing.getTypes()

# finds all games with a certain complexity
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

