import random
import os
import sys

clear = lambda: os.system('cls')

class Star:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1
    def move(self):
        dx = 0
        dy = 0
        i = int(input("Direction: "))
        if(i == 8):
            dx = 0
            dy = -1
        elif(i == 2):
            dx = 0
            dy = 1
        if(i == 4):
            dx = -1
            dy = 0
        if(i == 6):
            dx = 1
            dy = 0
        self.x += self.speed * dx
        self.y += self.speed * dy
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Arena:
    def __init__(self,w,h,star,cop):
        self.w = w
        self.h = h
        self.star = star
        self.cop = cop
    def draw(self):
        for i in range(self.h):
            for j in range(self.w):
                if(i == 0 or i == self.h-1):
                    print("* ",end = "")
                else:
                    if(j == 0 or j == self.w-1):
                        print("* " , end = "")
                    else:
                        print("  ", end = "")
            print()
    def drawWithPlayer(self):
        for i in range(self.h):
            for j in range(self.w):
                if(i == 0 or i == self.h-1):
                    print("# ",end = "")
                elif(self.star.getX() == j and self.star.getY() == i):
                    print("* ",end = "")
                elif(self.cop.getX() == j and self.cop.getY() == i):
                    print("& ",end = "")
                else:
                    if(j == 0 or j == self.w-1):
                        print("# " , end = "")
                    else:
                        print("  ", end = "")
            print()
    def checkPlayerPlace(self):
        if(self.star.getX() == self.cop.getX() and self.star.getY() == self.cop.getY()):
            print("You get caught")
            sys.exit(0)
        if(self.star.getX() <= 0 or self.star.getX() >= self.w-1 or self.star.getY() <= 0 or self.star.getY() >= self.h-1):
            print("You died")
            sys.exit(0)
def check(x):
    if(x < 0):
        return 1
    elif(x > 0):
        return -1
    else:
        return 0
class Cop:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1
    def move(self,x,y):
        dx = check(self.x - x)
        #dy = 0
        dy = check(self.y - y)
        
        self.x += self.speed * dx
        self.y += self.speed * dy
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    

W,H = 30,30
player = Star(random.randrange(1,H-2),random.randrange(1,H-2))
cop = Cop(random.randrange(1,H-2),random.randrange(1,H-2))
arena = Arena(W,H,player,cop)

running = True
while(running):
    clear()
    arena.drawWithPlayer()
    player.move()
    cop.move(player.getX(),player.getY())
    arena.checkPlayerPlace()
    clear()
