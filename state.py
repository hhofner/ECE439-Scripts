class State(object):
    def __init__(self, name):
        self.is_starting_state = False
        self._name = name

        self._logic = []

    def add_logic(self, log):
        """ Add state logic forwarding

        log should be a list of tuples, or just a tuple where
            the first element is the "output" of the state and
            the second element is the "bit read", and the third example
            a string stating what state it forwards to.
            Example: log = [(0b00, 0, "00"), (0b11, 1, "10")]
        """
        if isinstance(log, list):
            for val in log:
                self._logic.append(val)

        else:
            self._logic.append(log)

        # TODO
        self.refresh()

    def process(self, rcvd):
        """Process input depending on logic

        Arguments:
        rcvd: binary 

        Return [ list of new paths and new vals ]
        or `None` if rcvd does not exist in this State
        """
        pvs = []
        for logic in self._logic:
            pvs.append((logic[2], logic[0]^rcvd))

        return pvs

    def set_starting_state(self):
        self.is_starting_state = True

    def set_state_logic(self, f):
        self._logic = f

    def next_state(self, arg):
        return self._logic(arg)

    # TODO: Refresh refreshes some values 
    # That allows me to easily go through....idk
    def refresh(self):
        pass

    @property
    def name(self):
        return self._name

    def __repr__(self):
        rs = "State %s -- " % self._name
        rs += "Starting state: %s" % self.is_starting_state
        return rs
