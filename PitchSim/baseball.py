import Pitch
import PitchSolver
import pygame
import Delivery

pygame.init()
scr = pygame.display.set_mode((1000,750))
perspective = pygame.image.load("zone.bmp").convert()

#colors
White = (248,248,248)
Black = (0,0,0)
FF = (215,105,115)
SL = (235,235,105)
CH = (105,205,105)
CU = (105,205,235)
SI = (245,175,105)
FC = (165,105,105)
FS = (105,190,190)

skin = (245,220,155)
uniform = (185,185,185)

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

# calculate drawn size of the ball
def ballSize(y):
    return int(401 / ((y / 0.3048) + 19.1))+2

# takes XYZ in Meters to give a pixel location
def zPerspectiveAdjust(y, z):
    return -2483.4 * ((z-1.21) / (y + 19.1)) + 375
def xPerspectiveAdjust(y, x):
    return 2466.7 * (x / (y + 19.1)) + 500

def darken(C, d):
    return(C[0]-d, C[1]-d, C[2]-d)



def drawBackground():
    scr.blit(perspective, (0,0))
    pygame.display.flip()

def drawLine(x1,y1,x2,y2,c):
    pygame.draw.line(scr, c, (x1,y1),(x2,y2), width = 8)

def delayMS(t):
    pygame.time.delay(t)

#drawing pitch and delivery
def drawPD(P, D):
    t = -.017 * D.r
    while(t < 0):
        scr.blit(perspective, (0,0))
        drawDeliveryFrame(D, t)
        pygame.display.flip()
        t = t + .017
        delayMS(17)
    while yPosition(P, t) > 0 :
        x = xPosition(P, t)
        y = yPosition(P, t)
        z = zPosition(P, t)
        xp = xPerspectiveAdjust(y, x)
        zp = zPerspectiveAdjust(y, z)
        b = (ballSize(y)/2)
        scr.blit(perspective, (0,0,0,0))
        pygame.draw.circle(scr, White, (xp,zp), b-1)
        drawDeliveryFrame(D, t)
        pygame.display.flip()
        t = t + .017
        delayMS(17)

def drawDeliveryFrame(D, t):
        coord = []
        B = D.p[D.r - int(t/-.017)]
        i = 0
        while (i < 26):
            coord.append(xPerspectiveAdjust(16.5, -D.xscale*B.b[i]+D.xtrans))
            coord.append(zPerspectiveAdjust(16.5, D.zscale*B.b[i+1]+D.ztrans))
            pygame.draw.circle(scr, uniform, (xPerspectiveAdjust(16.5, -D.xscale*B.b[i]+D.xtrans), zPerspectiveAdjust(16.5, D.zscale*B.b[i+1]+D.ztrans)), 5)
            i = i + 2
        drawLine(coord[2],coord[3],coord[6],coord[7],uniform)
        drawLine(coord[6],coord[7],coord[10],coord[11],uniform)
        drawLine(coord[4],coord[5],coord[8],coord[9],uniform)
        drawLine(coord[8],coord[9],coord[12],coord[13],uniform)
        #drawLine(coord[0],coord[1],coord[2],coord[3],uniform)
        #drawLine(coord[0],coord[1],coord[4],coord[5],uniform)
        drawLine(coord[2],coord[3],coord[4],coord[5],uniform)
        drawLine(coord[2],coord[3],coord[14],coord[15],uniform)
        drawLine(coord[4],coord[5],coord[16],coord[17],uniform)
        drawLine(coord[14],coord[15],coord[16],coord[17],uniform)
        drawLine(coord[14],coord[15],coord[18],coord[19],uniform)
        drawLine(coord[16],coord[17],coord[20],coord[21],uniform)
        drawLine(coord[18],coord[19],coord[22],coord[23],uniform)
        drawLine(coord[20],coord[21],coord[24],coord[25],uniform)

def drawPitchFrame(P, t):
    return

drawBackground()
delayMS(1000)
