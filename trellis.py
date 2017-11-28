from state import State

import random 

class Path(object):
    def __init__(self):
        self._val = None  # Infinite
        self._path = []

    def add_path(self, path):
        self._path.append(path)

    def add_val(self, val):
        if self._val == None:
            self._val = val + 0
        else:
            self._val += val

    @property
    def prev(self):
        return self._path[-1]

    @property
    def val(self):
        return self._val

    @property
    def path(self):
        return self._path


class Trellis(object):
    def __init__(self, states):
        self._states = {}
        for state in states:
            self._states[state.name] = state

        self._set_up = False

    def set_up(self):
        # Can only set up once
        if self._set_up:
            return

        self.paths = []
        for i in self._states:
            if self._states[i].is_starting_state:
                self.paths.append(Path())
                self.paths[0].add_path(i)

        self._set_up = True

    def run(self, stream):
        """ Run through trellis

        Arguments:
        stream -- (string): the encoded message 

        Return:
        mssg -- (string): the decoded message based on the trellis (state machine)
            that was set up
        """
        
        # Ensure that the state machine makes sense
        # TODO: Loop through states and make sure they make sense (i.e. a state
        #   does not forward to a state that doesn't exist. 

        # Determine how many 'bits' to process
        # Arbitrarily select some state name.
        process_length = len(random.choice(self._states.keys())) 

        if len(stream) / process_length != 0:
            print('Length not nice')
            stream.append('0')

        for i in range(len(stream)):
            pass

    def __repr__(self):
        rs = "States\n"
        for state in self._states.items():
            rs += repr(state) + "\n"
        return rs

def main():
    s00 = State("00", ["01", "00"])
    s00.set_starting_state()
    s00.set_state_logic(lambda x: "00" if x == "0" else "01")

    s01 = State("01", ["10", "11"])
    s01.set_state_logic(lambda x: "10" if x == "0" else "11")

    s10 = State("10", ["11", "10"])
    s10.set_state_logic(lambda x: "11" if x == "0" else "10")

    s11 = State("11", ["00", "01"])
    s11.set_state_logic(lambda x: "00" if x == "0" else "01")

    t = Trellis([s00, s01, s10, s11])
    print(t)

    t.set_up()
    print(t.paths[0].path)

if __name__ == "__main__":
    main()
