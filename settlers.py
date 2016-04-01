m#Settlers of Catan
import random
import pygame


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
        self.resources = {'ham'      : 0, 
                          'pineapple': 0, 
                          'bread'    : 0, 
                          'sauce'    : 0, 
                          'cheese'   : 0}
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

#54 nodes
class Node:
    def __init__(self, id, resource, isroad):
        self.id = id
        self.resource = []
        self.isroad = False
    
    def res_calc(self, resource):
        if resource == comment_var:#variable here which will be from the map generator that will match triggers to resources
            if comment_var == "ham":
                dict['ham'] += 1
            elif comment_var == "pineapple":
                dict['pineapple'] += 1
            elif comment_var == "bread":
                dict['bread'] += 1
            elif comment_var == "cheese":
                dict['cheese'] += 1
            elif comment_var == "sauce":
                dict['sauce'] += 1

    def isroad():
        if road_button == pressed #button to make roads is clicked

node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node5 = Node()
node6 = Node()
node7 = Node()
node8 = Node()
node9 = Node()
node10 = Node()
node11 = Node()
node12 = Node()
node13 = Node()
node14 = Node()
node15 = Node()
node16 = Node()
node17 = Node()
node18 = Node()
node19 = Node()
node20 = Node()
node21 = Node()
node22 = Node()
node23 = Node()
node24 = Node()
node25 = Node()
node26 = Node()
node27 = Node()
node28 = Node()
node29 = Node()
node30 = Node()
node31 = Node()
node32 = Node()
node33 = Node()
node34 = Node()
node35 = Node()
node36 = Node()
node37 = Node()
node38 = Node()
node39 = Node()
node40 = Node()
node41 = Node()
node42 = Node()
node43 = Node()
node44 = Node()
node45 = Node()
node46 = Node()
node47 = Node()
node48 = Node()
node49 = Node()
node50 = Node()
node51 = Node()
node52 = Node()
node53 = Node()
node54 = Node()
roads = [[node1, node4], 
         [node1, node5], 
         [node5, node2], 
         [node2, node6], 
         [node6, node3], 
         [node3, node7], 
         [node4, node8], 
         [node5, node9], 
         [node6, node10],
         [node7, node11],
         [node12, node8], 
         [node8, node13], 
         [node13, node9], 
         [node9, node14], 
         [node14, node10], 
         [node10, node15], 
         [node15, node11], 
         [node11, node16],
         [node12, node17], 
         [node13, node18], 
         [node14, node19], 
         [node15, node20], 
         [node16, node21],
         [node22, node17], 
         [node17, node23], 
         [node23, node18], 
         [node18, node24], 
         [node24, node19], 
         [node19, node25], 
         [node25, node20], 
         [node20, node26], 
         [node26, node21], 
         [node21, node27],
         [node22, node28], 
         [node23, node29], 
         [node24, node30], 
         [node25, node31], 
         [node26, node32], 
         [node27, node33],
         [node28, node34], 
         [node34, node29], 
         [node29, node35], 
         [node35, node30], 
         [node30, node36], 
         [node36, node31], 
         [node31, node37], 
         [node37, node32], 
         [node32, node38],
         [node34, node39], 
         [node35, node40], 
         [node36, node41], 
         [node37, node42], 
         [node38, node43],
         [node44, node40], 
         [node40, node45], 
         [node45, node41], 
         [node41, node46], 
         [node46, node42], 
         [node42, node47], 
         [node47, node43],
         [node44, node48], 
         [node45, node49], 
         [node46, node50], 
         [node47, node51],
         [node48, node52], 
         [node52, node49], 
         [node49, node53], 
         [node53, node50], 
         [node50, node54], 
         [node54, node51]]

class Cluster:
    def __init__(self, resource, roads):
        self.resource = ResourceGenned
        self.roads = []

