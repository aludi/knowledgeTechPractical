from pyswip import Prolog

import tkinter as tk
from tkinter import *

from PrologInteraction import *

import guiTutorial as gui

def guiAnswers(pI):
	pI.setNumPlay(GUI.getNumPlayers())		# setting number of players in pI
	pI.setGame1(GUI.getGame1())				# setting game 1 for extracting features
	pI.setGame2(GUI.getGame2())				# setting game 2 for extracting features
	pI.setGame3(GUI.getGame3())				# setting game 3 for extracting features
	pI.setBudget(GUI.getMaxPrice())			# setting max price of game
	pI.setType(GUI.getGameType())			# setting type of game (family, strategy, etc.)
	pI.setCoop(GUI.getCoop())				# setting if game is cooperative
	pI.setCamp(GUI.getCampaign())			# setting if game is campaign
	pI.setMinAge("0")						# setting min age for playing

#TODO:
# lower priority (first query): campaign, leeftijd, duration, budget (sliders?), 
# complexity (base < 2.5 or basis of three games), recc. players, type (max 3), cooperate.

## higher priority (second query): campaign, leeftijd, duration, budget
# complexity (larger range), numPlayers range, cooperate.

# TODO TO IMPLEMENT

# 1) print list of final genres in GUI
# 2) get high/low priority queries in order
# 3) change gui to reflect questions
# 4) pop-ups on GUI for explanation

# QUESTIONS
# links/images in final GUI frame?


#initiate a root and an instance of the class Gui
root = Tk()
GUI = gui.Gui(root, 0, [])

#initialize prolog and the prolog interaction class
prolog = Prolog()
pI = PrologInteraction()

#getting the answers from the Gui
guiAnswers(pI)


# searching for other games with the complexity of game1:
pI.searchGameByAverageComplexity(pI.getAverageComplexity(GUI.getAllGames()), prolog)
# searching for games in list of type

pI.stringQuery(prolog)
finalList = pI.printSol()
print(pI.getSelfY())

root = Tk()
GUI = gui.Gui(root, 1, finalList)
#GUI.printResults(pI.getSelfY())
#GUI.setFinalGames(pI.getSelfY())
