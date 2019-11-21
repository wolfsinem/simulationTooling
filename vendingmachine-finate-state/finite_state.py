import random

class finiteState():
    states = []
    executing_state = {}
    stop = False
    variables = {}
    global_variables = {}

    def __init__(self, state_functions):
        self.states = state_functions
        self.executing_state = {
            "state": self.states[0],
            "state_index": 0
        }

    def end_state(finiteState, item):
        finiteState.stop = True
        finiteState.executing_state = {
            "state": finiteState.states[0],
            "state_index": 0
        }
    
    def set_state(self, state_function):
        index = self._search_function(state_function)
        self.executing_state = {
            "state": self.states[index],
            "state_index": index
        }
    
    def _search_function(self, function):
        for index, state in enumerate(self.states):
            if state == function:
                return index
        raise Exception("Function not found")

    def run(self, alfabet):
        if self.stop:
            return

        item = random.choice(alfabet)
        self.variables = self.executing_state["state"](self, item)
        self.run(alfabet)
        
