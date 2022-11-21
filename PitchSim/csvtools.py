
import csv
import Pitch
import baseball
import Body
import Delivery

filename = "CSV/baileyober.csv"
delivery = "CSV/Delivery/baileyoberwindup.csv"

# initializing the titles and rows list
fields = []
rows = []

def encodeDelivery():
    P = []
    line = next(csvreader)
    E = int(float(line[0])-1)
    for x in range(E):
        P.append(encodePosition())
    return Delivery.Delivery(P,int(float(line[1])),float(line[3]),float(line[4]),float(line[5]),float(line[6]))

def encodePosition():
    fields = next(csvreader)
    return Body.Body(((float(fields[0])),(float(fields[1])),(float(fields[2])),(float(fields[3])),(float(fields[4])),(float(fields[5])),(float(fields[6])),(float(fields[7])),(float(fields[8])),(float(fields[9])),(float(fields[10])),(float(fields[11])),(float(fields[12])),(float(fields[13])),(float(fields[14])),(float(fields[15])),(float(fields[16])),(float(fields[17])),(float(fields[18])),(float(fields[19])),(float(fields[20])),(float(fields[21])),(float(fields[22])),(float(fields[23])),(float(fields[24])),(float(fields[25]))))



with open(delivery, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    a = encodeDelivery()

with open(filename, 'r') as csvfile:
    pitch = csv.reader(csvfile)
    fields = next(pitch)
    for x in range(2200):
        p = next(pitch)
        #if(p[2]=="FF"):
        P = Pitch.Pitch(p[2],float(p[3]),float(p[4]),float(p[5]),float(p[6]),float(p[7]),float(p[8]),float(p[9]),float(p[10]),float(p[11]))
        baseball.drawPD(P, a)
