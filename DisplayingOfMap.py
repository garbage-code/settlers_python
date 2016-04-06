#Settlers of Catan
import random
import pygame


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
    def __init__(self, id):
        self.id = id
        self.resource = []

    
   # def res_calc(self, resource):
    #    if resource == usedResources[i]:#variable here which will be from the map generator that will match triggers to resources
     #       if comment_var == "ham":
      #          Player.resources['ham'] += 1
        #    elif comment_var == "pineapple":
         #       Player.resources['pineapple'] += 1
          #  elif comment_var == "bread":
           #     Player.resources['bread'] += 1
            #elif comment_var == "cheese":
             #   Player.resources['cheese'] += 1
            #elif comment_var == "sauce":
             #   Player.resources['sauce'] += 1

    #def isroad():
     #   if road_button == pressed #button to make roads is clicked

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)
node15 = Node(15)
node16 = Node(16)
node17 = Node(17)
node18 = Node(18)
node19 = Node(19)
node20 = Node(20)
node21 = Node(21)
node22 = Node(22)
node23 = Node(23)
node24 = Node(24)
node25 = Node(25)
node26 = Node(26)
node27 = Node(27)
node28 = Node(28)
node29 = Node(29)
node30 = Node(30)
node31 = Node(31)
node32 = Node(32)
node33 = Node(33)
node34 = Node(34)
node35 = Node(35)
node36 = Node(36)
node37 = Node(37)
node38 = Node(38)
node39 = Node(39)
node40 = Node(40)
node41 = Node(41)
node42 = Node(42)
node43 = Node(43)
node44 = Node(44)
node45 = Node(45)
node46 = Node(46)
node47 = Node(47)
node48 = Node(48)
node49 = Node(49)
node50 = Node(50)
node51 = Node(51)
node52 = Node(52)
node53 = Node(53)
node54 = Node(54)

class Road:
    def __init__(self, isroad = False):
        self.isroad = isroad
        self.nodes = []

