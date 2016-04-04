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
    def __init__(self, id, resource):
        self.id = id
        self.resource = []

    """
    def res_calc(self, resource):
        if resource == usedResources[i]:#variable here which will be from the map generator that will match triggers to resources
            if comment_var == "ham":
                Player.resources['ham'] += 1
            elif comment_var == "pineapple":
                Player.resources['pineapple'] += 1
            elif comment_var == "bread":
                Player.resources['bread'] += 1
            elif comment_var == "cheese":
                Player.resources['cheese'] += 1
            elif comment_var == "sauce":
                Player.resources['sauce'] += 1
    
    def isroad():
        if road_button == pressed #button to make roads is clicked
    """
"""
node1 = Node()
node1.id = 1
node2 = Node()
node2.id = 2
node3 = Node()
node3.id = 3
node4 = Node()
node4.id = 4
node5 = Node()
node5.id = 5
node6 = Node()
node6.id = 6
node7 = Node()
node7.id = 7
node8 = Node()
node8.id = 8
node9 = Node()
node9.id = 9
node10 = Node()
node10.id = 10
node11 = Node()
node11.id = 11
node12 = Node()
node12.id = 12
node13 = Node()
node13.id = 13
node14 = Node()
node14.id = 14
node15 = Node()
node15.id = 15
node16 = Node()
node16.id = 16
node17 = Node()
node17.id = 17
node18 = Node()
node18.id = 18
node19 = Node()
node19.id = 19
node20 = Node()
node20.id = 20
node21 = Node()
node21.id = 21
node22 = Node()
node22.id = 22
node23 = Node()
node23.id = 23
node24 = Node()
node24.id = 24
node25 = Node()
node25.id = 25
node26 = Node()
node26.id = 26
node27 = Node()
node27.id = 27
node28 = Node()
node28.id = 28
node29 = Node()
node29.id = 29
node30 = Node()
node30.id = 30
node31 = Node()
node31.id = 31
node32 = Node()
node32.id = 32
node33 = Node()
node33.id = 33
node34 = Node()
node34.id = 34
node35 = Node()
node35.id = 35
node36 = Node()
node36.id = 36
node37 = Node()
node37.id = 37
node38 = Node()
node38.id = 38
node39 = Node()
node39.id = 39
node40 = Node()
node40.id = 40
node41 = Node()
node41.id = 41
node42 = Node()
node42.id = 42
node43 = Node()
node43.id = 43
node44 = Node()
node44.id = 44
node45 = Node()
node45.id = 45
node46 = Node()
node46.id = 46
node47 = Node()
node47.id = 47
node48 = Node()
node48.id = 48
node49 = Node()
node49.id = 49
node50 = Node()
node50.id = 50
node51 = Node()
node51.id = 51
node52 = Node()
node52.id = 52
node53 = Node()
node53.id = 53
node54 = Node()
node54.id = 54
"""
class Road:
    def __init__(self, isroad, nodes):
        self.isroad = False
        self.nodes = []
"""
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
         [node54, node51],
         [node33, node38],
         [node44, node39]]

"""
class Cluster:
    def __init__(self, resource, roads):
        self.resource = ResourceGenned
        self.roads = []
"""
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
"""
usedResources = []

