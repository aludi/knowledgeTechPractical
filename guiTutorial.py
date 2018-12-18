import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
from PrologInteraction import *

from tkinter_autocomplete import AutocompleteEntry


class Gui: 
	
	def __init__(self, master, whichDef, finalList): 
		if(whichDef == 0):
			self.makeGui(master)
		else:
			self.printResults(master, finalList)
		
	def makeGui(self,master):
		
		def raise_frame(frame):
			frame.tkraise()
			
		f0 = Frame(master)
		f1 = Frame(master)
		f1a = Frame(master)
		f2one = AutocompleteEntry(master)
		f2two = AutocompleteEntry(master)
		f2three = AutocompleteEntry(master)
		f3 = Frame(master)
		f4 = Frame(master)
		f5 = Frame(master)
		f6 = Frame(master)
		f61 = Frame(master)
		f7 = Frame(master)
		
		
		for frame in (f0, f1, f1a, f2one, f2two, f2three, f3, f4, f5, f6,f61, f7):
		    frame.grid(row=0, column=0, sticky='news')
		
		#dubble underscore encapsulates the variable, it can't be directly accessed from main.py
		prologThing = PrologInteraction()
		self.__forSelf = True
		self.__numPlayers = 1

		self.__minPrice = 10000
		self.__maxPrice = 0
		self.__gameType = "strategy"
		self.__Coop = "true"
		self.__Campaign = "true"
		self.__ListType = prologThing.getTypesForGUI() 		#getting types-lists (family, strategy) from prologInteraction
		self.__ListNames = prologThing.getNamesGamesForGUI() #getting all names of all games from prologInteraction
		self.__ListGenres = prologThing.getGenresForGUI()
		self.__game1 = "some"
		self.__game2 = "some"
		self.__game3 = "some"
		self.__finalGames = "some"
		
		
		
		#TkInter for interface : link for tutorial :  https://www.python-course.eu/tkinter_labels.php
		w = Label(f0, font = "Times 16 bold", fg = "black", text = "Hello\n I will help you with selecting a boardgame!")
		pic = PhotoImage(file = "img/scaryOwl1.gif") #must always be a gif, thinter doesn't like other formats.
		w1 = Label(f0, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Button(f0, text="Exit", command= master.destroy).pack(side = "left")
		Button(f0, text="Start", command= lambda: raise_frame(f1)).pack(side = "left")
		w.pack()
		
		
		#question 1 
		Label(f1, text="Is the game for yourself or for someone else?").pack(anchor=tk.W)
		var1 = BooleanVar()
		var1.set(True)
		Radiobutton(f1, text="For me", padx = 20, variable=var1, value=True).pack(anchor=tk.W)
		Radiobutton(f1, text="For someone else", padx = 20, variable=var1, value=False).pack(anchor=tk.W)
		Button(f1, text="Next", command= lambda: self.save_person(master,var1,f1a)).pack(anchor=tk.W)	
		
		#question leeftijd
		Label(f1a, text="How old is your youngest player?").pack(anchor=tk.W)
		minA = Entry(f1a)
		minA.pack(anchor=tk.W)
		Button(f1a, text="Next", command= lambda: self.save_minAge(master,minA,f2one)).pack(anchor=tk.W)	
		
		
		#TEMPORARY
		games = ("Small world", "Monopoly", "Kolonisten van Catan", "pandemic", "Agricola", "Wizard")
		def choseEntry(entry):
			print(entry)
		
		#question 2.1 previous games
		Label(f2one, text="Name three games you like-1").grid()
		game1Entry = StringVar()


		f2one.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >",columnNum = 0, rowNum=2)	#changed to listNames
		game1Entry = f2one.text
		Button(f2one, text="Next", command= lambda: self.save_game1(master,game1Entry, f2two)).grid()
		
		#question 2.2
		Label(f2two, text="Name three games you like-2").grid()
		game2Entry = StringVar()
		f2two.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >",columnNum=0,rowNum=4)	#changed to listNames
		game2Entry = f2two.text
		Button(f2two, text="Next", command= lambda: self.save_game2(master,game2Entry, f2three)).grid()
		
		#question 2.3
		Label(f2three, text="Name three games you like-3").grid()
		game3Entry = StringVar()
		f2three.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >",columnNum=0,rowNum=6)	#changed to listNames
		game3Entry = f2three.text
		Button(f2three, text="Next", command= lambda: self.save_game3(master,game3Entry, f3)).grid()
		
		#question 3
		Label(f3, text="What is the preferred number of players?").pack(anchor=tk.W) #make sure input is valid!
		num = Entry(f3)
		num.pack(anchor=tk.W)
		Button(f3, text="Next", command= lambda: self.save_numPlayers(master,num,f4)).pack(anchor=tk.W)
		
		#question 4
		Label(f4, text="What is your price range?").pack(anchor=tk.W)
		Label(f4, text="You can select multiple boxes").pack(anchor=tk.W)
		P0 = IntVar()
		P1 = IntVar()
		P2 = IntVar()
		P3 = IntVar()
		P4 = IntVar()
		P5 = IntVar()
		Checkbutton(f4, text="0-10 euro", variable=P0, onvalue = 10, offvalue = 0).pack(anchor=tk.W)
		Checkbutton(f4, text="10-20 euro", variable=P1, onvalue = 20, offvalue = 0).pack(anchor=tk.W)
		Checkbutton(f4, text="20-30 euro", variable=P2, onvalue = 30, offvalue = 0).pack(anchor=tk.W)
		Checkbutton(f4, text="30-40 euro", variable=P3, onvalue = 40, offvalue = 0).pack(anchor=tk.W)
		Checkbutton(f4, text="40-50 euro", variable=P4, onvalue = 50, offvalue = 0).pack(anchor=tk.W)
		Checkbutton(f4, text="more than 50 euro", variable=P5, onvalue = 61, offvalue = 0).pack(anchor=tk.W)
		#if an impossible answer is given (max < min or price < 0), make a pop-up instead of going to next question
		Button(f4, text="Next", command= lambda: self.save_budget(master,P0,P1,P2,P3,P4,P5,f5)).pack(anchor=tk.W)
			
		#question 5
		Label(f5, text="What type of game do you want to play?").pack(anchor=tk.W)
		gen = StringVar()
		gen.set("strategy")
		for i in self.__ListType:		#loops through all game-types in database.
			Radiobutton(f5, text=i, padx = 20, variable=gen, value=i).pack(anchor=tk.W)
		Button(f5, text="Next", command= lambda: self.save_type(master,gen,f61)).pack(anchor=tk.W)
		
		#question 5
		Label(f61, text="How long do you want to play?").pack(anchor=tk.W)
		time = Entry(f61)
		time.pack(anchor=tk.W)
		Button(f61, text="Next", command= lambda: self.save_time(master,time,f6)).pack(anchor=tk.W)
		
		#question 6
		Label(f6, text="Do you want a cooperative game?").pack(anchor=tk.W)
		coop = StringVar()
		coop.set("true")
		Radiobutton(f6, text="Yes", padx = 20, variable=coop, value="true").pack(anchor=tk.W)
		Radiobutton(f6, text="No", padx = 20, variable=coop, value="false").pack(anchor=tk.W)
		Button(f6, text="Next", command= lambda: self.save_coop(master,coop, f7)).pack(anchor=tk.W)
		
		#question 7
		Label(f7, text="Do you want a game that has a campaign?").pack(anchor=tk.W)
		cam = StringVar()
		cam.set("true")
		Radiobutton(f7, text="Yes", padx = 20, variable=cam, value="true").pack(anchor=tk.W)
		Radiobutton(f7, text="No", padx = 20, variable=cam, value="false").pack(anchor=tk.W)
		Button(f7, text="End", command= lambda: self.save_campaign(master,cam)).pack(anchor=tk.W) 
		raise_frame(f0)
		
		master.mainloop()
	
			#final result
	def printResults(self, master, finalGames):
		Label(master,font = "Times 20 bold", fg = "blue", text="Here are your final games").pack(anchor=tk.W, side = "top")
		pic = PhotoImage(file = "img/scaryOwl1.gif")
		master1 = Label(master, image = pic)
		master1.image = pic
		master1.pack(side = "left")
		for i in finalGames:
			print(i)
			Label(master, text=i,font = "Times 20 bold", fg = "red", padx = 20).pack(anchor=tk.W, side = "right")
		Button(master, text="Exit", command= master.destroy).pack(side = "right")
		master.mainloop()	

	def save_person(self, master, var1,frame):
		self.__forSelf = var1.get()
		raise_frame(frame)
		master.update
		
	def save_game1(self, master, g1, frame):
		self.__game1 = g1.get()
		print("first saved game ")
		print(self.__game1)
		raise_frame(frame)
		master.update
		
	def save_game2(self, master, g2, frame):
		self.__game2 = g2.get()
		print("second saved game")
		print(self.__game2)
		raise_frame(frame)
		master.update
		
	def save_game3(self, master, g3, frame):
		self.__game3 = g3.get()
		print("third saved game")
		print(self.__game3)
		raise_frame(frame)
		master.update
	
	def save_numPlayers(self, master, num, frame):
		self.__numPlayers = num.get()
		if self.__numPlayers == '':
			self.__numPlayers = 1		#to change later, difference between "doesn't matter" and "nothing filled in"
		raise_frame(frame)
		master.update	
		
	def save_budget(self, master, P0,P1,P2,P3,P4,P5, frame):
		for x in (P0,P1,P2,P3,P4,P5):
			print(x.get())
			if x.get() != 0 and x.get()-10 < self.__minPrice:
				self.__minPrice = x.get()-10
			if x.get() > self.__maxPrice:
				self.__maxPrice = x.get()
			if x.get() == 61:
				self.__maxPrice = 10000

		if self.__minPrice == 10000 and self.__maxPrice == 0:
			self.__minPrice = 0
			self.__maxPrice = 10000
		print("minprice")
		print(self.__minPrice)
		print("maxprice")
		print(self.__maxPrice)
		raise_frame(frame)
		master.update
		
	def save_type(self, master, gen, frame):
		self.__gameType = gen.get()
		raise_frame(frame)
		master.update
		
	
	def save_time(self,master, time, frame):
		self.__gameTime = time.get()
		if self.__gameTime == '':
			self.__gameTime = 10000
		raise_frame(frame)
		master.update
		
	def save_coop(self, master, coop, frame):
		self.__Coop = coop.get()
		raise_frame(frame)
		master.update
		
		
	def save_campaign(self, master, cam):
		self.__Campaign = cam.get()
		master.destroy()
		master.update

	def save_minAge(self, master, minA, frame):
		self.__minAge = minA.get()
		if self.__minAge == '':
			self.__minAge = 0
		raise_frame(frame)
		master.update
		
	def callback(*args):
		print("variable changed")
	
	
	def setFinalGames(self, finalGames):
		self.__finalGames = finalGames
		
	# getters	

	def getPerson(self):
		return self.__forSelf
		
	def getMinAge(self):
		return self.__minAge	
	
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
		
	def getTime(self):
		return self.__gameTime
		
	def getCoop(self):
		return self.__Coop
		
	def getCampaign(self):
		return self.__Campaign
		
def raise_frame(frame):
			frame.tkraise()