road0 = Road()
road0.nodes = [node4, node1]
road1 = Road()
road1.nodes = [node1, node5]
road2 = Road()
road2.nodes = [node5, node2]
road3 = Road()
road3.nodes = [node2, node6]
road4 = Road()
road4.nodes = [node6, node3]
road5 = Road()
road5.nodes = [node3, node7]
road6 = Road()
road6.nodes = [node4, node8]
road7 = Road()
road7.nodes = [node5, node9]
road8 = Road()
road8.nodes = [node6, node10]
road9 = Road()
road9.nodes = [node7, node11]
road10 = Road()
road10.nodes = [node12, node8]
road11 = Road()
road11.nodes = [node8, node13]
road12 = Road()
road12.nodes = [node13, node9]
road13 = Road()
road13.nodes = [node9, node14]
road14 = Road()
road14.nodes = [node14, node10]
road15 = Road()
road15.nodes = [node10, node15]
road16 = Road()
road16.nodes = [node15, node11]
road17 = Road()
road17.nodes = [node11, node16]
road18 = Road()
road18.nodes = [node12, node17]
road19 = Road()
road19.nodes = [node13, node18]
road20 = Road()
road20.nodes = [node14, node19]
road21 = Road()
road21.nodes = [node15, node20]
road22 = Road()
road22.nodes = [node16, node21]
road23 = Road()
road23.nodes = [node22, node17]
road24 = Road()
road24.nodes = [node17, node23]
road25 = Road()
road25.nodes = [node23, node18]
road26 = Road()
road26.nodes = [node18, node24]
road27 = Road()
road27.nodes = [node24, node19]
road28 = Road()
road28.nodes = [node19, node25]
road29 = Road()
road29.nodes = [node25, node20]
road30 = Road()
road30.nodes = [node20, node26]
road31 = Road()
road31.nodes = [node26, node21]
road32 = Road()
road32.nodes = [node21, node27]
road33 = Road()
road33.nodes = [node22, node28]
road34 = Road()
road34.nodes = [node23, node29]
road35 = Road()
road35.nodes = [node24, node30]
road36 = Road()
road36.nodes = [node25, node31]
road37 = Road()
road37.nodes = [node26, node32]
road38 = Road()
road38.nodes = [node27, node33]
road39 = Road()
road39.nodes = [node28, node34]
road40 = Road()
road40.nodes = [node34, node29]
road41 = Road()
road41.nodes = [node29, node35]
road42 = Road()
road42.nodes = [node35, node30]
road43 = Road()
road43.nodes = [node30, node36]
road44 = Road()
road44.nodes = [node36, node31]
road45 = Road()
road45.nodes = [node31, node37]
road46 = Road()
road46.nodes = [node37, node32]
road47 = Road()
road47.nodes = [node32, node38]
road48 = Road()
road48.nodes = [node34, node39]
road49 = Road()
road49.nodes = [node35, node40]
road50 = Road()
road50.nodes = [node36, node41]
road51 = Road()
road51.nodes = [node37, node42]
road52 = Road()
road52.nodes = [node38, node43]
road53 = Road()
road53.nodes = [node44, node40]
road54 = Road()
road54.nodes = [node40, node45]
road55 = Road()
road55.nodes = [node45, node41]
road56 = Road()
road56.nodes = [node41, node46]
road57 = Road()
road57.nodes = [node46, node42]
road58 = Road()
road58.nodes = [node42, node47]
road59 = Road()
road59.nodes = [node47, node43]
road60 = Road()
road60.nodes = [node44, node48]
road61 = Road()
road61.nodes = [node45, node49]
road62 = Road()
road62.nodes = [node46, node50]
road63 = Road()
road63.nodes = [node47, node51]
road64 = Road()
road64.nodes = [node48, node52]
road65 = Road()
road65.nodes = [node52, node49]
road66 = Road()
road66.nodes = [node49, node53]
road67 = Road()
road67.nodes = [node53, node50]
road68 = Road()
road68.nodes = [node50, node54]
road69 = Road()
road69.nodes = [node54, node51]
road70 = Road()
road70.nodes = [node33, node38]
road71 = Road()
road71.nodes = [node44, node39]



class Cluster:
    def __init__(self):
        self.resource = ""
        self.roads = []

Cluster1 = Cluster()
Cluster1.roads = [road0, road6, road11, road12, road7, road1]
Cluster2 = Cluster()
Cluster2.roads = [road3, road8, road14, road13, road7, road2]
Cluster3 = Cluster()
Cluster3.roads = [road5, road9, road16, road15, road8, road4]
Cluster4 = Cluster()
Cluster4.roads = [road11, road19, road25, road24, road18, road10]
Cluster5 = Cluster()
Cluster5.roads = [road13, road20, road27, road26, road19, road12]
Cluster6 = Cluster()
Cluster6.roads = [road15, road21, road29, road28, road20, road14]
Cluster7 = Cluster()
Cluster7.roads = [road17, road22, road31, road30, road21, road16]
Cluster8 = Cluster()
Cluster8.roads = [road24, road34, road40, road39, road33, road23]
Cluster9 = Cluster()
Cluster9.roads = [road26, road35, road42, road41, road34, road25]
Cluster10 = Cluster()
Cluster10.roads = [road28, road36, road44, road43, road35, road27]
Cluster11 = Cluster()
Cluster11.roads = [road30, road37, road46, road45, road36, road29]
Cluster12 = Cluster()
Cluster12.roads = [road32, road38, road70, road47, road37, road31]
Cluster13 = Cluster()
Cluster13.roads = [road41, road49, road53, road71, road48, road40]
Cluster14 = Cluster()
Cluster14.roads = [road43, road50, road55, road54, road49, road42]
Cluster15 = Cluster()
Cluster15.roads = [road45, road51, road57, road56, road50, road44]
Cluster16 = Cluster()
Cluster16.roads = [road47, road52, road59, road58, road52, road46]
Cluster17 = Cluster()
Cluster17.roads = [road54, road61, road65, road64, road60, road53]
Cluster18 = Cluster()
Cluster18.roads = [road56, road62, road67, road66, road61, road66]
Cluster19 = Cluster()
Cluster19.roads = [road58, road63, road69, road68, road62, road57]

