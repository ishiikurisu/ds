class StateMachine:
    def __init__(self, states=[], start=None, transitions={}):
        self.states = states
        self.transitions = transitions
        self.state = start

    def add_transition(self, transition: dict):
        trigger = transition['trigger']
        if trigger not in self.transitions:
            self.transitions[trigger] = []
        self.transitions[trigger].append(transition)

    def trigger(self, action: str) -> bool:
        triggered = False
        transitions = self.transitions[action]
        target = None
        side_effect = None

        for transition in transitions:
            if transition['from'] == self.state:
                target = transition['to']
                side_effect = transition['fx'] if 'fx' in transition else None

        if target:
            self.state = target
            triggered = True
            side_effect()

        return triggered
