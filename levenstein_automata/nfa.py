from levenstein_automata.dfa import DFA


class NFA(object):
    EPSILON = object()
    ANY = object()

    def __init__(self, start_state):
        self.transitions = {}
        self.final_states = set()
        self._start_state = start_state

    @property
    def start_state(self):
        return frozenset(self._expand({self._start_state}))

    def add_transition(self, src, input_word, dest):
        self.transitions.setdefault(src, {})\
            .setdefault(input_word, set()).add(dest)

    def add_final_state(self, state):
        self.final_states.add(state)

    def is_final(self, states):
        return self.final_states.intersection(states)

    def _expand(self, states):
        frontier = set(states)
        while frontier:
            state = frontier.pop()
            new_states = self.transitions.get(state, {})\
                .get(NFA.EPSILON, set()).difference(states)
            frontier.update(new_states)
            states.update(new_states)
        return states

    def next_state(self, states, input_word):
        dest_states = set()
        for state in states:
            state_transitions = self.transitions.get(state, {})
            dest_states.update(state_transitions.get(input_word, []))
            dest_states.update(state_transitions.get(NFA.ANY, []))
        return frozenset(self._expand(dest_states))

    def get_inputs(self, states):
        inputs = set()
        for state in states:
            inputs.update(self.transitions.get(state, {}).keys())
        return inputs

    def to_dfa(self):
        dfa = DFA(self.start_state)
        frontier = [self.start_state]
        seen = set()
        while len(frontier) > 0:
            current = frontier.pop()
            inputs = self.get_inputs(current)
            for input_word in inputs:
                if input_word == NFA.EPSILON:
                    continue
                new_state = self.next_state(current, input_word)
                if new_state not in seen:
                    frontier.append(new_state)
                    seen.add(new_state)
                    if self.is_final(new_state):
                        dfa.add_final_state(new_state)
                if input_word == NFA.ANY:
                    dfa.set_default_transition(current, new_state)
                else:
                    dfa.add_transition(current, input_word, new_state)
        return dfa
