import bisect


class DFA(object):
    def __init__(self, start_state):
        self.start_state = start_state
        self.transitions = {}
        self.defaults = {}
        self.final_states = set()

    def add_transition(self, src, input_word, dest) -> None:
        self.transitions.setdefault(src, {})[input_word] = dest

    def set_default_transition(self, src, dest) -> None:
        self.defaults[src] = dest

    def add_final_state(self, state) -> None:
        self.final_states.add(state)

    def is_final(self, state) -> bool:
        return state in self.final_states

    def next_state(self, src, input_word) -> set:
        state_transitions = self.transitions.get(src, {})
        return state_transitions.get(input_word, self.defaults.get(src, None))

    def next_valid_string(self, input_word) -> tuple:
        state = self.start_state
        stack = []

        state = self.__evaluate_dfa(input_word, stack, state)

        if self.is_final(state):
            return input_word

        return self.__find_smallest_state(stack)

    def __find_next_edge(self, s, x):
        if x is None:
            x = u'\0'
        else:
            x = chr(ord(x) + 1)
        state_transitions = self.transitions.get(s, {})
        if x in state_transitions or s in self.defaults:
            return x
        labels = sorted(state_transitions.keys())
        pos = bisect.bisect_left(labels, x)
        if pos < len(labels):
            return labels[pos]
        return None

    def __evaluate_dfa(self, input_word, stack, start_state) -> set:
        state = start_state
        for i, x in enumerate(input_word):
            stack.append((input_word[:i], state, x))
            state = self.next_state(state, x)
            if not state:
                break
        else:
            stack.append((input_word[:i + 1], state, None))
        return state

    def __find_smallest_state(self, stack: list) -> tuple | None:
        while len(stack) > 0:
            path, state, x = stack.pop()
            x = self.__find_next_edge(state, x)
            if x:
                path += x
                state = self.next_state(state, x)
                if self.is_final(state):
                    return path
                stack.append((path, state, None))
        return None
