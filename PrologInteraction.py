from pyswip import Prolog


class PrologInteraction:
	
	#initialization

	def __init__(self):
		self.prolog = Prolog()
		self.kb = self.prolog.consult('startingKB.pl')		#to change so you can select your own file?
		prologRules = self.initPrologRules()
		self.game1 = "some game"
		self.game2 = "some game"
		self.game3 = "some game"

		self.numberOfPlayers = "_"
		self.budget = "_"
		self.typeGame = "_"
		self.coop = "_"
		self.camp = "_"
		self.minAge = "_"
		self.genre = "_"
		self.y = "_"
		self.complexity = "_"

		self.minTime = "_"
		self.maxTime = "_"
		self.listType = []

		
	def initPrologRules(self):
		self.prolog.assertz("numPlay(A,MIN, MAX):- A >= MIN, A =< MAX")  #rule for min/max (budget and players)
		self.prolog.assertz("minimumAge(M, N):- N >= M")   # rule for min age
		self.prolog.assertz("in_list_type(N,X) :- game(N,_,_,_,_,_,_,_,B,_,_,_,_), member(X, B)") #search by type
		self.prolog.assertz("in_list_genre(N,X) :- game(N,_,_,_,_,_,_,_,_,_,_,_,B), member(X, B)") #search by genre

	
	# some getters
	def getSelfY(self):
		#returns list of final games in prolog wrapper
		return self.y
	
	def getAllProperties(self, nameOfGame):
		print("am in here")
		x = self.prolog.query('''game({},MinP, MaxP, RecP, Mintime, Maxtime, Minage, Complexity, T, C, CO, CA, Listgenre)'''.format(nameOfGame))
		for soln in x:
			print(soln["MinP"], soln["MaxP"], soln["Mintime"], soln["Maxtime"], soln["Minage"], soln["Complexity"], soln["T"], soln["Listgenre"])
		
	def getAverageComplexity(self, listGame):
		compAv = 0
		comp = 0
		if listGame[0] == '':
			self.complexity = 2.5
		else:
			for y in listGame:
				print("y IN AVERAGE COMPLEXITY", type(y))
				x = self.prolog.query('''game("{}",_,_, _, _, _, _, Complexity, _,_, _,_, _)'''.format(y))
				query = '''game("{}",_,_, _, _, _, _, Complexity, _,_, _,_, _)'''.format(y)
				print(query)
				print("x IN AVERAGE COMPLEXITY", type(x))
				for soln in x:
					comp = soln["Complexity"]
				compAv = compAv + comp
			self.complexity = compAv/len(listGame)
		print("the average complexity of the three games is... ", self.complexity)
		return(compAv/len(listGame))
		


	#getters for GUI initialization
	def getNamesGamesForGUI(self):		# this function queries for the name of every game and puts it in a list
		gamesList = []
		x = self.prolog.query('''game(X,_,_, _, _, _, _, _, _,_, _,_, _)''')
		for soln in x:
			gamesList.append(soln["X"])
		return gamesList
		
	def getListsForGUI(self, typeOrGenre, resultQ):
		listForGUI = []
		for soln in resultQ:
			if isinstance(soln[typeOrGenre],(list,)):
				for i in soln[typeOrGenre]:
					sol = i.decode()
			if sol not in listForGUI:
				listForGUI.append(sol)
		return listForGUI
	
	def getTypesForGUI(self):					# this function queries for every unique type of game and puts it in the list
		x = self.prolog.query('''game(_,_,_,_, _, _, _, _, T,_, _,_, _)''')
		typesList = self.getListsForGUI("T", x)
		return typesList
	
	def getGenresForGUI(self):
		x = self.prolog.query('''game(_,_,_,_, _, _, _, _,_,_, _,_, G)''')
		genresList = self.getListsForGUI("G", x)
		return genresList
		
	
		
	
	
	#some setters
	
	def setNumPlay(self, numPlay):
		self.numberOfPlayers = numPlay
	
	def setGame1(self, game):
		self.game1 = game
		
	def setGame2(self, game):
		self.game2 = game
		
	def setGame3(self, game):
		self.game3 = game
		
	def setBudget(self, budgetVal):
		self.budget = budgetVal #to implement: range of budgets
		
	def setType(self, typeGameSel):
		self.typeGame = typeGameSel
		
	def setTime(self, time):
		self.time= time
		
	def setCoop(self, CoopTF):
		self.coop = CoopTF
	
	def setCamp(self, CampTF):
		self.camp = CampTF
		
	def setMinAge(self, minAgeSet):
		self.minAge = minAgeSet
	
	def setGenre(self, genreSet):
		self.genre = genreSet
		
	def setAvComplexity(self, avCom):
		self.complexity = avCom
		
		
	# assorted other functions
	
	

	def makeListOfGames(self):
		return [self.game1, self.game2, self.game3]
		
	# queries
	
	def searchGameByType(self, prolog):			# selects all games with a certain type
		x = 0
		typeGame = self.typeGame
		q = '''T = {}, in_list_type(A,T)'''.format(typeGame)
		self.y = prolog.query(q)
		for soln in self.y:
			print("you can play:", (soln['A']))
			x = 1
		if x == 0:
			print("sorry, we couldn't find any games for you")	
			
	def searchGameByGenre(self, prolog):			# selects all games with a certain type
		x = 0
		genre = self.genre
		q = '''T = {}, in_list_genre(A,T)'''.format(genre)
		self.y = prolog.query(q)
		for soln in self.y:
			print("you can play:", (soln['A']))
			x = 1
		if x == 0:
			print("sorry, we couldn't find any games for you")	
		
		
	def stringQuery(self, prolog):	# to add, checkbox types - multiple queries
		
		
		# to implement: for object in self.listTypes:
			# call stringQuery where self.type = object
		stringQuery ='''
		NUMBEROFPLAYERS = {},
		MINAGE = {},
		BUDGET = {},
		TYPE = {},
		MINTIME = {},
		MAXTIME = {},
		in_list_type(Name, TYPE),
		CO = {},
		CA = {},
		AVERAGECOMPLEXITY = {},
		game(Name, MinP, MaxP, NUMBEROFPLAYERS, Mintime, Maxtime, Minage, Complexity,_, COST, CO, CA, Listgenre),
		COST < BUDGET,
		Time < TIME,
        minimumAge(MINAGE, Minage),
        Complexity =< AVERAGECOMPLEXITY + 1,
		Complexity >= AVERAGECOMPLEXITY - 1'''.format(self.numberOfPlayers, self.minAge, self.budget, self.typeGame,self.minTime, self.maxTime, self.coop, self.camp, self.complexity)
		self.y = prolog.query(stringQuery)
		print(self.numberOfPlayers, self.minAge, self.budget,self.typeGame, self.coop, self.camp,self.complexity )
		

#: time, time is smaller or equal to = tijd aangegeven + 50% van tijd aangegeven. TIME NOW HAS RANGE
# 
#
#game(name, min players, max players, minTime, maxTime, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)
	
	
	def printSol(self):		# prints and creates list
		listFinal = []
		x= 0
		for soln in self.y:
			print(soln["Name"])
			if soln["Name"] not in listFinal:
				listFinal.append(soln["Name"])
			x = 1
		if x == 0:
			t = "Sorry, we couldn't find any games for you"
			print(t)
			listFinal.append(str(t))
		print(listFinal)
		return listFinal
