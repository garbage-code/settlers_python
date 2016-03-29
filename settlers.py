#Settlers of Catan
import random
import pygame

types = ["bread", "sauce", "cheese", "ham", "pepperoni"]
trigger = [dice1, dice2]



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
    
    def __init__(self, name, color, position, cards, cities, roads):
        self.name = name
        self.color = color
        self.position = position
        self.items = {}
        
    def isturn(self, turn): #Global turn must be implemented
        if self.position == turn:
            return True
        else:
            return False

    def add_item(self, item):
        self.items[item.name] = item

class Card:
    def __init__(self, resource, 

def roll():
    dice1 = random.randint(2, 7)
    dice2 = random.randint(7, 12)

class Tile:


    def __init__(self, type, trigger):
        self.type = type
        self.trigger = trigger
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