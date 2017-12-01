from state import State

import random
import copy

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

    def __repr__(self):
        s = ''
        for p in self._path:
            s += (p + ' ')
        s += '// Value: '
        s += str(self._val)
        return s

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

        # INPUT: LIST OF BITS
        # I'm assumming that `stream` is a list of input bits

        for rcvd in stream:
            temp = []
            # Get latest path from each path object
            for path in self.paths:
                # Call function `process` from previous state object
                rt = self._states[path.prev].process(rcvd)
                if rt != None:
                    if len(rt) > 1:
                        for j in range(1,len(rt)):
                            x = copy.deepcopy(path)
                            x.add_path(rt[j][0])
                            x.add_val(rt[j][1])
                            temp.append(x)
                    path.add_path(rt[0][0])
                    path.add_val(rt[0][1])
            self.paths = self.paths + temp

        final_path = None 
        temp_val = 10000 # Arbitrary
        for p in self.paths:
            if p.val < temp_val:
                temp_val = p.val
                final_path = p

        #print(final_path)
        
        # Start decoding the path
        final_bit_stream = []
        for i in range(len(final_path.path)):
            temp = final_path.path[i]
            try:
                temp2 = final_path.path[i+1]
            except:
                continue
            #print("Processing for %s -> %s" % (temp, temp2))
            #raw_input("Next?")
            rb   = self._states[temp].return_bit(temp2)
            final_bit_stream.append(rb)
        return final_bit_stream

    def __repr__(self):
        rs = "States\n"
        for state in self._states.items():
            rs += repr(state) + "\n"
        return rs

def main():
    """
    Set up your trellis here! 
    """
    s00 = State("00")
    s00.set_starting_state()
    s00.add_logic([(0b00, 0, "00"), (0b11, 1, "10")])

    s01 = State("10")
    s01.add_logic([(0b00, 1, "11"), (0b11, 0, "01")])

    s10 = State("01")
    s10.add_logic([(0b10, 0, "00"), (0b01, 1, "10")])

    s11 = State("11")
    s11.add_logic([(0b10, 1, "11"), (0b01, 0, "01")])

    t = Trellis([s00, s01, s10, s11])
#    print(t)

    t.set_up()
#    print(t.paths[0].path)


    """
    This is the test input taken from  the MIT Lecture on Convolutional Codes
    The input is a LIST (array) of the binary digits. 
    """
    tst = [0b11, 0b10, 0b11, 0b00, 0b01, 0b10]
#    tst = []
    print(t.run(tst))

if __name__ == "__main__":
    main()
