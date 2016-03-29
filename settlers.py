#Settlers of Catan
import random
import pygame


dice1 = 0
dice2 = 0

def roll():
    global dice1
    global dice2
    dice1 = random.randint(2, 7)
    dice2 = random.randint(7, 12)
    
    
types = ["bread", "sauce", "cheese", "ham", "pepperoni"]
trigger = [dice1, dice2]



def play():
    input1 = input("How Many Players?:   ")
    numplayers = input1
    return str(input1)

numplayers = 0
colors = ['red', 'blue', 'white', 'orange', 'green', 'brown']
playernames = [] 
playercolor = [] 
playerposition = []


           
def playerinput(string):
    global playernames
    global colors
    if int(string) == 1:
        playernames.append(input("Enter Player " + string + " Name:   "))
        m = str(input("Enter Player " + string + " Color (Blue, Red, White, Orange, Green, or Brown):   ")).lower()
        while colors.count(m) != 1 or playercolor.count(m) > 0:
            m = str(input("Enter Player " + string + " Color (Blue, Red, White, Orange, Green, or Brown):   ")).lower()
        playercolor.append(m) 
        playerposition.append(int(string))
    else:
        playernames.append(input("Enter Player " + string + " Name:   "))
        m = str(input("Enter Player " + string + " Color (Blue, Red, White, Orange, Green, or Brown):   ")).lower()
        while colors.count(m) != 1 or playercolor.count(m) > 0:
            m = str(input("Enter Player " + string + " Color (Blue, Red, White, Orange, Green, or Brown):   ")).lower()
        playercolor.append(m) 
        playerposition.append(int(string))
        playerinput(str(int(string) - 1))
        
class Player:
    
    def __init__(self, name, color, position, points = 0):
        self.name = name
        self.color = color
        self.position = position
        self.points = points
        
    #def display():
     #   print(self.name = name, self.color = color, self.position = position, self.points = points)
        
    def isturn(self, turn): #Global turn must be implemented
        if self.position == turn:
            return True
        else:
            return False

    def add_item(self, item):
        self.items[item.name] = item

#class Card:
 #   def __init__(self, resource, 


class Tile:


    def __init__(self, type, trigger):
        self.type = type
        self.trigger = trigger
        

#def init():
 #   for i in numplayers:
   #     player + i  = Player(playernames(i), playercolor(i), playerposition(i))
        
playerinput(play())



"""
class ResourceCard:

    def __init__(self, type):
        self.type = type

class DevelopmentCard:

    devtype = ["delivery", "progress", "pizza"]

    def __init__(self, devtype):
        self.devtype = devtype

class ProgressCard:

    protype = ["road", "extra", "yoink"]

    def __init__(self, protype):
        self.protype = protype
"""