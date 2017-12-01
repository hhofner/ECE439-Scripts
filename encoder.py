"""
encoder.py

encodes an image file into a list of bits (bit stream)
"""
import sys

script, img = sys.argv

##############################
# Somehow get bits from img ##
##############################

class Encoder:
    def get_image_bits(self, img):
        ##############################
        # Somehow get bits from img ##
        ##############################
        pass

    def __init__(self, img):
        self.image_bits = get_image_bits(img)
        self.parity_equations_set = False

    def set_parity_equations(self, parity_eq, window):
        """ 
        args:
        parity_eq = list of list. example: [[0,1,1], [1,1,0]]
        window    = window for encoding bits
        """
        ####################
        # Do stuff ########
        ###################
        self.parity_equations_set = True
        pass

    def encode(self):
        pass

def main():
    print("Calling main")

if __name__ == "__main__":
    main()
