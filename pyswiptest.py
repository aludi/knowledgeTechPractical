from pyswip import Prolog

import Tkinter as tk
from Tkinter import *

#or

#import tkinter as tk
#from tkinter import *

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
	#               game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)
	prolog.assertz("game(spacecorp, 2, 4, 30, 12, science_fiction)")
	prolog.assertz("game(luna, 2, 4, 60, 12, fantasy)")
	prolog.assertz("game(betrayal_legacy, 2, 5, 45, 12, adventure)")
	prolog.assertz("game(madeup1, 2, 30, 45, 12, adventure)")
	prolog.assertz("game(madeup2, 2, 5, 5, 4, adventure)")
	prolog.assertz("game(madeup3, 1, 2, 10, 5, strategy)")
	prolog.assertz("game(madeup4, 2, 5, 5, 4, adventure)")
	prolog.assertz("game(madeup5, 1, 2, 10, 5, strategy)")
	
	## testing new predicate below
	prolog.assertz("game(madeup5, 1, 2, 10, 5, 5, family, 10, T, T, strategy)")
	### to add: complexity, TYPE, budget, rec players, cooperative, vaste-groep (campaign games)), list-of-genres.


def queryOld(numberOfPlayers, genre, minAge):		#querying based on 2 things
	return prolog.query(
	"A is {}, Z = {}, M is {}, game(X, B, C,_,N,Z), numPlay(A, B, C), minimumAge(M, N)."
	.format(numberOfPlayers, genre, minAge)) #inference rule
	
def queryNew(numberOfPlayers, genre, minAge):		#querying based on 2 things
	return prolog.query(
	"A is {}, Z = {}, M is {}, game(X, B, C,_,N,Z), numPlay(A, B, C), minimumAge(M, N)."
	.format(numberOfPlayers, genre, minAge)) #inference rule

def gui():
	#TkInter for interface : link for tutorial :  https://www.python-course.eu/tkinter_labels.php
	root = tk.Tk()
	w = tk.Label(root, font = "Times 16 bold", fg = "black", text = "Hello\n I will help you with selecting a boardgame!")
	pic = tk.PhotoImage(file = "img/scaryOwl1.gif") #must always be a gif, thinter doesn't like other formats.
	w1 = tk.Label(root, image = pic).pack(side= "right")
	tk.Button(root, text="ok, let's start!").pack(side = "bottom")
	w.pack()
	
	###Derping around
	
	def raise_frame(frame):
		frame.tkraise()
	
	def save_states():
		print("Catan: %d,\n Uno: %d,\n Derp: %d" % (var1.get(), var2.get(), var3.get()))
		
	def save_person():
		print("v = %d" % v.get())
		
	def save_budget():
		print("Min price: %s\nMax price: %s" % (e1.get(), e2.get()))
		
	def save_numPlayers():
		numberOfPlayers = num.get()
		
	def save_minAge():
		minAge = minA.get()
	
	frame1 = Frame(root)
	frame2 = Frame(root)
	frame3 = Frame(root)
	frame4 = Frame(root)
	frame5 = Frame(root)
	frame6 = Frame(root)
	
	#question 1
	tk.Label(frame1, text="Is the game for yourself or for someone else?").pack()
	v = tk.IntVar()
	tk.Radiobutton(frame1, text="For me", padx = 20, variable=v, value=1).pack(anchor=tk.W)
	tk.Radiobutton(frame1, text="For someone else", padx = 20, variable=v, value=2).pack(anchor=tk.W)
	tk.Button(frame1, text="Next Question", command=save_person).pack(anchor=tk.W)
	
	frame1.pack()
	
	#question 2
	tk.Label(frame2, text="Which games have you played before?").pack()
	var1 = IntVar()
	tk.Checkbutton(frame2, text="Catan", variable=var1).pack(anchor="w")
	var2 = IntVar()
	tk.Checkbutton(frame2, text="Uno", variable=var2).pack(anchor="w")
	var3 = IntVar()
	tk.Checkbutton(frame2, text="I've never played a game in my life", variable=var3).pack(anchor="w")
	tk.Button(frame2, text="Next Question", command=save_states).pack(anchor="w")
	
	frame2.pack()
	
	#question 3
	tk.Label(frame3, text="What is the minimum price you want to pay for the game? (in euros)").pack()
	e1 = Entry(frame3)
	e1.pack()
	tk.Label(frame3, text="What is the maximum price you want to pay for the game? (in euros)").pack()
	e2 = Entry(frame3)
	e2.pack()
	#if an impossible answer is given (max < min or price < 0), make a pop-up instead of going to next question
	tk.Button(frame3, text="Next Question", command=save_budget).pack()
	
	frame3.pack()
	
	#question 4
	tk.Label(frame4, text = "Number of players").pack()
	num = Entry(frame4)
	num.pack()
	tk.Button(frame4, text="Next Question", command=save_numPlayers).pack()
	
	frame4.pack()
	
	#question 5
	tk.Label(frame5, text = "minimum age").pack()
	minA = Entry(frame5)
	minA.pack()
	tk.Button(frame5, text="Next Question", command = save_minAge).pack()
	
	frame5.pack()
	
	#question 6
	tk.Label(frame6, text = "genre").pack()
	genre = tk.IntVar()
	tk.Radiobutton(frame6, text="Science fiction", padx = 20, variable=genre, value=1).pack(anchor=tk.W)
	tk.Radiobutton(frame6, text="Adventure", padx = 20, variable=genre, value=2).pack(anchor=tk.W)
	tk.Radiobutton(frame6, text="Strategy", padx = 20, variable=genre, value=3).pack(anchor=tk.W)
	tk.Radiobutton(frame6, text="Fantasy", padx = 20, variable=genre, value=4).pack(anchor=tk.W)
	tk.Button(frame6, text="Exit", command = root.quit).pack()
	
	frame6.pack()
	
	raise_frame(frame1)
	root.mainloop()


