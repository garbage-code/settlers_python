#Settlers of Catan
import random
import pygame

def roll():
    dice = random.randint(2, 7) + random.randint(7, 12)

types = ["bread", "sauce", "cheese", "ham", "pepperoni"]
board = [["_", "_", "T", "_", "T", "_", "T", "_", "_"], 
         ["_", "T", "_", "T", "_", "T", "_", "T", "_"], 
         ["T", "_", "T", "_", "T", "_", "T", "_", "T"], 
         ["_", "T", "_", "T", "_", "T", "_", "T", "_"], 
         ["_", "_", "T", "_", "T", "_", "T", "_", "_"]]
 
types = ["bread", "sauce", "cheese", "ham", "pepperoni"]

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
    def __init__(self, name, color, position, resources, development, progress, points, special):
        self.name = name
        self.color = color
        self.position = position
        self.resources = []
        self.development = []
        self.progress = []
        self.points = points
        self.special = []




class Tile:
    def __init__(self, type, trigger):
        self.type = type
        self.trigger = trigger

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


#class Card:
 #   def __init__(self, resource, 


class Tile:


    def __init__(self, type, trigger):
        self.type = type
        self.trigger = trigger
        

# def init():
 #   for i in numplayers:
   #     player + i  = Player(playernames(i), playercolor(i), playerposition(i))
        
playerinput(play())