Cluster1 = Cluster()
Cluster1.roads = [roads[0], roads[6], roads[11], roads[12], roads[7], roads[1]]
Cluster2 = Cluster()
Cluster2.roads = [roads[3], roads[8], roads[14], roads[13], roads[7], roads[2]]
Cluster3 = Cluster()
Cluster3.roads = [roads[5], roads[9], roads[16], roads[15], roads[8], roads[4]]
Cluster4 = Cluster()
Cluster4.roads = [roads[11], roads[19], roads[25], roads[24], roads[18], roads[10]]
Cluster5 = Cluster()
Cluster5.roads = [roads[13], roads[20], roads[27], roads[26], roads[19], roads[12]]
Cluster6 = Cluster()
Cluster6.roads = [roads[15], roads[21], roads[29], roads[28], roads[20], roads[14]]
Cluster7 = Cluster()
Cluster7.roads = [roads[17], roads[22], roads[31], roads[30], roads[21], roads[16]]
Cluster8 = Cluster()
Cluster8.roads = [roads[24], roads[34], roads[40], roads[39], roads[33], roads[23]]
Cluster9 = Cluster()
Cluster9.roads = [roads[26], roads[35], roads[42], roads[41], roads[34], roads[25]]
Cluster10 = Cluster()
Cluster10.roads = [roads[28], roads[36], roads[44], roads[43], roads[35], roads[27]]
Cluster11 = Cluster()
Cluster12 = Cluster()
Cluster13 = Cluster()
Cluster14 = Cluster()
Cluster15 = Cluster()
Cluster16 = Cluster()
Cluster17 = Cluster()
Cluster18 = Cluster()
Cluster19 = Cluster()

usedResources = []

def InitialHexResourceRandomizer():
    while len(usedResources) < 19:            
        ResourceGenVar = random.choice(["ham", "pineapple", "cheese", "sauce", "bread"])
        if ResourceGenVar == "ham":
            if usedResources.count("ham") == 0 or usedResources.count("ham") == 1:
                usedResources.append("ham")
                ResourceGenned = "ham"
                InitialHexResourceRandomizer()
            if usedResources.count("ham") == 2:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "pineapple":
            if usedResources.count("pineapple") == 0 or usedResources.count("pineapple") == 1:
                usedResources.append("pineapple")
                ResourceGenned = "pineapple"
                InitialHexResourceRandomizer()
            if usedResources.count("pineapple") == 2:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "cheese":
            if usedResources.count("cheese") == 0 or usedResources.count("cheese") == 1:
                usedResources.append("cheese")
                ResourceGenned = "cheese"
                InitialHexResourceRandomizer()
            if usedResources.count("cheese") == 2:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "sauce":
            if usedResources.count("sauce") == 0 or usedResources.count("sauce") == 1:
                usedResources.append("sauce")
                ResourceGenned = "sauce"
                InitialHexResourceRandomizer()
            if usedResources.count("cheese") == 2:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "bread":
            if usedResources.count("bread") == 0 or usedResources.count("bread") == 1:
                usedResources.append("bread")
                ResourceGenned = "bread"
                InitialHexResourceRandomizer()
            if usedResources.count("bread") == 2:
                InitialHexResourceRandomizer()
    Cluster1.resource = usedResources[0]
    Cluster2.resource = usedResources[1]
    Cluster3.resource = usedResources[2]
    Cluster4.resource = usedResources[3]
    Cluster5.resource = usedResources[4]
    Cluster6.resource = usedResources[5]
    Cluster7.resource = usedResources[6]
    Cluster8.resource = usedResources[7]
    Cluster9.resource = usedResources[8]
    Cluster10.resource = usedResources[9]
    Cluster11.resource = usedResources[10]
    Cluster12.resource = usedResources[11]
    Cluster13.resource = usedResources[12]
    Cluster14.resource = usedResources[13]
    Cluster15.resource = usedResources[14]
    Cluster16.resource = usedResources[15]
    Cluster17.resource = usedResources[16]
    Cluster18.resource = usedResources[17]
    Cluster19.resource = usedResources[18]
            


        

# def init():
 #   for i in numplayers:
   #     player + i  = Player(playernames(i), playercolor(i), playerposition(i))
        
playerinput(play())