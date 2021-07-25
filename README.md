# simple-state-machine
A simple State Machine in python

##### states require an array of string: s1, s2, s3... is the name of the states
states = ["s1", "s2", "s3", "s4", "s5", "s6", "s7"]

##### transition require an array of dictionary
###### trigger is the transition
###### source: can be a state or an array of states
###### destination: can be state or an array of states
###### given a source(s) state with transtition(trigger) goes to dest state.
transitions = [
	{"trigger": "t1", "source": "s1", "dest": "s2"},
	{"trigger": "t2", "source": "s1", "dest": "s3"},
	{"trigger": "t3", "source": ["s2", "s3"], "dest": "s4"},
	{"trigger": "t4", "source": "s3", "dest": "s5"},
	{"trigger": "t5", "source": "s4", "dest": "s6"},
	{"trigger": "t6", "source": "s5", "dest": "s7"},
]

##### machine initialize requires 3 params: list of states, transition list, and start State
machine = StateMachine.StateMachine(states, transitions, "s1")

###### print state machine
machine.showStateMachine()

##### Add transition to the existing machine
machine.addTransitions([{"trigger": "t7", "source": "s3", "dest": "s5"}])
print("Machine Transition Add:")
machine.showStateMachine()

##### add state to the existing machine
machine.addStates(["s8"])
machine.addTransitions([{"trigger": "t9", "source": "s4", "dest": "s8"}])
machine.addTransitions([{"trigger": "t10", "source": "s8", "dest": "s6"}])
machine.showStateMachine()