def InitialHexResourceRandomizer():
    global ResourceGenned
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
"""            

Clusters = [Cluster1, Cluster2, Cluster3, Cluster4, Cluster5, Cluster6, Cluster7, Cluster8, Cluster9, Cluster10, Cluster11, CLuster12, Cluster13, Cluster14, Cluster15, Cluster16, Cluster17, Cluster18, Cluster19]
Roads = [road1, road2, road3, road4, road5, road6, road7, road8, road9, road10, road11, road12, road13, road14, road15, road16, road17, road18, road19, road20, road21, road22, road23, road24, road25, road26, road27, road28, road29, road30, road31, road32, road33, road34, road35, road36, road37, road38, road39, road40, road41, road42, road43, road44, road45, road46, road47, road48, road49, road50, road51, road52, road53, road54, road55, road56, road57, road58, road59, road60, road61, road62, road63, road64, road65, road66, road67, road68, road69, road70, road71]

def ClusterToNode(cluster):
    for cluster in Clusters:
        for nodes in roads in cluster.roads:
            nodes.resource.append(cluster.resource)
"""
def maptest():
    node1 = Node()
    node1.id = 1
    node2 = Node()
    node2.id = 2
    node3 = Node()
    node3.id = 3
    node4 = Node()
    node4.id = 4
    node5 = Node()
    node5.id = 5
    node6 = Node()
    node6.id = 6
    node7 = Node()
    node7.id = 7
    node8 = Node()
    node8.id = 8
    node9 = Node()
    node9.id = 9
    node10 = Node()
    node10.id = 10
    node11 = Node()
    node11.id = 11
    node12 = Node()
    node12.id = 12
    node13 = Node()
    node13.id = 13
    node14 = Node()
    node14.id = 14
    node15 = Node()
    node15.id = 15
    node16 = Node()
    node16.id = 16
    node17 = Node()
    node17.id = 17
    node18 = Node()
    node18.id = 18
    node19 = Node()
    node19.id = 19
    node20 = Node()
    node20.id = 20
    node21 = Node()
    node21.id = 21
    node22 = Node()
    node22.id = 22
    node23 = Node()
    node23.id = 23
    node24 = Node()
    node24.id = 24
    node25 = Node()
    node25.id = 25
    node26 = Node()
    node26.id = 26
    node27 = Node()
    node27.id = 27
    node28 = Node()
    node28.id = 28
    node29 = Node()
    node29.id = 29
    node30 = Node()
    node30.id = 30
    node31 = Node()
    node31.id = 31
    node32 = Node()
    node32.id = 32
    node33 = Node()
    node33.id = 33
    node34 = Node()
    node34.id = 34
    node35 = Node()
    node35.id = 35
    node36 = Node()
    node36.id = 36
    node37 = Node()
    node37.id = 37
    node38 = Node()
    node38.id = 38
    node39 = Node()
    node39.id = 39
    node40 = Node()
    node40.id = 40
    node41 = Node()
    node41.id = 41
    node42 = Node()
    node42.id = 42
    node43 = Node()
    node43.id = 43
    node44 = Node()
    node44.id = 44
    node45 = Node()
    node45.id = 45
    node46 = Node()
    node46.id = 46
    node47 = Node()
    node47.id = 47
    node48 = Node()
    node48.id = 48
    node49 = Node()
    node49.id = 49
    node50 = Node()
    node50.id = 50
    node51 = Node()
    node51.id = 51
    node52 = Node()
    node52.id = 52
    node53 = Node()
    node53.id = 53
    node54 = Node()
    node54.id = 54
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
    InitialHexResourceRandomizer()
    Clusters = [Cluster1, Cluster2, Cluster3, Cluster4, Cluster5, Cluster6, Cluster7, Cluster8, Cluster9, Cluster10, Cluster11, CLuster12, Cluster13, Cluster14, Cluster15, Cluster16, Cluster17, Cluster18, Cluster19]
    Roads = [road1, road2, road3, road4, road5, road6, road7, road8, road9, road10, road11, road12, road13, road14, road15, road16, road17, road18, road19, road20, road21, road22, road23, road24, road25, road26, road27, road28, road29, road30, road31, road32, road33, road34, road35, road36, road37, road38, road39, road40, road41, road42, road43, road44, road45, road46, road47, road48, road49, road50, road51, road52, road53, road54, road55, road56, road57, road58, road59, road60, road61, road62, road63, road64, road65, road66, road67, road68, road69, road70, road71]
    for cluster in Clusters:
        for nodes in roads in cluster.roads:
            nodes.resource.append(cluster.resource)
    print(node1.resource)
    print(node2.resource)
    print(node3.resource)
    print(node4.resource)
    print(node5.resource)
    print(node6.resource)
    print(node7.resource)
    print(node8.resource)
    print(node9.resource)
    print(node9.resource)
    print(node10.resource)
    print(node11.resource)
    print(node12.resource)
    print(node13.resource)
    print(node14.resource)
    print(node15.resource)
    print(node16.resource)
    print(node17.resource)
    print(node18.resource)
    print(node19.resource)
    print(node20.resource)
    print(node21.resource)
    print(node22.resource)
    print(node23.resource)
    print(node24.resource)
    print(node25.resource)
    print(node26.resource)
    print(node27.resource)
    print(node28.resource)
    print(node29.resource)
    print(node30.resource)
    print(node31.resource)
    print(node32.resource)
    print(node33.resource)
    print(node34.resource)
    print(node35.resource)
    print(node36.resource)
    print(node37.resource)
    print(node38.resource)
    print(node39.resource)
    print(node40.resource)
    print(node50.resource)
    print(node51.resource)
    print(node52.resource)
    print(node53.resource)
    print(node54.resource)

maptest()



# def init():
 #   for i in numplayers:
   #     player + i  = Player(playernames(i), playercolor(i), playerposition(i))