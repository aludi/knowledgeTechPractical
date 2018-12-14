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

#todo: select more than 1 type of game?

#initiate a root and an instance of the class Gui
root = Tk()
GUI = gui.Gui(root)

#initialize prolog and the prolog interaction class
prolog = Prolog()
pI = PrologInteraction()

#getting the answers from the Gui
guiAnswers(pI)

# searching for other games with the complexity of game1:
pI.searchGameByAverageComplexity(pI.getAverageComplexity(GUI.getAllGames()), prolog)
# searching for games in list of type
pI.searchGameByType(prolog)
# searching for games in list of genre
#only for testing if genre selection works
pI.setGenre("adventure")
pI.searchGameByGenre(prolog)

pI.stringQuery(prolog)
pI.printSol()

