import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from PrologInteraction import *
from functools import partial

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
		f2one = AutocompleteEntry(master)
		f2two = AutocompleteEntry(master)
		f2three = AutocompleteEntry(master)
		f3 = Frame(master)
		f4 = Frame(master)
		f5 = Frame(master)
		f6 = Frame(master)
		f7 = Frame(master)
		f8 = Frame(master)
		
		
		for frame in (f0, f1, f2one, f2two, f2three, f3, f4, f5, f6, f7, f8):
		    frame.grid(row=0, column=0, sticky='news')
		    
		
		#dubble underscore encapsulates the variable, it can't be directly accessed from main.py
		prologThing = PrologInteraction()
		self.__forSelf = True
		self.__numPlayers = 1
		self.__minPrice = 10000
		self.__maxPrice = 0
		self.__gameType = "strategy"
		self.__gameTime = 60
		self.__minAge = 100
		self.__Coop = "true"
		self.__Campaign = "true"
		self.__ListType = prologThing.getTypesForGUI() 		#getting types-lists (family, strategy) from prologInteraction
		self.__ListNames = prologThing.getNamesGamesForGUI() #getting all names of all games from prologInteraction
		self.__ListGenres = prologThing.getGenresForGUI()
		self.__game1 = "some"
		self.__game2 = "some"
		self.__game3 = "some"
		self.__finalGames = "some"
		self.__genreList = PrologInteraction()
		self.__finished = False
			
		
		
		#TkInter for interface : link for tutorial :  https://www.python-course.eu/tkinter_labels.php
		w = Label(f0, font = "TkDefaultFont 16", fg = "black", text = "Hello,\n I will help you with selecting a board game!")
		w.pack(fill=X,padx=0)
		pic = PhotoImage(file = "img/scaryOwl1.gif") #must always be a gif, thinter doesn't like other formats.
		w1 = Label(f0, image = pic)
		w1.image = pic
		w1.pack(fill=X,padx=0)
		Button(f0, font = "TkDefaultFont 16", text="Exit", command= master.destroy).pack(fill=X,padx=250, side="bottom")
<<<<<<< HEAD
		Button(f0, font = "TkDefaultFont 16", text="Start", command= lambda: raise_frame(f1)).pack(fill=X,padx=250,side="bottom")
	    
=======
		Button(f0, font = "TkDefaultFont 16", text="Start", command= lambda: raise_frame(f1a)).pack(fill=X,padx=250,side="bottom")
