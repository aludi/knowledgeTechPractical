class Gui:
	
	import tkinter as tk
	from tkinter import * 
	
	def __init__(self): 
		forSelf = True 
		game1 = None 
		game2 = None
		game3 = None
		
	
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
	tk.Radiobutton(frame1, text="For me", padx = 20, variable=forSelf, value=True).pack(anchor=tk.W)
	tk.Radiobutton(frame1, text="For someone else", padx = 20, variable=forSelf, value=False).pack(anchor=tk.W)
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
