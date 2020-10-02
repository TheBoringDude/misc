# a simple decoder for a Ceramic Disc Capacitor

class CeramicDiscCapacitor:
    def __init__(self, numcode):
        self.numcode = numcode
        self.significant = int(str(numcode)[:2]) # get the first 2 significant value
        self.multiplier = int(str(numcode)[2]) # get the multiplier value
        self.uF = 0
        self.pF = 0

    def Decode(self):
        # get and set the values
        self.get_pF()
        self.get_uF()

        # print the output
        print("\n\t  pF =", self.pF)
        print("\n\t  uF =", self.uF)

    # calculate the pF
    def get_pF(self):
        zeros = '0' * self.multiplier
        self.pF = int(str(self.significant) + zeros)

    # calculate the uF
    def get_uF(self):
        self.uF = self.pF / 1000000

if __name__ == "__main__":
    # loop it so that it will not exit after decoding one problem
    while True:
        print("\n\n\t==========| Ceramic Disc Capacitor (Decoder) |==========")
        numCode = input("\n\tNumber Code ~:> ")

        main = CeramicDiscCapacitor(numCode)

        main.Decode()