>>>>>>> 6ec3a9b4d4e6b9f04ce5c1269726324c755e72ee

		#question 1
		pic = PhotoImage(file = "img/scaryOwl1.gif") 
		w1 = Label(f1, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Label(f1, font = "TkDefaultFont 16", text="Question 1.", padx = 200, pady = 30).pack(anchor=tk.W)
		Label(f1, font = "TkDefaultFont 16", text="How old is your youngest player?", padx = 200).pack(anchor=tk.W)
		minA = Entry(f1)
		minA.pack(anchor=tk.W, padx = 200)
		NA = IntVar()
		Checkbutton(f1, font = "TkDefaultFont 16", text="Doesn't matter", padx = 200, variable = NA, onvalue=1, offvalue=0).pack(anchor=tk.W)
		Button(f1, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_minAge(master,minA,NA,f2one)).pack(fill=X,padx=250,side="bottom")
		
		#question 2.1 previous games
		#pic = PhotoImage(file = "img/scaryOwl1.gif") 
		#w1 = Label(f2one, image = pic)
		#w1.image = pic
		#w1.grid(row = 10, column = 100, sticky = S)
		Label(f2one, font = "TkDefaultFont 16", text="Question 2a.").grid(row=0, column=0, sticky=W)
		Label(f2one, font = "TkDefaultFont 16", text="Name three games you like-1").grid(row=1, column=0, sticky=W)
		Label(f2one, font = "TkDefaultFont 10 italic", text="If the game you like is not in the database, please leave the entry blank").grid(row=2, column=0, sticky=W)
		game1Entry = StringVar()
		f2one.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >",columnNum = 0, rowNum=4)	#changed to listNames
		game1Entry = f2one.text
		Button(f2one, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_game1(master,game1Entry, f2two)).grid(row=19, column=50, sticky=S)
		Button(f2one, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f1)).grid(row=20, column=50,sticky=S)
		
		#question 2.2
		Label(f2two, font = "TkDefaultFont 16", text="Question 2b.").grid(row=0, column=0, sticky=W)
		Label(f2two, font = "TkDefaultFont 16", text="Name three games you like-2").grid(row=1, column=0, sticky=W)
		Label(f2two, font = "TkDefaultFont 10 italic", text="If the game you like is not in the database, please leave the entry blank").grid(row=2, column=0, sticky=W)
		game2Entry = StringVar()
		f2two.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >",columnNum=0,rowNum=4)	#changed to listNames
		game2Entry = f2two.text
		Button(f2two, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_game2(master,game2Entry, f2three)).grid(row=19, sticky=W+S)
		Button(f2two, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f2one)).grid(row=20, sticky=W+S)
		
		
		#question 2.3
		Label(f2three, font = "TkDefaultFont 16", text="Question 2c.").grid(row=0, column=0, sticky=W)
		Label(f2three, font = "TkDefaultFont 16", text="Name three games you like-3").grid(row=1, column=0, sticky=W)
		Label(f2three, font = "TkDefaultFont 10 italic", text="If the game you like is not in the database, please leave the entry blank").grid(row=2, column=0)
		game3Entry = StringVar()
		f2three.build(entries=self.__ListNames, no_results_message="<No results found for '{}' >",columnNum=0,rowNum=4)	#changed to listNames
		game3Entry = f2three.text
		Button(f2three, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_game3(master,game3Entry, f3)).grid(row=19, sticky=W+S)
		Button(f2three, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f2two)).grid(row=20, sticky=W+S)
		
		#question 3
		pic = PhotoImage(file = "img/scaryOwl1.gif") 
		w1 = Label(f3, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Label(f3, font = "TkDefaultFont 16", text="Question 3.").pack(anchor=tk.W)
		Label(f3, font = "TkDefaultFont 16", text="What is the preferred number of players?").pack(anchor=tk.W) #make sure input is valid!
		num = Entry(f3)
		num.pack(anchor=tk.W)
		NA = IntVar()
		Checkbutton(f3, font = "TkDefaultFont 16", text="No preference", variable = NA, onvalue=1, offvalue=0).pack(anchor=tk.W)
		Button(f3, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f2three)).pack(fill=X,padx=250,side="bottom")
		Button(f3, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_numPlayers(master,num,NA,f4)).pack(fill=X,padx=250,side="bottom")
		
		
		#question 4
		pic = PhotoImage(file = "img/scaryOwl1.gif") 
		w1 = Label(f4, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Label(f4, font = "TkDefaultFont 16", text="Question 4.").pack(anchor=tk.W)
		Label(f4, font = "TkDefaultFont 16", text="What is the maximum price you want to pay for the game?").pack(anchor=tk.W)
		maxP = IntVar()
		maxP.set("10")
		Radiobutton(f4, font = "TkDefaultFont 16", text="10 dollar", variable=maxP, value = 10).pack(anchor=tk.W)
		Radiobutton(f4, font = "TkDefaultFont 16", text="20 dollar", variable=maxP, value = 20).pack(anchor=tk.W)
		Radiobutton(f4, font = "TkDefaultFont 16", text="30 dollar", variable=maxP, value = 30).pack(anchor=tk.W)
		Radiobutton(f4, font = "TkDefaultFont 16", text="40 dollar", variable=maxP, value = 40).pack(anchor=tk.W)
		Radiobutton(f4, font = "TkDefaultFont 16", text="50 dollar", variable=maxP, value = 50).pack(anchor=tk.W)
		Radiobutton(f4, font = "TkDefaultFont 16", text="75 dollar", variable=maxP, value = 75).pack(anchor=tk.W)
		Radiobutton(f4, font = "TkDefaultFont 16", text="100 dollar", variable=maxP, value = 100).pack(anchor=tk.W)
		Radiobutton(f4, font = "TkDefaultFont 16", text="150 dollar", variable=maxP, value = 150).pack(anchor=tk.W)
		Radiobutton(f4, font = "TkDefaultFont 16", text="more than 150 dollar", variable=maxP, value = 1000).pack(anchor=tk.W)
		Button(f4, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f3)).pack(fill=X,padx=250,side="bottom")
		Button(f4, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_budget(master,maxP,f5)).pack(fill=X,padx=250,side="bottom")
			
			
		def typesExplained():
			popup = Tk()
			popup.wm_title("Types explained")
			Label(popup, text = "Thematic:", font = "TkDefaultFont 11 bold", fg = "black", padx=20,pady=2).grid(row = 0,sticky=W)
			Label(popup, text = "Emphasis on narative", font = "TkDefaultFont 10", fg = "black").grid(row=0,column=1,sticky=W)
			Label(popup, text = "Strategy:", font = "TkDefaultFont 11 bold", fg = "black", padx=20,pady=2).grid(row = 1,sticky=W)
			Label(popup, text = "More complex games", font = "TkDefaultFont 10", fg = "black").grid(row=1,column=1,sticky=W)
			Label(popup, text = "Wargame:", font = "TkDefaultFont 11 bold", fg = "black", padx=20,pady=2).grid(row = 2,sticky=W)
			Label(popup, text = "Conflict simulation", font = "TkDefaultFont 10", fg = "black").grid(row=2,column=1,sticky=W)
			Label(popup, text = "Family:", font = "TkDefaultFont 11 bold", fg = "black", padx=20,pady=2).grid(row = 3,sticky=W)
			Label(popup, text = "Fun for kids and adults", font = "TkDefaultFont 10", fg = "black").grid(row=3,column=1,sticky=W)
			Label(popup, text = "Customizable:", font = "TkDefaultFont 11 bold", fg = "black", padx=20,pady=2).grid(row = 4,sticky=W)
			Label(popup, text = "Has collectibles (such as cards)", font = "TkDefaultFont 10", fg = "black").grid(row=4,column=1,sticky=W)
			Label(popup, text = "Party:", font = "TkDefaultFont 11 bold", fg = "black", padx=20,pady=2).grid(row = 5,sticky=W)
			Label(popup, text = "Few rules, lots of laughs", font = "TkDefaultFont 10", fg = "black").grid(row=5,column=1,sticky=W)
			
		
		#question 5
		pic = PhotoImage(file = "img/scaryOwl1.gif") 
		w1 = Label(f5, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Label(f5, font = "TkDefaultFont 16", text="Question 5.").pack(anchor=tk.W)
		Button(f5, font = "TkDefaultFont 16", text="What type of game do you want to play?", command= typesExplained).pack(anchor=tk.W)
		gen = StringVar()
		count = 0
		for i in self.__ListType:		#loops through all game-types in database.
			if count == 0:
				gen.set(i)
				count = 1
			Radiobutton(f5, font = "TkDefaultFont 16", text=i, padx = 20, variable=gen, value=i).pack(anchor=tk.W)
		Radiobutton(f5, font = "TkDefaultFont 16", text="No preference", padx = 20, variable=gen, value="_").pack(anchor=tk.W)
		Button(f5, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f4)).pack(fill=X,padx=250,side="bottom")
		Button(f5, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_type(master,gen,f6)).pack(fill=X,padx=250,side="bottom")
		
		#question 6
		pic = PhotoImage(file = "img/scaryOwl1.gif") 
		w1 = Label(f6, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Label(f6, font = "TkDefaultFont 16", text="Question 6.").pack(anchor=tk.W)
		Label(f6, font = "TkDefaultFont 16", text="How long do you want your average game to be? (in minutes)").pack(anchor=tk.W)
		time = Entry(f6)
		time.pack(anchor=tk.W)
		NA = IntVar()
		Checkbutton(f6, font = "TkDefaultFont 16", text="No preference", variable = NA, onvalue=1, offvalue=0).pack(anchor=tk.W)
		Button(f6, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f5)).pack(fill=X,padx=250,side="bottom")
		Button(f6, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_time(master,time,NA, f7)).pack(fill=X,padx=250,side="bottom")
		
		
		def cooperative():
			messagebox.showinfo("Cooperative play","Co-operative play encourages or requires players to work together to beat the game. There is little or no competition between players. Either the players win the game by reaching a pre-determined objective, or all players lose the game, often by not reaching the objective before a certain event happens.")
		
		#question 7
		pic = PhotoImage(file = "img/scaryOwl1.gif") 
		w1 = Label(f7, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Label(f7, font = "TkDefaultFont 16", text="Question 7.").pack(anchor=tk.W)
		Button(f7, font = "TkDefaultFont 16", text="Do you want a cooperative game?", command = cooperative).pack(anchor=tk.W)
		Label(f7, font = "TkDefaultFont 10", text="(click on the question if you don't know what a cooperative game is)").pack(anchor=tk.W)
		coop = StringVar()
		coop.set("true")
		Radiobutton(f7, font = "TkDefaultFont 16", text="Yes", padx = 20, variable=coop, value="true").pack(anchor=tk.W)
		Radiobutton(f7, font = "TkDefaultFont 16", text="No", padx = 20, variable=coop, value="false").pack(anchor=tk.W)
		Radiobutton(f7, font = "TkDefaultFont 16", text="No preference", padx = 20, variable=coop, value="either").pack(anchor=tk.W)
		Button(f7, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f6)).pack(fill=X,padx=250,side="bottom")
		Button(f7, font = "TkDefaultFont 16", text="Next Question", command= lambda: self.save_coop(master,coop, f8)).pack(fill=X,padx=250,side="bottom")
		
		def campaign():
			messagebox.showinfo("Campaign games","Campaign games are games where the game and/or characters change over time, such that the results of one game may influence future plays.")
		
		#question 8
		pic = PhotoImage(file = "img/scaryOwl1.gif") 
		w1 = Label(f8, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Label(f8, font = "TkDefaultFont 16", text="Question 8.").pack(anchor=tk.W)
		Button(f8, font = "TkDefaultFont 16", text="Do you want a game that has a campaign?",command=campaign).pack(anchor=tk.W)
		Label(f8, font = "TkDefaultFont 10", text="(click on the question if you don't know what a campaign game is)").pack(anchor=tk.W)
		cam = StringVar()
		cam.set("true")
		Radiobutton(f8, font = "TkDefaultFont 16", text="Yes", padx = 20, variable=cam, value="true").pack(anchor=tk.W)
		Radiobutton(f8, font = "TkDefaultFont 16", text="No", padx = 20, variable=cam, value="false").pack(anchor=tk.W)
		Radiobutton(f8, font = "TkDefaultFont 16", text="No preference", padx = 20, variable=cam, value="either").pack(anchor=tk.W)
		Button(f8, font = "TkDefaultFont 16", text="Previous Question", command= lambda: raise_frame(f7)).pack(fill=X,padx=250,side="bottom")
		Button(f8, font = "TkDefaultFont 16", text="Recommend me some games!", command= lambda: self.save_campaign(master,cam)).pack(fill=X,padx=250,side="bottom")
		
		
		raise_frame(f0)
		master.mainloop()
		
	def displayGameInfo(self,game):
		popup = Tk()
		popup.wm_title(game.decode())
		Label(popup, text = "This game falls under the following categories:",font = "TkDefaultFont 11 bold", fg = "black", padx = 20,pady=2).grid(columnspan=4)
		genres = PrologInteraction().getGenreList(game.decode())
		#players = PrologInteraction().getNumPlayers(game.decode())
		r = 1
		for j in genres:
			Label(popup, text=j,font = "TkDefaultFont 10 italic", fg = "blue", padx = 40).grid(row=r,sticky=W)
			r = r+1
		
		numPlayers = PrologInteraction().getNumPlayers(game.decode())	
		Label(popup, text = "Number of players:", font = "TkDefaultFont 11 bold", fg = "black", padx=20,pady=2).grid(row = r+1, column=0,sticky=W)
		Label(popup, text = "%s-%s"%(numPlayers[0],numPlayers[1]), font = "TkDefaultFont 10 italic", fg = "blue").grid(row = r+1, column=1,sticky=W)
		Label(popup, text = "Best:", font = "TkDefaultFont 11 bold", fg = "black").grid(row = r+1, column=2,sticky=W)
		Label(popup, text = "%s"%numPlayers[2], font = "TkDefaultFont 10 italic", fg = "blue").grid(row = r+1, column=3,sticky=W)
		
		playTime = PrologInteraction().getPlayTime(game.decode())
		Label(popup, text = "Playtime:", font = "TkDefaultFont 11 bold", fg = "black",padx=20,pady=2).grid(row=r+2, sticky=W) 
		Label(popup, text = "%s-%s min"%(playTime[0],playTime[1]), font = "TkDefaultFont 10 italic", fg = "blue").grid(row = r+2, column=1,sticky=W)
		
		age = PrologInteraction().getAge(game.decode())
		Label(popup, text = "Age:", font = "TkDefaultFont 11 bold", fg = "black",padx=20,pady=2).grid(row=r+3, sticky=W) 
		Label(popup, text = "%s+"%age, font = "TkDefaultFont 10 italic", fg = "blue").grid(row = r+3, column=1,sticky=W)
		
		
		Button(popup,text="Okay",command=popup.destroy).grid(column=3)
		popup.mainloop()
	
	def displayChanges(self, change):
		if change == 'Best Matching Games':
			popup = Tk()
			popup.wm_title("explanation")
			Label(popup, text = "These are the games that match all of your specifications",font = "TkDefaultFont 11 bold", fg = "black", padx = 20).pack(anchor=tk.W)
			Button(popup,text="Okay",command=popup.destroy).pack()
			popup.mainloop()
		if change == "Expanding Search...":
			popup = Tk()
			popup.wm_title("explanation")
			explanation = "These games match fewer of your specifications: \nThe number of players is in range instead of recommended, \ntime range is wider by 20 minutes on both sides, \ncomplexity range is also increased!"
			Label(popup, text = explanation,font = "TkDefaultFont 11 bold", fg = "black", padx = 20).pack(anchor=tk.W)
			Button(popup,text="Okay",command=popup.destroy).pack()
			popup.mainloop()
		if change == "Expanding Search Again...":
			popup = Tk()
			popup.wm_title("explanation")
			explanation = "These games have even wider search criteria: \nType preference is removed, \nbudget is expanded with 10 euros, \nplayer range has increased, \nand time range has increased with 30 minutes on both sides"
			Label(popup, text = explanation,font = "TkDefaultFont 11 bold", fg = "black", padx = 20).pack(anchor=tk.W)
			Button(popup,text="Okay",command=popup.destroy).pack()
			popup.mainloop()
		
	
			#final result
	def printResults(self, master, finalGames):
		pic = PhotoImage(file = "img/scaryOwlBig.gif")
		master1 = Label(master, image = pic)
		master1.image = pic
		master1.pack(side = "left")
		count = 0
		for i in finalGames:
			if count >= 5: 
				break
			if i == "Best Matching Games" or i == "Expanding Search..." or i == "Expanding Search Again...":
				#Label(master, text=i,font = "TkDefaultFont 20 bold", fg = "black", padx = 20).pack(anchor=tk.W)
				Button(master, text = i, font = "TkDefaultFont 20 bold", fg = "black", padx = 20, command = partial(self.displayChanges,i)).pack(anchor = tk.W)
			else:
				count = count+1
				Button(master, text=i,font = "TkDefaultFont 20", fg = "red", padx = 20, command= partial(self.displayGameInfo,i)).pack(anchor=tk.W)		
		Button(master, font = "TkDefaultFont 16", text="Exit", command= master.destroy).pack(fill=X,padx=250, side="bottom")
		master.mainloop()	
		
	def errorMessage(self):
		messagebox.showinfo("Error","Input should be a digit")

		
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
	 
	def save_numPlayers(self, master, num, NA, frame):
		if not (num.get().isdigit() or num.get() ==''):
			self.errorMessage()
			return
		self.__numPlayers = num.get()
		if self.__numPlayers == '' or NA.get() == 1:
			self.__numPlayers = 0		#to change later, difference between "doesn't matter" and "nothing filled in"
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
		
	def save_time(self,master, time, NA, frame):
		if not (time.get().isdigit() or time.get() ==''):
			self.errorMessage()
			return
		self.__gameTime = time.get()
		if self.__gameTime == '' or NA.get() == 1:
			self.__gameTime = 0
		raise_frame(frame)
		master.update
		
	def save_coop(self, master, coop, frame):
		self.__Coop = coop.get()
		if self.__Coop == "either":
			self.__Coop = "_"
		print("coop", self.__Coop)
		raise_frame(frame)
		master.update
		
	def save_campaign(self, master, cam):
		self.__Campaign = cam.get()
		self.__finished = True
		if self.__Campaign== "either":
			self.__Campaign = "_"
		print("camp", self.__Campaign)
		master.destroy()
		master.update

	def save_minAge(self, master, minA, NA, frame):
		if not (minA.get().isdigit() or minA.get() ==''):
			self.errorMessage()
			return
		self.__minAge = minA.get()
		if self.__minAge == '' or NA.get() == 1 :
			self.__minAge = 100
		raise_frame(frame)
		master.update
	
	
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
		games = []
		if self.__game1 != '': 
			games.append(self.__game1)
		if self.__game2 != '': 
			games.append(self.__game2)
		if self.__game3 != '': 
			games.append(self.__game3)
		return games
		
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
	
	def getFinished(self):
		return self.__finished
		
def raise_frame(frame):
	frame.tkraise()
