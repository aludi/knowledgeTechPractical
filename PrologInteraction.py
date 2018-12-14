from pyswip import Prolog


class PrologInteraction:
	
	#initialization

	def __init__(self):
		self.prolog = Prolog()
		self.kb = self.prolog.consult("startingKB.pl")		#to change so you can select your own file?
		prologRules = self.initPrologRules()
		self.game1 = "some game"
		self.game2 = "some game"
		self.game3 = "some game"
		self.numberOfPlayers = 0
		self.budget = 0
		self.typeGame = 0
		self.coop = 0
		self.camp = 0
		self.minAge = 0
		self.genre = 0
		self.y = 0
		
		
	def initPrologRules(self):
		self.prolog.assertz("numPlay(A,MIN, MAX):- A >= MIN, A =< MAX")  #rule for min/max (budget and players)
		self.prolog.assertz("minimumAge(M, N):- N >= M")   # rule for min age
		self.prolog.assertz("in_list_type(N,X) :- game(N,_,_,_,_,_,_,B,_,_,_,_), member(X, B)") #search by type
		self.prolog.assertz("in_list_genre(N,X) :- game(N,_,_,_,_,_,_,_,_,_,_,B), member(X, B)") #search by genre

	
	# some getters
	
	def getAllProperties(self, nameOfGame):
		print("am in here")
		x = self.prolog.query('''game({},MinP, MaxP, RecP, Time, Minage, Complexity, T, C, CO, CA, Listgenre)'''.format(nameOfGame))
		for soln in x:
			print(soln["MinP"], soln["MaxP"], soln["Time"], soln["Minage"], soln["Complexity"], soln["T"], soln["Listgenre"])
		
	def getAverageComplexity(self, listGame):
		compAv = 0
		comp = 0
		print(listGame)
		for y in listGame:
			print(y)
			x = self.prolog.query('''game({},_,_, _, _, _, Complexity, _,_, _,_, _)'''.format(y))
			for soln in x:
				comp = soln["Complexity"]
				print(comp)
			compAv = compAv + comp
		print("the average complexity of the three games is... ", compAv/len(listGame))
		return(compAv/len(listGame))
		
	def getGenres
		

	#getters for GUI initialization
	def getNamesGamesForGUI(self):		# this function queries for the name of every game and puts it in a list
		gamesList = []
		x = self.prolog.query('''game(X,_,_, _, _, _, _, _,_, _,_, _)''')
		for soln in x:
			gamesList.append(soln["X"])
		return gamesList
		
	def getTypesForGUI(self):					# this function queries for every unique type of game and puts it in the list
		typesList = []
		x = self.prolog.query('''game(_,_,_,_, _, _, _, T,_, _,_, _)''')
		for soln in x:
			if isinstance(soln["T"],(list,)):
				for i in soln["T"]:
					sol = str(i)
			if sol not in typesList:
				typesList.append(sol)
		print(typesList)
		return typesList
	
	def getGenresForGUI(self):
		genresList = []
		x = self.prolog.query('''game(_,_,_,_, _, _, _,_,_, _,_, G)''')
		for soln in x:
			if isinstance(soln["G"],(list,)):
				for i in soln["G"]:
					sol = str(i)
			if sol not in genresList:
				genresList.append(sol)
		print(genresList)
		return genresList
		
	
	
	#some setters
	
	def setNumPlay(self, numPlay):
		print(numPlay)
		self.numberOfPlayers = numPlay
		print(self.numberOfPlayers)
	
	def setGame1(self, game):
		print(game)
		self.game1 = game
		print(self.game1)
	def setGame2(self, game):
		print(game)
		self.game2 = game
		print(self.game2)
	def setGame3(self, game):
		print(game)
		self.game3 = game
		print(self.game3)
	
	def setBudget(self, budgetVal):
		self.budget = budgetVal #to implement: range of budgets
		
	def setType(self, typeGameSel):
		self.typeGame = typeGameSel
		
	def setCoop(self, CoopTF):
		self.coop = CoopTF
	
	def setCamp(self, CampTF):
		self.camp = CampTF
		
	def setMinAge(self, minAgeSet):
		self.minAge = minAgeSet
	
	def setGenre(self, genreSet):
		self.genre = genreSet
		
		
	# assorted other functions
	
	

	def makeListOfGames(self):
		return [self.game1, self.game2, self.game3]
		
	# queries
	
	def searchGameByAverageComplexity(self, avComp, prolog):
		# TODO: finetune range complexity, for now it's ±5
		stringQuery = '''
		A is {},
		game(Name, _,_, _, _, _, C,_, _, _, _, _),
		C =< A + 0.5,
		C >= A - 0.5'''.format(avComp)
		self.y = self.prolog.query(stringQuery)
		x= 0
		for soln in self.y:
			print("you can play:", (soln["Name"], soln['C']))
			x = 1
		if x == 0:
			print("sorry, we couldn't find any games for you")	
			
	def searchGameByType(self, prolog):			# selects all games with a certain type
		x = 0
		typeGame = self.typeGame
		print(typeGame)
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
		print(genre)
		q = '''T = {}, in_list_genre(A,T)'''.format(genre)
		self.y = prolog.query(q)
		for soln in self.y:
			print("you can play:", (soln['A']))
			x = 1
		if x == 0:
			print("sorry, we couldn't find any games for you")	
		
		
	def stringQuery(self, prolog):
		stringQuery ='''
		A is {},
		M = {},
		B = {},
		T = {}, 
		CO = {},
		CA = {},
		game(Name, MinP, MaxP, RecP, Time, Minage, Complexity, T, C, CO, CA, Listgenre),
		C < B,
		numPlay(A, MinP, MaxP), 
        minimumAge(M, Minage)'''.format(self.numberOfPlayers, self.minAge, self.budget, self.typeGame, self.coop, self.camp)
		print(self.numberOfPlayers, self.minAge, self.budget, self.typeGame, self.coop, self.camp)
		self.y = prolog.query(stringQuery)



#game(name, min players, max players, time, min age, complexity, type, budget, cooperativeTF, campaignTF, Listgenre)
	def printSol(self):
		x= 0
		for soln in self.y:
			print("you can play:", (soln["Name"]))
			x = 1
		if x == 0:
			print("sorry, we couldn't find any games for you")	
