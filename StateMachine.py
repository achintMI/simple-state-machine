from collections import defaultdict

from State import State
from Transition import Transition

class StateMachine:

	def __init__(self, allStates, allTransitions, initialState = None):
		self.states = dict()
		self.transitions = defaultdict(list)
		if allStates:
			self.addStates(allStates)
		
		if allTransitions:
			self.addTransitions(allTransitions)

		self.initialState = self.states[initialState]

	def addStates(self, states):
		for state in states:
			self.states[state] = State(state)

	def addTransitions(self, transitions):
		transitionList = defaultdict(list)
		for transition in transitions:
			transitionType = transition["trigger"]
			transitionSource = transition["source"]
			transitionDest = transition["dest"]

			transitionObj = Transition(transitionType)

			sourcesToAdd = self.addSourceStates(transitionSource)
			destToAdd = self.addSourceStates(transitionDest)

			transitionObj.setInitialStates(sourcesToAdd)
			transitionObj.setFinalStates(destToAdd)

			for source in transitionObj.getInitialStates():
				self.transitions[source].append(transitionObj)

	def addSourceStates(self, transitionSources):
		if type(transitionSources) is str:
			return [self.states[transitionSources]]

		initialStates = []
		for source in transitionSources:
			initialStates = initialStates + self.addSourceStates(source)
		return initialStates

	def addDestStates(self, transitionDest: list):
		if type(transitionDest) is str:
			return [self.states[transitionDest]]

		finalStates = []
		for dest in transitionDest:
			finalStates = finalStates + self.addDestStates(dest)
		return finalStates

	def showStateMachine(self):
		for stateName, state in self.states.items():
			for transition in self.transitions[state]:
				for finalState in transition.getFinalStates():
					print(stateName + f' -> {transition.getTransitionName()} -> ' + finalState.getCurrentStateName())


