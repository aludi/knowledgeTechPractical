import tkinter as tk
from tkinter import *


class Gui: 
	
	def __init__(self, master): 
		
		#TkInter for interface : link for tutorial :  https://www.python-course.eu/tkinter_labels.php
		w = Label(root, font = "Times 16 bold", fg = "black", text = "Hello\n I will help you with selecting a boardgame!")
		pic = PhotoImage(file = "img/scaryOwl1.gif") #must always be a gif, thinter doesn't like other formats.
		w1 = Label(root, image = pic)
		w1.image = pic
		w1.pack(side = "right")
		Button(root, text="ok, let's start!").pack(side = "bottom")
		w.pack()
		
		
		#frame = Frame(master)
		#frame.pack()
		
		#self.printButton = Button(frame, text= "Print Message", command=self.printMessage)
		#self.printButton.pack(side=LEFT)
		
		#self.quitButton =  Button(frame, text= "Quit", command = frame.quit)
		#self.quitButton.pack(side=LEFT)
		
	def printMessage(self): 
		print("wow, this actually worked")

root = Tk()
gui = Gui(root)
root.mainloop()
   
