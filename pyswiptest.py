from pyswip import Prolog
import tkinter as tk


def do_something():
	print("im doing something")
	
def load_knowledge_base():		#implementing knowledge base in separate function
	prolog.assertz("game(spacecorp, 2, 4, 30, 12, science_fiction)")
	prolog.assertz("game(luna, 2, 4, 60, 12, fantasy)")
	prolog.assertz("game(betrayal_legacy, 2, 5, 45, 12, adventure)")
	prolog.assertz("game(madeup1, 2, 30, 45, 12, adventure)")
	prolog.assertz("game(madeup2, 2, 5, 5, 4, adventure)")
	prolog.assertz("game(madeup3, 1, 2, 10, 5, strategy)")
	prolog.assertz("game(madeup4, 2, 5, 5, 4, adventure)")
	prolog.assertz("game(madeup5, 1, 2, 10, 5, strategy)")


def query(numberOfPlayers, genre, minAge):		#querying based on 2 things
	return prolog.query("A is {}, Z = {}, M is {}, game(X, B, C,_,N,Z), numPlay(A, B, C), minimumAge(M, N).".format(numberOfPlayers, genre, minAge)) #inference rule

def gui():
	#TkInter for interface : link for tutorial :  https://www.python-course.eu/tkinter_labels.php
	root = tk.Tk()
	w = tk.Label(root, font = "Times 16 bold", fg = "black", text = "Hello\n I will help you with selecting a boardgame!")
	pic = tk.PhotoImage(file = "img/scaryOwl1.gif") #must always be a gif, thinter doesn't like other formats.
	w1 = tk.Label(root, image = pic).pack(side= "right")
	tk.Button(root, text="ok, let's start!", command = do_something).pack(side = "bottom")
	w.pack()
	root.mainloop()

#knowledge base:
'''
prolog.assertz("game(spacecorp, 2, 4, 30, twaalf, science_fiction)")
prolog.assertz("game(luna, 2, 4, 60, twaalf, fantasy)")
prolog.assertz("game(betrayal_legacy, 2, 5, 45, twaalf, adventure)")
prolog.assertz("game(madeup1, 2, 30, 45, twaalf, adventure)")
prolog.assertz("game(madeup2, 2, 5, 5, vijf, adventure)")
prolog.assertz("game(madeup3, 1, 2, 10, vijf, strategy)")'''

prolog = Prolog()
kb = load_knowledge_base()		#loading the knowledge base
gui()							#loads the gui
#rule for min/max
prolog.assertz("numPlay(A,MIN, MAX):- A >= MIN, A =< MAX")
# rule for min age
prolog.assertz("minimumAge(M, N):- N >= M")



#unsubtle way of selecting for 

numberOfPlayers = input("with how many players do you want to play?\n")
print("you want to play with ", numberOfPlayers, "players")
genre = input("what genre do you want?\n")
print("you want to play a ", genre , "game")
minAge = input("what is the minimum age of the players?\n")
print("your min age is ", minAge)


x= 0
for soln in query(numberOfPlayers, genre, minAge):
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
