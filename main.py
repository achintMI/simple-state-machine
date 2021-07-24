import StateMachine


states = ["s1", "s2", "s3", "s4"]
transitions = [
	{"trigger": "t1", "source": "s1", "dest": "s2"},
	{"trigger": "t2", "source": "s1", "dest": "s3"},
	{"trigger": "t3", "source": "s2", "dest": "s4"},
	{"trigger": "t4", "source": "s3", "dest": "s4"},
]
machine = StateMachine.StateMachine(states, transitions, "s1")