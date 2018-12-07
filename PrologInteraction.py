from pyswip import Prolog

class PrologInteraction:
	
	def __init__(self):
		self.prolog = Prolog()
		self.kb = self.prolog.consult("startingKB.pl")		#to change so you can select your own file?
		prologRules = self.initPrologRules()
		self.numberOfPlayers = 0
		self.budget = 0
		self.typeGame = 0
		self.coop = 0
		self.camp = 0
		self.minAge = 0
		self.y = 0
		print(self.minAge)
		
	def initPrologRules(self):
		#rule for min/max (budget and players)
		self.prolog.assertz("numPlay(A,MIN, MAX):- A >= MIN, A =< MAX")
		# rule for min age
		self.prolog.assertz("minimumAge(M, N):- N >= M")
	
	def setNumPlay(self, numPlay):
		print(numPlay)
		self.numberOfPlayers = numPlay
		print(self.numberOfPlayers)
	
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
