from state import State

class Trellis(object):
	def __init__(self, states):
		self._states = {}
		for state in states:
			self._states[state.name] = state

		self.set_up = False

	def set_up(self):
		# Can only set up once
		if self.set_up:
			return

		self._trell_vals = {}
		for i in self._states:
			if self._states[i].is_starting_state:
				self._trell_vals[self._states[i].name] = 0
			else:
				self._trell_vals[self._states[i].name] = None

		self.set_up = True

	def run(self, stream):
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

	t   = Trellis([s00, s01, s10, s11])
	print(t)


if __name__ == "__main__":
	main()