usedResources = []

def InitialHexResourceRandomizer():
    while len(usedResources) < 19:            
        ResourceGenVar = random.choice(["ham", "pineapple", "cheese", "sauce", "bread", "desert"])
        if ResourceGenVar == "ham":
            if usedResources.count("ham") >= 0 and usedResources.count("ham") <= 3:
                usedResources.append("ham")
                ResourceGenned = "ham"
                InitialHexResourceRandomizer()
            if usedResources.count("ham") == 4:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "pineapple":
            if usedResources.count("pineapple") >= 0 and usedResources.count("pineapple") <= 3:
                usedResources.append("pineapple")
                ResourceGenned = "pineapple"
                InitialHexResourceRandomizer()
            if usedResources.count("pineapple") == 4:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "cheese":
            if usedResources.count("cheese") >= 0 and usedResources.count("cheese") <= 4:
                usedResources.append("cheese")
                ResourceGenned = "cheese"
                InitialHexResourceRandomizer()
            if usedResources.count("cheese") == 5:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "sauce":
            if usedResources.count("sauce") >= 0 and usedResources.count("sauce") <= 4:
                usedResources.append("sauce")
                ResourceGenned = "sauce"
                InitialHexResourceRandomizer()
            if usedResources.count("cheese") == 5:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "bread":
            if usedResources.count("bread") >= 0 and usedResources.count("bread") <= 4:
                usedResources.append("bread")
                ResourceGenned = "bread"
                InitialHexResourceRandomizer()
            if usedResources.count("bread") == 5:
                InitialHexResourceRandomizer()
        if ResourceGenVar == "desert":
            if usedResources.count("desert") == 0:
                usedResources.append("desert")
                ResourceGenned = "desert"
                InitialHexResourceRandomizer()
            if usedResources.count("desert") == 1:
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
            

clusters = [Cluster1, Cluster2, Cluster3, Cluster4, Cluster5, Cluster6, Cluster7, Cluster8, Cluster9, Cluster10, Cluster11, Cluster12, Cluster13, Cluster14, Cluster15, Cluster16, Cluster17, Cluster18, Cluster19]
Roads = [road1, road2, road3, road4, road5, road6, road7, road8, road9, road10, road11, road12, road13, road14, road15, road16, road17, road18, road19, road20, road21, road22, road23, road24, road25, road26, road27, road28, road29, road30, road31, road32, road33, road34, road35, road36, road37, road38, road39, road40, road41, road42, road43, road44, road45, road46, road47, road48, road49, road50, road51, road52, road53, road54, road55, road56, road57, road58, road59, road60, road61, road62, road63, road64, road65, road66, road67, road68, road69, road70, road71]
Nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15, node16, node17, node18, node19, node20, node21, node22, node23, node24, node25, node26, node27, node28, node29, node30, node31, node32, node33, node34, node35, node36, node37, node38, node39, node40, node41, node42, node43, node44, node45, node46, node47, node48, node49, node50, node51, node52, node53, node54]

def ClusterToNode():
    for cluster in clusters:
        for road in cluster.roads:
            for node in road.nodes:
                node.resource.append(cluster.resource)
            temp = []
            if node.resource.count("ham") == 2:
                temp.append("ham")
            elif node.resource.count("pineapple") == 2:
                temp.append("pineapple")
            elif node.resource.count("cheese") == 2:
                temp.append("cheese")
            elif node.resource.count("sauce") == 2:
                temp.append("sauce")
            elif node.resource.count("bread") == 2:
                temp.append("bread")
            elif node.resource.count("desert") == 2:
                temp.append("desert")
            node.resource = temp
    
        
 
InitialHexResourceRandomizer()
ClusterToNode()


# def init():
 #   for i in numplayers:
   #     player + i  = Player(playernames(i), playercolor(i), playerposition(i))
        
#playerinput(play())


