class State(object):
    def __init__(self, name, fs = []):
        self.is_starting_state = False
        self._fs   = fs
        self._name = name

    def set_starting_state(self):
        self.is_starting_state = True

    def set_state_logic(self, f):
        self._logic = f

    def next_state(self, arg):
            return self._logic(arg)

    @property
    def name(self):
        return self._name

    @property
    def fs(self):
        return self._fs

    def __repr__(self):
        rs = "State %s -- " % self._name
        rs += "Forwarding states: %s, " % self.fs
        rs += "Starting state: %s" % self.is_starting_state
        return rs
