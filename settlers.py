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



def play():
    input1 = input("How Many Players?:   ")
    return input1

playernames = [] 
           
def playerinput(string):
    global playernames
    if int(string) == 1:
        playernames.append(input("Enter Player " + string + " Name:   "))
    else:
        playernames.append(input("Enter Player " + string + " Name:   "))
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

"""       
    def isturn(self, turn): #Global turn must be implemented
        if self.position == turn:
            return True
        else:
            return False
"""


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