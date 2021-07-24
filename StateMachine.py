from collections import defaultdict

import States
import Transitions

class StateMachine:

	def __init__(self, allStates, allTransitions, initialState = None):
		self.states = None
		self.transitions = None
		if allStates:
			self.states = self.addStates(allStates)
		

		if allTransitions:
			self.transitions = self.addTransitions(allTransitions)

		self.initialState = self.states[initialState]

	def addStates(self, states):
		stateDict = {}
		for state in states:
			stateDict[state] = States.State(state)
		return stateDict

	def addTransitions(self, transitions):
		transitionList = defaultdict(list)
		for transition in transitions:
			transitionType = transition["trigger"]
			transitionSource = transition["source"]
			transitionDest = transition["dest"]

			transitionObj = Transitions.Transition(transitionType)
			transitionObj.setInitialStates(self.addSourceStates(transitionSource))
			transitionObj.setFinalStates(self.addDestStates(transitionDest))

			for source in transitionObj.getInitialStates():

				transitionList[source].append(transitionObj)
		return transitionList

	def addSourceStates(self, transitionSources: list):
		initialStates = []
		for source in transitionSources:
			initialStates.append(self.addSourceStates(source))
		return initialStates

	def addSourceStates(self, transitionSource: str):
		return self.states[transitionSource]

	def addDestStates(self, transitionDest: list):
		finalStates = []
		for dest in transitionDest:
			finalStates.append(self.addDestStates(dest))
		return finalStates

	def addDestStates(self, transitionDest: str):
		return self.states[transitionDest]




