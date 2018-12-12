import tkinter as tk
from tkinter import *
from functools import partial


class Gui: 
	
	forSelf = True
	
	def __init__(self, master): 
		
		#TkInter for interface : link for tutorial :  https://www.python-course.eu/tkinter_labels.php
		w = Label(root, font = "Times 16 bold", fg = "black", text = "Hello\n I will help you with selecting a boardgame!")
		pic = PhotoImage(file = "img/scaryOwl1.gif") #must always be a gif, thinter doesn't like other formats.
		w1 = Label(root, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Button(root, text="ok, let's start!").pack(side = "bottom")
		w.pack()
		
		#question 1 # the forSelf variable is undefined and causes a crash
	
		Label(master, text="Is the game for yourself or for someone else?").pack()
		var1 = BooleanVar()
		Radiobutton(master, text="For me", padx = 20, variable=var1, value=True).pack(anchor=tk.W)
		Radiobutton(master, text="For someone else", padx = 20, variable=var1, value=False).pack(anchor=tk.W)
		Button(master, text="Next Question", command= lambda: self.save_person(var1)).pack(anchor=tk.W)	
		
		

	
	def save_states():
		print("Catan: %d,\n Uno: %d,\n Derp: %d" % (var1.get(), var2.get(), var3.get()))
		
	def save_person(self, var1):
		self.forSelf = var1.get()
		print("Self = ", forSelf)
		
	def save_budget():
		print("Min price: %s\nMax price: %s" % (e1.get(), e2.get()))
		
	def save_numPlayers():
		numberOfPlayers = num.get()
		
	def save_minAge():
		minAge = minA.get()
		
	def callback(*args):
		print("variable changed")
	
	
	
	# getters	
	def getPerson(self):
		return self.forSelf	
		#frame = Frame(master)
		#frame.pack()
		
		#self.printButton = Button(frame, text= "Print Message", command=self.printMessage)
		#self.printButton.pack(side=LEFT)
		
		#self.quitButton =  Button(frame, text= "Quit", command = frame.quit)
		#self.quitButton.pack(side=LEFT)
		
	#def printMessage(self): 
		#print("wow, this actually worked")
		

root = Tk()
gui = Gui(root)
while(True):
	print(gui.forSelf)
	root.update() 
	
root.mainloop()
   
