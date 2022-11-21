import Pitch
import math

def xVelocity(P, t):
    return P.xV0 + (P.xA0 * t)
def xPosition(P, t):
    return P.xP0 + (P.xV0 * t) + (0.5 * P.xA0 * t * t)

def yVelocity(P, t):
    return P.yV0 + (P.yA0 * t)
def yPosition(P, t):
    return P.yP0 + (P.yV0 * t) + (0.5 * P.yA0 * t * t)

def zVelocity(P, t):
    return P.zV0 + (P.zA0 * t)
def zPosition(P, t):
    return P.zP0 + (P.zV0 * t) + (0.5 * P.zA0 * t * t)

def timeToPlate(P):
    x = 0.0000
    while yPosition(P, x) > 0:
        x = x + .001
    return x

def pitchMoveH(P):
    p = Pitch.Pitch("Test", P.xP0, P.yP0, P.zP0, P.xV0, P.yV0, P.zV0, 0, P.yA0, P.zA0)
    t = timeToPlate(P)
    print(xPosition(P, t))
    print(xPosition(p, t))
    return (xPosition(P, t) - xPosition(p, t)) * 39.37

def pitchMoveV(P):
    p = Pitch.Pitch("test", "test", P.pitchVelo, P.xForce, P.yForce, P.zForce, 100, 100, 100, P.pitchVelo, 0, 0, .145)
    t = timeToPlate(P)

    return -(zPosition(p, 0) - zPosition(p, t)) * 39.37
