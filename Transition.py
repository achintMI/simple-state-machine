from State import State

class Transition:
	def __init__(self, name):
		self.__name = name
		self.__intialStates = None
		self.__finalStates = None

	def getTransitionName(self):
		return self.__name

	def getInitialStates(self):
		return self.__intialStates

	def getFinalStates(self):
		return self.__finalStates

	def setFinalStates(self, finalState):
		self.__finalStates = finalState

	def setInitialStates(self, initialStates):
		self.__intialStates = initialStates
