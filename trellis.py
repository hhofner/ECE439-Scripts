from state import State

import random
import copy

class Path(object):
    """Class to keep track of possible paths and their values
    
    This is almost a direct implementation of MIT's Convolutional Coding (Lecture 9)
    on how to decode with a trellis. This class holds a list that contains a particular
    path through the Trellis and an associated value for that path that tells you how 
    probable the path was. It utilizes a hamming distance.
    """ 
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
    """ Class to represent a trellis depending on a user-specified state machine.

    This trellis class is a almost direct implementation of MIT's lecture notes on how
    to decode convolutional codes (Lecture 9). This class should contain State objects
    that describe the State Machine. Using run(bit_stream) will decode the message based 
    on the state machine described through the State objects. 

    Methods:
    run(bit_stream) -- return a list with the decoded bit stream
    set_up()        -- "sets up" the trellis

    To properly set up a trellis, one must pass a list of State objects that 
    properly describe the state machine for the encoder. After that, you must run
    "set_up()". To decode a bit stream, pass the bit stream as LIST of ints (the 
    corresponding decimal value) to the "run" function. 
    """
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
        stream -- the encoded message as a list (array) of integers

        Return:
        mssg   -- (string): the decoded message based on the trellis (state machine)
            that was set up
        """

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

        
        # Start decoding the path
        final_bit_stream = []
        for i in range(len(final_path.path)):
            temp = final_path.path[i]
            try:
                temp2 = final_path.path[i+1]
            except:
                continue
            rb   = self._states[temp].return_bit(temp2)
            final_bit_stream.append(rb)
        return final_bit_stream

    def __repr__(self):
        rs = "States\n"
        for state in self._states.items():
            rs += repr(state) + "\n"
        return rs

def main():
    """ Sample Trellis set up. """

    # Create State objects. 
    s00 = State("00")
    s00.set_starting_state()
    
    # Input to `add_logic`: [ (output, bit_read, next_state), (output2, bit_read2, next_state2), ..]
    s00.add_logic([(0b00, 0, "00"), (0b11, 1, "10")])

    s01 = State("10")
    s01.add_logic([(0b00, 1, "11"), (0b11, 0, "01")])

    s10 = State("01")
    s10.add_logic([(0b10, 0, "00"), (0b01, 1, "10")])

    s11 = State("11")
    s11.add_logic([(0b10, 1, "11"), (0b01, 0, "01")])

    # Create Trellis Object passing the State Objects 
    t = Trellis([s00, s01, s10, s11])

    # Set up the Trellis
    t.set_up()


    """
    This is the test input taken from  the MIT Lecture on Convolutional Codes
    The input is a LIST (array) of the binary digits. 
    """
    tst = [0b11, 0b10, 0b11, 0b00, 0b01, 0b10]

    # Call `run` and passing `tst` list
    print(t.run(tst))

if __name__ == "__main__":
    main()
