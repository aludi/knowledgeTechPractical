import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from PrologInteraction import *

from tkinter_autocomplete import AutocompleteEntry


class Gui: 
	
	def __init__(self, master): 
		
		def raise_frame(frame):
			frame.tkraise()
			
		f0 = Frame(master)
		f1 = Frame(master)
		f2 = AutocompleteEntry(master)
		f3 = Frame(master)
		f4 = Frame(master)
		f5 = Frame(master)
		f6 = Frame(master)
		f7 = Frame(master)
		
		for frame in (f0, f1, f2, f3, f4, f5, f6, f7):
		    frame.grid(row=0, column=0, sticky='news')
		
		#dubble underscore encapsulates the variable, it can't be directly accessed from main.py
		prologThing = PrologInteraction()
		self.__forSelf = True
		self.__numPlayers = 1
		self.__maxPrice = 10
		self.__gameType = "strategy"
		self.__Coop = "true"
		self.__Campaign = "true"
		self.__ListType = prologThing.getTypesForGUI() 		#getting types-lists (family, strategy) from prologInteraction
		self.__ListNames = prologThing.getNamesGamesForGUI() #getting all names of all games from prologInteraction
		self.__ListGenres = prologThing.getGenresForGUI()
		self.__game1 = "some"
		self.__game2 = "some"
		self.__game3 = "some"
		
		
		
		#TkInter for interface : link for tutorial :  https://www.python-course.eu/tkinter_labels.php
		w = Label(f0, font = "Times 16 bold", fg = "black", text = "Hello\n I will help you with selecting a boardgame!")
		pic = PhotoImage(file = "img/scaryOwl1.gif") #must always be a gif, thinter doesn't like other formats.
		w1 = Label(f0, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Button(f0, text="Exit", command= master.destroy).pack(side = "bottom")
		Button(f0, text="Start", command= lambda: raise_frame(f1)).pack(side = "bottom")
		w.pack()
		
		
		#question 1 
		Label(f1, text="Is the game for yourself or for someone else?").pack(anchor=tk.W)
		var1 = BooleanVar()
		var1.set(True)
		Radiobutton(f1, text="For me", padx = 20, variable=var1, value=True).pack(anchor=tk.W)
		Radiobutton(f1, text="For someone else", padx = 20, variable=var1, value=False).pack(anchor=tk.W)
		Button(f1, text="Next", command= lambda: self.save_person(master,var1,f2)).pack(anchor=tk.W)	
		
		
		#TEMPORARY
		games = ("Small world", "Monopoly", "Colonisten van Catan", "pandemic", "Agricola", "Wizard")
		def choseEntry(entry):
			print(entry)
		
		#question 2 previous games
		Label(f2, text="Name three games you like").grid()
		#game1Entry = AutocompleteEntry(master)
		game1Entry = f2.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >")	#changed to listNames
		#game1Entry.grid()
		
		#game2Entry = AutocompleteEntry(master)
		game2Entry = f2.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >")	#changed to listNames
		#game2Entry.grid()
		
		#game3Entry = AutocompleteEntry(master)
		game3Entry = f2.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >")	#changed to listNames
		#game3Entry.grid()
		Button(f2, text="Next", command= lambda: self.save_games(master,game1Entry, game2Entry, game3Entry, f3)).grid()
		
		#question 3
		Label(f3, text="What is the preferred number of players?").pack(anchor=tk.W) #make sure input is valid!
		num = Entry(f3)
		num.pack(anchor=tk.W)
		Button(f3, text="Next", command= lambda: self.save_numPlayers(master,num,f4)).pack(anchor=tk.W)
		
		#question 4
		Label(f4, text="What is the maximum price you want to pay for the game? (in euros)").pack(anchor=tk.W)
		maxP = Entry(f4)
		maxP.pack(anchor=tk.W)
		#if an impossible answer is given (max < min or price < 0), make a pop-up instead of going to next question
		Button(f4, text="Next", command= lambda: self.save_budget(master,maxP,f5)).pack(anchor=tk.W)
			
		#question 5
		Label(f5, text="What type of game do you want to play?").pack(anchor=tk.W)
		gen = StringVar()
		gen.set("family")
		for i in self.__ListType:		#loops through all game-types in database.
			Radiobutton(f5, text=i, padx = 20, variable=gen, value=i).pack(anchor=tk.W)
		Button(f5, text="Next", command= lambda: self.save_type(master,gen,f6)).pack(anchor=tk.W)
		
		#question 6
		Label(f6, text="Do you want a cooperative game?").pack(anchor=tk.W)
		coop = StringVar()
		coop.set("true")
		Radiobutton(f6, text="Yes", padx = 20, variable=coop, value="true").pack(anchor=tk.W)
		Radiobutton(f6, text="No", padx = 20, variable=coop, value="false").pack(anchor=tk.W)
		Button(f6, text="Confirm Choice", command= lambda: self.save_coop(master,coop, f7)).pack(anchor=tk.W)
		
		#question 7
		Label(f7, text="Do you want a game that has a campaign?").pack(anchor=tk.W)
		cam = StringVar()
		cam.set("true")
		Radiobutton(f7, text="Yes", padx = 20, variable=cam, value="true").pack(anchor=tk.W)
		Radiobutton(f7, text="No", padx = 20, variable=cam, value="false").pack(anchor=tk.W)
		Button(f7, text="Confirm Choice", command= lambda: self.save_campaign(master,cam)).pack(anchor=tk.W) 
		
		raise_frame(f0)
		
		master.mainloop()
	
		

	def save_person(self, master, var1,frame):
		self.__forSelf = var1.get()
		raise_frame(frame)
		master.update
		
	def save_games(self, master, g1, g2, g3, frame):
		self.__game1 = g1.text.get()
		self.__game2 = g2.text.get()
		self.__game3 = g3.text.get()
		raise_frame(frame)
		master.update
		
	def save_numPlayers(self, master, num, frame):
		self.__numPlayers = num.get()
		raise_frame(frame)
		master.update	
		
	def save_budget(self, master, maxP, frame):
		self.__maxPrice = maxP.get()
		raise_frame(frame)
		master.update
		
	def save_type(self, master, gen, frame):
		self.__gameType = gen.get()
		raise_frame(frame)
		master.update
		
	def save_coop(self, master, coop, frame):
		self.__Coop = coop.get()
		raise_frame(frame)
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
		
	def getGame2(self):
		return self.__game2
		
	def getGame3(self):
		return self.__game3
		
	def getAllGames(self):
		return [self.__game1, self.__game2, self.__game3]
		
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
		
def raise_frame(frame):
			frame.tkraise()
