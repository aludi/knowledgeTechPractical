from pyswip import Prolog

import tkinter as tk
from tkinter import *

from PrologInteraction import *

import gui

def guiAnswers(pI):
	pI.setNumPlay(GUI.getNumPlayers())		# setting number of players in pI
	pI.setGame1(GUI.getGame1())				# setting game 1 for extracting features
	pI.setGame2(GUI.getGame2())				# setting game 2 for extracting features
	pI.setGame3(GUI.getGame3())				# setting game 3 for extracting features
	pI.setBudget(GUI.getMaxPrice())			# setting max price of game
	pI.setType(GUI.getGameType())			# setting type of game (family, strategy, etc.)
	pI.setCoop(GUI.getCoop())				# setting if game is cooperative
	pI.setCamp(GUI.getCampaign())			# setting if game is campaign
	pI.setMinAge(GUI.getMinAge())			# setting min age for playing
	pI.setTime(GUI.getTime())
	pI.setAvComplexity(pI.getAverageComplexity(GUI.getAllGames()))	#setting average complexity
	pI.setTimeMatters(GUI.getTime())
	pI.setNumPlayersMatter(GUI.getNumPlayers())




#initiate a root and an instance of the class Gui
root = Tk()
root.wm_title("Board game recommendation")
GUI = gui.Gui(root, 0, [])

if GUI.getFinished():		
	#initialize prolog and the prolog interaction class
	prolog = Prolog()
	pI = PrologInteraction()

	#getting the answers from the Gui
	guiAnswers(pI)

	# searching for other games with the complexity of game1:
	playedGames = GUI.getAllGames()

	pI.getAverageComplexity(playedGames)

	# searching for games in list of type
	#pI.getAverageComplexity(GUI.getAllGames()) # initialize average complexity

	pI.stringQuery(prolog, "high")
	finalList = pI.selectPriority(playedGames)
	print(pI.getSelfY())

	root = Tk()
	root.wm_title("Board game recommendation")
	GUI = gui.Gui(root, 1, finalList)
