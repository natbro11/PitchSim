
import random

class Pitch:

    def __init__(self, t, xP, yP, zP, xV, yV, zV, xA, yA, zA):
        self.pitchType = t

        self.xP0 = xP * 0.3048
        self.yP0 = yP * 0.3048
        self.zP0 = zP * 0.3048

        self.xV0 = xV * 0.3048
        self.yV0 = yV * 0.3048
        self.zV0 = zV * 0.3048

        self.xA0 = xA * 0.3048
        self.yA0 = yA * 0.3048
        self.zA0 = zA * 0.3048

    def toString(self):
        print("Pitch Type: " + self.pitchType)
        print("xP0: " + str(self.xP0))
        print("yP0: " + str(self.yP0))
        print("zP0: " + str(self.zP0))
        print("xV0: " + str(self.xV0))
        print("yV0: " + str(self.yV0))
        print("zV0: " + str(self.zV0))
        print("xA0: " + str(self.xA0))
        print("yA0: " + str(self.yA0))
        print("zA0: " + str(self.zA0))




#test pitches

L1 = Pitch("FF",-1.8,53.8,5.3,5.0,-137.1,-4.0,-10.5,30.6,-15.5)
L2 = Pitch("FC",-1.9,53.9,5.4,5.0,-131.3,-4.0,1.0,26.2,-23.3)
L3 = Pitch("SL",-1.8,53.8,5.4,5.0,-121.6,-4.0,5.5,21.9,-32.7)
L4 = Pitch("CH",-2.0,53.7,5.2,5.0,-121.1,-4.0,-12.4,22.3,-26.8)

C1 = Pitch("FS",-2.2,55.1,5.4,6.0,-123.4,-1.5,-11.8,24.7,-32.8)
C2 = Pitch("FF",-2.0,55.1,5.5,6.0,-133.3,-1.5,-10.0,27.4,-19.6)
C3 = Pitch("FC",-2.0,55.2,5.5,6.0,-122.8,-1.5,1.4,22.0,-29.2)
C4 = Pitch("CU",-2.0,55.3,5.4,0.0,-114.5,-1.5,13.6,22.5,-35.5)

W1 = Pitch("FF",-1.8,52.9,5.4,7.0,-136.5,-3.0,-14.4,30.9,-14.1)
W2 = Pitch("CH",-2.1,53.2,5.2,7.0,-121.2,-0.0,-17.1,25.1,-34.5)
W3 = Pitch("FC",-2.0,53.0,5.4,7.0,-126.5,-3.0,2.1,25.0,-23.9)

F1 = Pitch("FF",-0.3,53.9,7.0,0.0,-143.8,-8.0,-0.2,34.6,-6.2)
F2 = Pitch("SL",-0.2,54.0,7.1,0.0,-125.2,-8.0,1.8,25.0,-37.2)
