import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from PrologInteraction import *

from tkinter_autocomplete import AutocompleteEntry


class Gui: 
	
	def __init__(self, master): 
		
		#dubble underscore encapsulates the variable, it can't be directly accessed from main.py
		prologThing = PrologInteraction()
		#dubble underscore encapsulates the variable, it can't be directly accessed from main.py
		self.__forSelf = True
		self.__numPlayers = 1
		self.__maxPrice = 10
		self.__gameType = "strategy"
		self.__Coop = "true"
		self.__Campaign = "true"
		self.__ListType = prologThing.getTypes() 		#getting types-lists (family, strategy) from prologInteraction
		self.__ListNames = prologThing.getNamesGamesInList() #getting all names of all games from prologInteraction
		
		
		#TkInter for interface : link for tutorial :  https://www.python-course.eu/tkinter_labels.php
		w = Label(master, font = "Times 16 bold", fg = "black", text = "Hello\n I will help you with selecting a boardgame!")
		pic = PhotoImage(file = "img/scaryOwl1.gif") #must always be a gif, thinter doesn't like other formats.
		w1 = Label(master, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Button(master, text="Exit", command= master.destroy).pack(side = "bottom")
		w.pack()
		
		
		#question 1 
		Label(master, text="Is the game for yourself or for someone else?").pack(anchor=tk.W)
		var1 = BooleanVar()
		var1.set(True)
		Radiobutton(master, text="For me", padx = 20, variable=var1, value=True).pack(anchor=tk.W)
		Radiobutton(master, text="For someone else", padx = 20, variable=var1, value=False).pack(anchor=tk.W)
		Button(master, text="Confirm Choice", command= lambda: self.save_person(master,var1)).pack(anchor=tk.W)	
		
		
		#TEMPORARY
		games = ("Small world", "Monopoly", "Colonisten van katan", "pandemic", "Agricola", "Wizard")
		def choseEntry(entry):
			print(entry)
		
		#question 2 previous games
		Label(master, text="Name three games you like").pack(anchor=tk.W)
		game1Entry = AutocompleteEntry(master)
		game1Entry.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >")
		game1Entry.pack(anchor=tk.W)
		Button(master, text="Confirm Choice", command= lambda: self.save_game1(master,game1Entry)).pack(anchor=tk.W)
		
		#question 2
		Label(master, text="What is the preferred number of players?").pack(anchor=tk.W) #make sure input is valid!
		num = Entry(master)
		num.pack(anchor=tk.W)
		Button(master, text="Confirm Choice", command= lambda: self.save_numPlayers(master,num)).pack(anchor=tk.W)
		
		#question 3
		Label(master, text="What is the maximum price you want to pay for the game? (in euros)").pack(anchor=tk.W)
		maxP = Entry(master)
		maxP.pack(anchor=tk.W)
		#if an impossible answer is given (max < min or price < 0), make a pop-up instead of going to next question
		Button(master, text="Confirm Choice", command= lambda: self.save_budget(master,maxP)).pack(anchor=tk.W)
			
		#question 4
		Label(master, text="What type of game do you want to play?").pack(anchor=tk.W)
		gen = StringVar()
		gen.set("family")
		for i in self.__ListType:		#loops through all game-types in database.
			Radiobutton(master, text=i, padx = 20, variable=gen, value=i).pack(anchor=tk.W)
		Button(master, text="Confirm Choice", command= lambda: self.save_type(master,gen)).pack(anchor=tk.W)
		
		#question 5
		Label(master, text="Do you want a cooperative game?").pack(anchor=tk.W)
		coop = StringVar()
		coop.set("true")
		Radiobutton(master, text="Yes", padx = 20, variable=coop, value="true").pack(anchor=tk.W)
		Radiobutton(master, text="No", padx = 20, variable=coop, value="false").pack(anchor=tk.W)
		Button(master, text="Confirm Choice", command= lambda: self.save_coop(master,coop)).pack(anchor=tk.W)
		
		#question 6
		Label(master, text="Do you want a game that has a campaign?").pack(anchor=tk.W)
		cam = StringVar()
		cam.set("true")
		Radiobutton(master, text="Yes", padx = 20, variable=cam, value="true").pack(anchor=tk.W)
		Radiobutton(master, text="No", padx = 20, variable=cam, value="false").pack(anchor=tk.W)
		Button(master, text="Confirm Choice", command= lambda: self.save_campaign(master,cam)).pack(anchor=tk.W) 
		
		
		master.mainloop()
		
		

			
	def save_person(self, master, var1):
		self.__forSelf = var1.get()
		master.update
	
	def save_game1(self, master, game):
		self.__game1 = game.text.get()
		master.update
		
	def save_numPlayers(self, master, num):
		self.__numPlayers = num.get()
		master.update	
		
	def save_budget(self, master, maxP):
		self.__maxPrice = maxP.get()
		master.update
		
	def save_type(self, master, gen):
		self.__gameType = gen.get()
		master.update
		
	def save_coop(self, master, coop):
		self.__Coop = coop.get()
		master.update
		
	def save_campaign(self, master, cam):
		self.__Campaign = cam.get()
		master.update
		
		
	def save_minAge():
		minAge = minA.get()
		
	def callback(*args):
		print("variable changed")
	
	
	
	# getters	
	def getPerson(self):
		return self.__forSelf	
	
	def getGame1(self):
		return self.__game1
		
	def getNumPlayers(self):
		return self.__numPlayers
		
	def getMaxPrice(self):
		return self.__maxPrice
		
	def getGameType(self):
		return self.__gameType
		
	def getCoop(self):
		return self.__Coop
		
	def getCampaign(self):
		return self.__Campaign
		
		#frame = Frame(master)
		#frame.pack()
		
		#self.printButton = Button(frame, text= "Print Message", command=self.printMessage)
		#self.printButton.pack(side=LEFT)
		
		#self.quitButton =  Button(frame, text= "Quit", command = frame.quit)
		#self.quitButton.pack(side=LEFT)
		
	#def printMessage(self): 
#print("wow, this actually worked")
