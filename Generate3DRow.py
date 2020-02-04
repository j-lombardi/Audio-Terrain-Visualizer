from vpython import *
import random
import time

LENGTH = 1
WIDTH = 0.1
HEIGHT = 0.1

#abox1 = box(pos=vector(0, 0.51, 0), length=1, width=1, height=1)
#abox2 = box(pos=vector(-4.5, 0.51, 0), length=1, width=1, height=1)
#abox3 = box(pos=vector(4.5, 0.51, 0), length=1, width=1, height=1)

#scene.userpan = False
#scene.userzoom = False
#scene.userspin = False

flatPlane = box(pos=vector(0, 0, 0), length=10, width=10, height=0, color= color.blue)

def genNewRow():
    row = [0 for x in range(10)]
    #Builds random 10x10 cube map
    for i in range(0, 10):
            h = random.randint(0, 5)
            row[i] = box(pos=vector(-4.5 + (1 * i), h/2, 0), length=1, width=1, height=h, color=color.purple)
    return row


def deleteOldRow(row):
    for i in row:
        i.visible = False
        del i


def shiftRow(row):
    for i in row:
        i.pos.z -= 1



cols = [0 for x in range(10)]
for i in range(10):
    row=genNewRow()
    cols[i] = row

for i in range(10):
    for z in range(0, i):
        shiftRow(cols[z])
    time.sleep(1)