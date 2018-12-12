from pyswip import Prolog

class PrologInteraction:
	
	#initialization
	
	def __init__(self):
		self.prolog = Prolog()
		self.kb = self.prolog.consult("startingKB.pl")		#to change so you can select your own file?
		prologRules = self.initPrologRules()
		self.game1 = "some game"
		self.numberOfPlayers = 0
		self.budget = 0
		self.typeGame = 0
		self.coop = 0
		self.camp = 0
		self.minAge = 0
		self.y = 0
		print(self.minAge)
		
	def initPrologRules(self):
		self.prolog.assertz("numPlay(A,MIN, MAX):- A >= MIN, A =< MAX")  #rule for min/max (budget and players)
		self.prolog.assertz("minimumAge(M, N):- N >= M")   # rule for min age
	
	# some getters
	
	def getAllProperties(self, nameOfGame):
		print("am in here")
		x = self.prolog.query('''game({},MinP, MaxP, Time, Minage, Complexity, T, C, CO, CA, Listgenre)'''.format(nameOfGame))
		for soln in x:
			print(soln["MinP"], soln["MaxP"], soln["Time"], soln["Minage"], soln["Complexity"], soln["T"], soln["Listgenre"])
		
	def getAverageComplexity(self, listGame):
		compAv = 0
		for y in listGame:
			x = self.prolog.query('''game({},_, _, _, _, Complexity, _,_, _,_, _)'''.format(y))
			for soln in x:
				comp = soln["Complexity"]
			compAv = compAv + comp
		print("the average complexity of the three games is... ", compAv/len(listGame))
		return(compAv/len(listGame))
		

	#some setters
	
	def setNumPlay(self, numPlay):
		print(numPlay)
		self.numberOfPlayers = numPlay
		print(self.numberOfPlayers)
	
	def setGame1(self, game):
		print(game)
		self.game1 = game
		print(self.game1)
	
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
		
		
	# assorted other functions
		
		
	def searchGameByAverageComplexity(self, avComp, prolog):
		# TODO: finetune range complexity, for now it's ±5
		stringQuery = '''
		A is {},
		game(Name, _, _, _, _, C,_, _, _, _, _),
		C =< A + 0.5,
		C >= A - 0.5.'''.format(avComp)
		self.y = self.prolog.query(stringQuery)
		x= 0
		for soln in self.y:
			print("you can play:", (soln["Name"], soln['C']))
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
		game(Name, MinP, MaxP, Time, Minage, Complexity, T, C, CO, CA, Listgenre),
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
