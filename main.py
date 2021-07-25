import StateMachine


states = ["s1", "s2", "s3", "s4", "s5", "s6", "s7"]
transitions = [
	{"trigger": "t1", "source": "s1", "dest": "s2"},
	{"trigger": "t2", "source": "s1", "dest": "s3"},
	{"trigger": "t3", "source": ["s2", "s3"], "dest": "s4"},
	{"trigger": "t4", "source": "s3", "dest": "s5"},
	{"trigger": "t5", "source": "s4", "dest": "s6"},
	{"trigger": "t6", "source": "s5", "dest": "s7"},
]
machine = StateMachine.StateMachine(states, transitions, "s1")

print("Machine INIT:")
machine.showStateMachine()

machine.addTransitions([{"trigger": "t7", "source": "s3", "dest": "s5"}])
print("Machine Transition Add:")
machine.showStateMachine()


machine.addStates(["s8"])
machine.addTransitions([{"trigger": "t9", "source": "s4", "dest": "s8"}])
machine.addTransitions([{"trigger": "t10", "source": "s8", "dest": "s6"}])
print("New State and Transition Add:")
machine.showStateMachine()
