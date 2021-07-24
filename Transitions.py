import States

class Transition:
	def __init__(self, name):
		self.__name = name
		self.__intialStates = None
		self.__finalStates = None

	def getTransitionName(self):
		return self.__name

	def getInitialStates(self):
		return self.__intialStates

	def finalState(self):
		return self.finalStates

	def setFinalStates(self, finalStates: list):
		self.__finalState = finalStates

	def setInitialStates(self, initialStates: list):
		self.__intialStates = initialStates

	def setInitialStates(self, initialState: States.State):
		self.__intialStates = [initialState]