prolog = Prolog()
kb = load_knowledge_base()		#loading the knowledge base
gui()							#loads the gui
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
print("your game-type is ", budget)

coop = input("cooperative? T/F\n")
print(coop)

camp = input("campaign?\n")
print(camp)

minAge = input("what is the minimum age of the players?\n")
print("your min age is ", minAge)



'''
prolog.query(

	"A is {},  game(Name, MinP, MaxP, Rime, Minage, Complexity, Type, Budget, CooperativeTF, CampaignTF, Listgenre), numPlay(A, MinP, MaxP),". numberOfPlayers

	game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)
	"A is {}, Z = {}, M is {}, game(X, B, C,_,N,Z), numPlay(A, B, C), minimumAge(M, N)."
	.format(numberOfPlayers, genre, minAge)) #inference rule
'''
x= 0
for soln in queryOld(numberOfPlayers, genre, minAge):
	print("you can play:", (soln["X"]))
	x = 1
if x == 0:
	print("sorry, we couldn't find any games for you")



## retracting facts?
## only asserting facts when gui prompts or something?

'''
/* queries: 
* to select a game where number of players is 5: A is 5, game(X, B, C,_,_,_), numPlay(A,B,C).
* to find the genre of the game luna: game(luna,_,_,_,_,X).
*
* Format of game.6: game(name, minNumPlayers, maxNumPlayers, minPlayTime, age, category)
*/


numPlay(A,MIN, MAX):- A >= MIN, A =< MAX.
game(spacecorp, 2, 4, 30, twaalf, science_fiction).
game(luna, 2, 4, 60, twaalf, fantasy).
game(betrayal_legacy, 2, 5, 45, twaalf, adventure).
game(madeup1, 2, 30, 45, twaalf, adventure).
game(madeup2, 2, 5, 5, vijf, adventure).
game(madeup3, 1, 2, 10, vijf, strategy).

'''
