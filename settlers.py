#Settlers of Catan

import random
#import pygame

"""
CODE DIRECTORY:
Line 33: Beginning of node invocations
Line 86: End of node invocations
Line 87: Beginning of road invocations
Line 158: End of road invocations
Line 159: Beginning of Cluster invocations
Line 177: End of cluster invocations
Line 178-182: Lists of clusters, roads, and nodes
Line 183: Player Class
Line 578: Node Class
Line 602: Road Class
Line 619: Cluster Class
Line 629: Roller function
Line 635: Startup function
Line 651: Initialize Function
Line 677: Player Input Function
Line 699: Hex Resource Randomizer Function
Line 767: Hex Trigger Randomizer Function
Line 860: Cluster to Node Distributor Function
Line 885 - 914: Verifier functions:
Line 916: Build Function
Line 951 - 1022: Initialization Functions
Line 1024 - 1041: Robber
"""

class Node:
    def __init__(self, id, claimed = False, iscity = False):
        self.id = id
        self.resource = []
        self.claimed = claimed
        self.claimedby = ""
        self.iscity = iscity 
    
    def claim(self, color):   #Need to only allow if certain color is other one
        if canclaim(self, color) == True:
            self.claimed = True
            self.claimedby = color
        else:
            print("Can't claim")
        
    
    def claimbypass(self, color):
        self.claimed = True
        self.claimedby = color
    
    def makecity(self, color):
        if cancity(self, color) == True:
            self.iscity = True 
            
class Road:
    def __init__(self, nodes, claimed = False):
        self.claimed = claimed
        self.nodes = []
        self.claimedby = ""
    
    def claim(self, color):
        if canclaimroad(self, color) == True:
            self.claimed = True
            self.claimedby = color
        else:
            print("Can't claim")

    def claimbypass(self, color):
        self.claimed = True
        self.claimedby = color
            
class Cluster:
    def __init__(self, roads, isrobber = False):
        self.resource = ""
        self.roads = []
        self.isrobber = isrobber
        self.tempresource = ""
        self.trigger = ""
        
def roller():
    global trigger
    trigger = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

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
road0 = Road([node4, node1])
road1 = Road([node1, node5])
road2 = Road([node5, node2])
road3 = Road([node2, node6])
road4 = Road([node6, node3])
road5 = Road([node3, node7])
road6 = Road([node4, node8])
road7 = Road([node5, node9])
road8 = Road([node6, node10])
road9 = Road([node7, node11])
road10 = Road([node12, node8])
road11 = Road([node8, node13])
road12 = Road([node13, node9])
road13 = Road([node9, node14])
road14 = Road([node14, node10])
road15 = Road([node10, node15])
road16 = Road([node15, node11])
road17 = Road([node11, node16])
road18 = Road([node12, node17])
road19 = Road([node13, node18])
road20 = Road([node14, node19])
road21 = Road([node15, node20])
road22 = Road([node16, node21])
road23 = Road([node22, node17])
road24 = Road([node17, node23])
road25 = Road([node23, node18])
road26 = Road([node18, node24])
road27 = Road([node24, node19])
road28 = Road([node19, node25])
road29 = Road([node25, node20])
road30 = Road([node20, node26])
road31 = Road([node26, node21])
road32 = Road([node21, node27])
road33 = Road([node22, node28])
road34 = Road([node23, node29])
road35 = Road([node24, node30])
road36 = Road([node25, node31])
road37 = Road([node26, node32])
road38 = Road([node27, node33])
road39 = Road([node28, node34])
road40 = Road([node34, node29])
road41 = Road([node29, node35])
road42 = Road([node35, node30])
road43 = Road([node30, node36])
road44 = Road([node36, node31])
road45 = Road([node31, node37])
road46 = Road([node37, node32])
road47 = Road([node32, node38])
road48 = Road([node34, node39])
road49 = Road([node35, node40])
road50 = Road([node36, node41])
road51 = Road([node37, node42])
road52 = Road([node38, node43])
road53 = Road([node44, node40])
road54 = Road([node40, node45])
road55 = Road([node45, node41])
road56 = Road([node41, node46])
road57 = Road([node46, node42])
road58 = Road([node42, node47])
road59 = Road([node47, node43])
road60 = Road([node44, node48])
road61 = Road([node45, node49])
road62 = Road([node46, node50])
road63 = Road([node47, node51])
road64 = Road([node48, node52])
road65 = Road([node52, node49])
road66 = Road([node49, node53])
road67 = Road([node53, node50])
road68 = Road([node50, node54])
road69 = Road([node54, node51])
road70 = Road([node33, node38])
road71 = Road([node44, node39])
Cluster1 = Cluster([road0, road6, road11, road12, road7, road1])
Cluster2 = Cluster([road3, road8, road14, road13, road7, road2])
Cluster3 = Cluster([road5, road9, road16, road15, road8, road4])
Cluster4 = Cluster([road11, road19, road25, road24, road18, road10])
Cluster5 = Cluster([road13, road20, road27, road26, road19, road12])
Cluster6 = Cluster([road15, road21, road29, road28, road20, road14])
Cluster7 = Cluster([road17, road22, road31, road30, road21, road16])
Cluster8 = Cluster([road24, road34, road40, road39, road33, road23])
Cluster9 = Cluster([road26, road35, road42, road41, road34, road25])
Cluster10 = Cluster([road28, road36, road44, road43, road35, road27])
Cluster11 = Cluster([road30, road37, road46, road45, road36, road29])
Cluster12 = Cluster([road32, road38, road70, road47, road37, road31])
Cluster13 = Cluster([road41, road49, road53, road71, road48, road40])
Cluster14 = Cluster([road43, road50, road55, road54, road49, road42])
Cluster15 = Cluster([road45, road51, road57, road56, road50, road44])
Cluster16 = Cluster([road47, road52, road59, road58, road52, road46])
Cluster17 = Cluster([road54, road61, road65, road64, road60, road53])
Cluster18 = Cluster([road56, road62, road67, road66, road61, road66])
Cluster19 = Cluster([road58, road63, road69, road68, road62, road57])
clusters = [Cluster1, Cluster2, Cluster3, Cluster4, Cluster5, Cluster6, Cluster7, Cluster8, Cluster9, Cluster10, Cluster11, Cluster12, Cluster13, Cluster14, Cluster15, Cluster16, Cluster17, Cluster18, Cluster19]
Roads = [road0, road1, road2, road3, road4, road5, road6, road7, road8, road9, road10, road11, road12, road13, road14, road15, road16, road17, road18, road19, road20, road21, road22, road23, road24, road25, road26, road27, road28, road29, road30, road31, road32, road33, road34, road35, road36, road37, road38, road39, road40, road41, road42, road43, road44, road45, road46, road47, road48, road49, road50, road51, road52, road53, road54, road55, road56, road57, road58, road59, road60, road61, road62, road63, road64, road65, road66, road67, road68, road69, road70, road71]
Nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15, node16, node17, node18, node19, node20, node21, node22, node23, node24, node25, node26, node27, node28, node29, node30, node31, node32, node33, node34, node35, node36, node37, node38, node39, node40, node41, node42, node43, node44, node45, node46, node47, node48, node49, node50, node51, node52, node53, node54]  
nodedict = {1 : node1, 2 : node2, 3 : node3, 4 : node4, 5 : node5, 6 : node6, 7 : node7, 8 : node8, 9 : node9, 10 : node10, 11 : node11, 12 : node12, 13 : node13, 14 : node14, 15 : node15, 16 : node16, 17 : node17, 18 : node18, 19 : node19, 20 : node20, 21 : node21, 22 : node22, 23 : node23, 24 : node24, 25 : node25, 26 : node26, 27 : node27, 28 : node28, 29 : node29, 30 : node30, 31 : node31, 32 : node32, 33 : node33, 34 : node34, 35 : node35, 36 : node36, 37 : node37, 38 : node38, 39 : node39, 40 : node40, 41 : node41, 42 : node42, 43 : node43, 44 : node44, 45 : node45, 46 : node46, 47 : node47, 48 : node48, 49 : node49, 50 : node50, 51 : node51, 52 : node52, 53 : node53, 54 : node54}       
roaddict = {0 : road0, 1 : road1, 2 : road2, 3 : road3, 4 : road4, 5 : road5, 6 : road6, 7 : road7, 8 : road8, 9 : road9, 10 : road10, 11 : road11, 12 : road12, 13 : road13, 14 : road14, 15 : road15, 16 : road16, 17 : road17, 18 : road18, 19 : road19, 20 : road20, 21 : road21, 22 : road22, 23 : road23, 24 : road24, 25 : road25, 26 : road26, 27 : road27, 28 : road28, 29 : road29, 30 : road30, 31 : road31, 32 : road32, 33 : road33, 34 : road34, 35 : road35, 36 : road36, 37 : road37, 38 : road38, 39 : road39, 40 : road40, 41 : road41, 42 : road42, 43 : road43, 44 : road44, 45 : road45, 46 : road46, 47 : road47, 48 : road48, 49 : road49, 50 : road50, 51 : road51, 52 : road52, 53 : road53, 54 : road54, 55 : road55, 56 : road56, 57 : road57, 58 : road58, 59 : road59, 60 : road60, 61 : road61, 62 : road62, 63 : road63, 64 : road64, 65 : road65, 66 : road66, 67 : road67, 68 : road68, 69 : road69, 70 : road70, 71 : road71}
class Player:
    def __init__(self, name, color, position):
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
        self.special = []
        self.nodes = []
        self.roads = []

    def payoff(self):
        for cluster in clusters:
            if cluster.trigger == trigger:
                if cluster.resource == "ham":
                    self.resources['ham'] += 1
                elif cluster.resource == "pineapple":
                    self.resources['pineapple'] += 1
                elif cluster.resource == "bread":
                    self.resources['bread'] += 1
                elif cluster.resource == "cheese":
                    self.resources['cheese'] += 1
                elif cluster.resource == "sauce":
                    self.resources['sauce'] += 1
    
    def claimnode(self, node): # Needs finishing
        if node == 1:
            node1.claim(self.color)
        elif node == 2:
            node2.claim(self.color)
        elif node == 3:
            node3.claim(self.color)
        elif node == 4:
            node4.claim(self.color)
        elif node == 5:
            node5.claim(self.color)
        elif node == 6:
            node6.claim(self.color)
        elif node == 7:
            node7.claim(self.color)
        elif node == 8:
            node8.claim(self.color)
        elif node == 9:
            node9.claim(self.color)
        elif node == 10:
            node10.claim(self.color)
        elif node == 11:
            node11.claim(self.color)
        elif node == 12:
            node12.claim(self.color)
        elif node == 13:
            node13.claim(self.color)
        elif node == 14:
            node14.claim(self.color)
        elif node == 15:
            node15.claim(self.color)
        elif node == 16:
            node16.claim(self.color)
        elif node == 17:
            node17.claim(self.color)
        elif node == 18:
            node18.claim(self.color)
        elif node == 19:
            node19.claim(self.color)
        elif node == 20:
            node20.claim(self.color)
        elif node == 21:
            node21.claim(self.color)
        elif node == 22:
            node22.claim(self.color)
        elif node == 23:
            node23.claim(self.color)
        elif node == 24:
            node24.claim(self.color)
        elif node == 25:
            node25.claim(self.color)
        elif node == 26:
            node26.claim(self.color)
        elif node == 27:
            node27.claim(self.color)
        elif node == 28:
            node28.claim(self.color)
        elif node == 29:
            node29.claim(self.color)
        elif node == 30:
            node30.claim(self.color)
        elif node == 31:
            node31.claim(self.color)
        elif node == 32:
            node32.claim(self.color)
        elif node == 33:
            node33.claim(self.color)
        elif node == 34:
            node34.claim(self.color)
        elif node == 35:
            node35.claim(self.color)
        elif node == 36:
            node36.claim(self.color)
        elif node == 37:
            node37.claim(self.color)
        elif node == 38:
            node38.claim(self.color)
        elif node == 39:
            node39.claim(self.color)
        elif node == 40:
            node40.claim(self.color)
        elif node ==41:
            node41.claim(self.color)
        elif node == 42:
            node42.claim(self.color)
        elif node == 43:
            node43.claim(self.color)
        elif node == 44:
            node44.claim(self.color)
        elif node == 45:
            node45.claim(self.color)
        elif node == 46:
            node46.claim(self.color)
        elif node == 47:
            node47.claim(self.color)
        elif node == 48:
            node48.claim(self.color)
        elif node == 49:
            node49.claim(self.color)
        elif node == 50:
            node50.claim(self.color)
        elif node == 51:
            node51.claim(self.color)
        elif node == 52:
            node52.claim(self.color)
        elif node == 53:
            node53.claim(self.color)
        elif node == 54:
            node54.claim(self.color)
    
    def claimroad(self, road):
        if road == 0:
            road0.claim(self.color)
        elif road == 1:
            road1.claim(self.color)
        elif road == 2:
            road2.claim(self.color)
        elif road == 3:
            road3.claim(self.color)
        elif road == 4:
            road4.claim(self.color)
        elif road == 5:
            road5.claim(self.color)
        elif road == 6:
            road6.claim(self.color)
        elif road == 7:
            road7.claim(self.color)
        elif road == 8:
            road8.claim(self.color)
        elif road == 9:
            road9.claim(self.color)
        elif road == 10:
            road10.claim(self.color)
        elif road == 11:
            road11.claim(self.color)
        elif road == 12:
            road12.claim(self.color)
        elif road == 13:
            road13.claim(self.color)
        elif road == 14:
            road14.claim(self.color)
        elif road == 15:
            road15.claim(self.color)
        elif road == 16:
            road16.claim(self.color)
        elif road == 17:
            road17.claim(self.color)
        elif road == 18:
            road18.claim(self.color)
        elif road == 19:
            road19.claim(self.color)
        elif road == 20:
            road20.claim(self.color)
        elif road == 21:
            road21.claim(self.color)
        elif road == 22:
            road22.claim(self.color)
        elif road == 23:
            road23.claim(self.color)
        elif road == 24:
            road24.claim(self.color)
        elif road == 25:
            road25.claim(self.color)
        elif road == 26:
            road26.claim(self.color)
        elif road == 27:
            road27.claim(self.color)
        elif road == 28:
            road28.claim(self.color)
        elif road == 29:
            road29.claim(self.color)
        elif road == 30:
            road30.claim(self.color)
        elif road == 31:
            road31.claim(self.color)
        elif road == 32:
            road32.claim(self.color)
        elif road == 33:
            road33.claim(self.color)
        elif road == 34:
            road34.claim(self.color)
        elif road == 35:
            road35.claim(self.color)
        elif road == 36:
            road36.claim(self.color)
        elif road == 37:
            road37.claim(self.color)
        elif road == 38:
            road38.claim(self.color)
        elif road == 39:
            road39.claim(self.color)
        elif road == 40:
            road40.claim(self.color)
        elif road == 41:
            road41.claim(self.color)
        elif road == 42:
            road42.claim(self.color)
        elif road == 43:
            road43.claim(self.color)
        elif road == 44:
            road44.claim(self.color)
        elif road == 45:
            road45.claim(self.color)
        elif road == 46:
            road46.claim(self.color)
        elif road == 47:
            road47.claim(self.color)
        elif road == 48:
            road48.claim(self.color)
        elif road == 49:
            road49.claim(self.color)
        elif road == 50:
            road50.claim(self.color)
        elif road == 51:
            road51.claim(self.color)
        elif road == 52:
            road52.claim(self.color)
        elif road == 53:
            road53.claim(self.color)
        elif road == 54:
            road54.claim(self.color)
        elif road == 55:
            road55.claim(self.color)
        elif road == 56:
            road56.claim(self.color)
        elif road == 57:
            road57.claim(self.color)
        elif road == 58:
            road58.claim(self.color)
        elif road == 59:
            road59.claim(self.color)
        elif road == 60:
            road60.claim(self.color)
        elif road == 61:
            road61.claim(self.color)
        elif road == 62:
            road62.claim(self.color)
        elif road == 63:
            road63.claim(self.color)
        elif road == 64:
            road64.claim(self.color)
        elif road == 65:
            road65.claim(self.color)
        elif road == 66:
            road66.claim(self.color)
        elif road == 67:
            road67.claim(self.color)
        elif road == 68:
            road68.claim(self.color)
        elif road == 69:
            road69.claim(self.color)
        elif road == 70:
            road70.claim(self.color)
        elif road == 71:
            road71.claim(self.color)
            
    def makepapa(self, node):
        if node == 1:
            node1.makecity(self.color)
        elif node == 2:
            node2.makecity(self.color)
        elif node == 3:
            node3.makecity(self.color)
        elif node == 4:
            node4.makecity(self.color)
        elif node == 5:
            node5.makecity(self.color)
        elif node == 6:
            node6.makecity(self.color)
        elif node == 7:
            node7.makecity(self.color)
        elif node == 8:
            node8.makecity(self.color)
        elif node == 9:
            node9.makecity(self.color)
        elif node == 10:
            node10.makecity(self.color)
        elif node == 11:
            node11.makecity(self.color)
        elif node == 12:
            node12.makecity(self.color)
        elif node == 13:
            node13.makecity(self.color)
        elif node == 14:
            node14.makecity(self.color)
        elif node == 15:
            node15.makecity(self.color)
        elif node == 16:
            node16.makecity(self.color)
        elif node == 17:
            node17.makecity(self.color)
        elif node == 18:
            node18.makecity(self.color)
        elif node == 19:
            node19.makecity(self.color)
        elif node == 20:
            node20.makecity(self.color)
        elif node == 21:
            node21.makecity(self.color) #Oh Node - FIX THIS SOON
        elif node == 22:
            node22.makecity(self.color)
        elif node == 23:
            node23.makecity(self.color)
        elif node == 24:
            node24.makecity(self.color)
        elif node == 25:
            node25.makecity(self.color)
        elif node == 26:
            node26.makecity(self.color)
        elif node == 27:
            node27.makecity(self.color)
        elif node == 28:
            node28.makecity(self.color)
        elif node == 29:
            node29.makecity(self.color)
        elif node == 30:
            node30.makecity(self.color)
        elif node == 31:
            node31.makecity(self.color)
        elif node == 32:
            node32.makecity(self.color)
        elif node == 33:
            node33.makecity(self.color)
        elif node == 34:
            node34.makecity(self.color)
        elif node == 35:
            node35.makecity(self.color)
        elif node == 36:
            node36.makecity(self.color)
        elif node == 37:
            node37.makecity(self.color)
        elif node == 38:
            node38.makecity(self.color)
        elif node == 39:
            node39.makecity(self.color)
        elif node == 40:
            node40.makecity(self.color)
        elif node ==41:
            node41.makecity(self.color)
        elif node == 42:
            node42.makecity(self.color)
        elif node == 43:
            node43.makecity(self.color)
        elif node == 44:
            node44.makecity(self.color)
        elif node == 45:
            node45.makecity(self.color)
        elif node == 46:
            node46.makecity(self.color)
        elif node == 47:
            node47.makecity(self.color)
        elif node == 48:
            node48.makecity(self.color)
        elif node == 49:
            node49.makecity(self.color)
        elif node == 50:
            node50.makecity(self.color)
        elif node == 51:
            node51.makecity(self.color)
        elif node == 52:
            node52.makecity(self.color)
        elif node == 53:
            node53.makecity(self.color)
        elif node == 54:
            node54.makecity(self.color)








def play():
    global numplayers
    input1 = input("How Many Players?:   ")
    numplayers = input1
    return str(input1)

##numplayers = 0
colors = ['red', 'blue', 'white', 'orange', 'green', 'brown']
playernames = [] 
playercolor = [] 
playerposition = []



turn = 1

def init():
    global P1
    global P2
    global P3
    global P4
    global playerdict
    global playerdict1
    if len(playercolor) == 4:
        P4 = Player(playernames[0], playercolor[0], playerposition[0])
        P3 = Player(playernames[1], playercolor[1], playerposition[1])
        P2 = Player(playernames[2], playercolor[2], playerposition[2])
        P1 = Player(playernames[3], playercolor[3], playerposition[3])
        playerdict = {4 : P1, 3: P2, 2: P3, 1 : P4}
        playerdict1 = {1 : P1, 2 : P2, 3 : P3, 4 : P4}
    elif len(playercolor) == 3:
        P3 = Player(playernames[0], playercolor[0], playerposition[0])
        P2 = Player(playernames[1], playercolor[1], playerposition[1])
        P1 = Player(playernames[2], playercolor[2], playerposition[2])
        playerdict = {3 : P1, 2 : P2, 1 : P3}
        playerdict1 = {1 : P1, 2 : P2, 3 : P3}
    elif len(playercolor) == 2:
        P2 = Player(playernames[0], playercolor[0], playerposition[0])
        P1 = Player(playernames[1], playercolor[1], playerposition[1])
        playerdict = {2 : P1, 1 : P2}
        playerdict1 = {1 : P1, 2 : P2}
    
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
        init()
    else:
        playernames.append(input("Enter Player " + string + " Name:   "))
        m = str(input("Enter Player " + string + " Color (Blue, Red, White, Orange, Green, or Brown):   ")).lower()
        while colors.count(m) != 1 or playercolor.count(m) > 0:
            m = str(input("Enter Player " + string + " Color (Blue, Red, White, Orange, Green, or Brown):   ")).lower()
        playercolor.append(m) 
        playerposition.append(int(string))
        playerinput(str(int(string) - 1))

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
            
usedID = []
IDGenned = []

def InitialHexTriggerRandomizer():
    while len(usedID) < 18:          
        IDGenVar = int(random.choice([2, 3, 4, 5, 6, 8, 9, 10, 11, 12]))
        if IDGenVar == 2:
            if usedID.count(2) == 0:
                usedID.append(2)
                IDGenned.append(2)
                InitialHexTriggerRandomizer()
            else:
                InitialHexTriggerRandomizer()
        if IDGenVar == 3:
            if usedID.count(3) == 0 or usedID.count(3) == 1:
                usedID.append(3)
                IDGenned.append(3)
                InitialHexTriggerRandomizer()
            if usedID.count(3) >= 2:
                InitialHexTriggerRandomizer()
        if IDGenVar == 4:
            if usedID.count(4) == 0 or usedID.count(4) == 1:
                usedID.append(4)
                IDGenned.append(4)
                InitialHexTriggerRandomizer()
            if usedID.count(4) >= 2:
                InitialHexTriggerRandomizer()
        if IDGenVar == 5:
            if usedID.count(5) == 0 or usedID.count(5) == 1:
                usedID.append(5)
                IDGenned.append(5)
                InitialHexTriggerRandomizer()
            if usedID.count(5) >= 2:
                InitialHexTriggerRandomizer()
        if IDGenVar == 6:
            if usedID.count(6) == 0 or usedID.count(6) == 1:
                usedID.append(6)
                IDGenned.append(6)
                InitialHexTriggerRandomizer()
            if usedID.count(6) >= 2:
                InitialHexTriggerRandomizer()
        if IDGenVar == 8:
            if usedID.count(8) == 0 or usedID.count(8) == 1:
                usedID.append(8)
                IDGenned.append(8)
                InitialHexTriggerRandomizer()
            if usedID.count(8) >= 2:
                InitialHexTriggerRandomizer()
        if IDGenVar == 9:
            if usedID.count(9) == 0 or usedID.count(9) == 1:
                usedID.append(9)
                IDGenned.append(9)
                InitialHexTriggerRandomizer()
            if usedID.count(9) >= 2:
                InitialHexTriggerRandomizer()
        if IDGenVar == 10:
            if usedID.count(10) == 0 or usedID.count(10) == 1:
                usedID.append(10)
                IDGenned.append(10)
                InitialHexTriggerRandomizer()
            if usedID.count(10) >= 2:
                InitialHexTriggerRandomizer()
        if IDGenVar == 11:
            if usedID.count(11) == 0 or usedID.count(11) == 1:
                usedID.append(11)
                IDGenned.append(11)
                InitialHexTriggerRandomizer()
            if usedID.count(11) >= 2:
                InitialHexTriggerRandomizer()
        if IDGenVar == 12:
            if usedID.count(12) == 0:
                usedID.append(12)
                IDGenned.append(12)
                InitialHexTriggerRandomizer()
            if usedID.count(12) >= 2:
                InitialHexTriggerRandomizer()
    Cluster1.trigger = IDGenned[0]
    Cluster2.trigger = IDGenned[1]
    Cluster3.trigger = IDGenned[2]
    Cluster4.trigger = IDGenned[3]
    Cluster5.trigger = IDGenned[4]
    Cluster6.trigger = IDGenned[5]
    Cluster7.trigger = IDGenned[6]
    Cluster8.trigger = IDGenned[7]
    Cluster9.trigger = IDGenned[8]
    Cluster10.trigger = IDGenned[9]
    Cluster11.trigger = IDGenned[10]
    Cluster12.trigger = IDGenned[11]
    Cluster13.trigger = IDGenned[12]
    Cluster14.trigger = IDGenned[13]
    Cluster15.trigger = IDGenned[14]
    Cluster16.trigger = IDGenned[15]
    Cluster17.trigger = IDGenned[16]
    Cluster18.trigger = IDGenned[17]

def ClusterToNode():
    global robber_loc
    for cluster in clusters:
        for road in cluster.roads:
            for node in road.nodes:
                node.resource.append(cluster.resource)
                node.isrobber = cluster.isrobber
                hamburglar()
                if cluster.isrobber == True:
                    robber_loc = node                
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
               
def canclaimroad(roadr, color):
    a = False
    for roads in Roads:
        if roads.claimed == True and roads.claimedby == color:
            for node in roads.nodes:
                for node1 in roadr.nodes:
                    if node == node1:
                        a = True
    return a
    
def canclaim(noder, color):
    colors = ['red', 'blue', 'white', 'orange', 'green', 'brown']
    colors.remove(color)
    a = False
    if noder.claimedby != '' or colors.count(noder.claimedby) > 0:
        return a
    else:
        for roads in Roads:
            if roads.claimed == True and roads.claimedby == color:
                for node in roads.nodes:
                    if noder == node:
                        a = True
    return a
                
def cancity(noder, color):
    if noder.claimedby == color:
        return True
    else:
        print("Can't Papa")
        return False
 
def build(): #Needs to be finished
    global turn
    print("\n Choices: \n Road (1 Pineapple, 1 Cheese) \n Pizza Hut (1 Bread, 1 Cheese, 1 Pineapple, 1 Sauce) \n Papa Johns (3 Ham, 2 Bread) \n  ")
    input2 = input("What would you like to construct?    ")
    if input2 == "Pizza Hut":
        input3 = input("Where would you like to to place this?  ")
        if turn == 1:
            P1.claimnode(int(input3))
        if turn == 2:
            P2.claimnode(int(input3))
        if turn == 3:
            P3.claimnode(int(input3))
        if turn == 4:
            P4.claimnode(int(input3))
    if input2 == "Road":
        input3 = input("Where would you like to to place this?  ")
        if turn == 1:
            P1.claimroad(int(input3))
        if turn == 2:
            P2.claimroad(int(input3))
        if turn == 3:
            P3.claimroad(int(input3))
        if turn == 4:
            P4.claimroad(int(input3))
    if input2 == "Papa Johns":
        input3 = input("Where would you like to to place this?  ")
        if turn == 1:
            P1.makepapa(int(input3))
        if turn == 2:
            P2.makepapa(int(input3))
        if turn == 3:
            P3.makepapa(int(input3))
        if turn == 4:
            P4.makepapa(int(input3))

def initialize(n):
    if n == 1:
        input4 = input("Please place your first settlement, " + playerdict[n].name + ":   ")
        while nodedict[int(input4)].claimedby != playerdict[n].color:
            if nodedict[int(input4)].claimedby == "":
                nodedict[int(input4)].claimbypass(playerdict[n].color)
            else:
                print("Please select an empty vertice")
                input4 = input("Please place your first settlement, " + playerdict[n].name + ":   ")
        input4 = input("Please place your first road, " + playerdict[n].name + ":   ")
        while roaddict[int(input4)].claimedby != playerdict[n].color:
            if roaddict[int(input4)].claimedby == "":
                roaddict[int(input4)].claimbypass(playerdict[n].color)
            else:
                print("Please select an empty road")
                input4 = input("Please place your first road, " + playerdict[n].name + ":   ")    
    else:
        input4 = input("Please place your first settlement, " + playerdict[n].name + ":   ")
        while nodedict[int(input4)].claimedby != playerdict[n].color:
            if nodedict[int(input4)].claimedby == "":
                nodedict[int(input4)].claimbypass(playerdict[n].color)
            else:
                print("Please select an empty vertice")
                input4 = input("Please place your first settlement, " + playerdict[n].name + ":   ")
        input4 = input("Please place your first road, " + playerdict[n].name + ":   ")
        while roaddict[int(input4)].claimedby != playerdict[n].color:
            if roaddict[int(input4)].claimedby == "":
                roaddict[int(input4)].claimbypass(playerdict[n].color)
            else:
                print("Please select an empty road")
                input4 = input("Please place your first road, " + playerdict[n].name + ":   ") 
        initialize(n-1)
        
def initializepart2(n):
    if n == 1:
        input4 = input("Please place your second settlement, " + playerdict1[n].name + ":   ")
        while nodedict[int(input4)].claimedby != playerdict1[n].color:
            if nodedict[int(input4)].claimedby == "":
                nodedict[int(input4)].claimbypass(playerdict1[n].color)
            else:
                print("Please select an empty vertex")
                input4 = input("Please place your second settlement, " + playerdict1[n].name + ":   ")
        input4 = input("Please place your second road, " + playerdict1[n].name + ":   ")
        while roaddict[int(input4)].claimedby != playerdict1[n].color:
            if roaddict[int(input4)].claimedby == "":
                roaddict[int(input4)].claimbypass(playerdict1[n].color)
            else:
                print("Please select an empty road")
                input4 = input("Please place your second road, " + playerdict1[n].name + ":   ") 
    else:
        input4 = input("Please place your second settlement, " + playerdict1[n].name + ":   ")
        while nodedict[int(input4)].claimedby != playerdict1[n].color or howmanynodes(playerdict1[n].color) < 2:
            if nodedict[int(input4)].claimedby == "":
                nodedict[int(input4)].claimbypass(playerdict1[n].color)
            else:
                print("Please select an empty vertex")
                input4 = input("Please place your second settlement, " + playerdict1[n].name + ":   ")
        input4 = input("Please place your second road, " + playerdict[n].name + ":   ")
        while roaddict[int(input4)].claimedby != playerdict1[n].color:
            if roaddict[int(input4)].claimedby == "":
                roaddict[int(input4)].claimbypass(playerdict1[n].color)
            else:
                print("Please select an second road")
                input4 = input("Please place your second road, " + playerdict1[n].name + ":   ") 
        initializepart2(n-1)
      
def howmanynodes(color):
    a = 0
    for node in Nodes:
        if node.claimedby == color:
            a = a + 1
    return a
            
def hamburglar():
    if cluster.isrobber == True:
        cluster.tempresource = clusters.resource
        cluster.resource = ""
    if cluster.isrobber == False:
        if cluster.resource == "":
            cluster.resource = clusters.tempresource            

def move_hamburglar():
    if trigger == 7:
        hamburglar_newloc = int(input("Where would you like to move the hamburglar?"))
        relevant_var = hamburglar_newloc - 1
        robber_loc = False
        clusters[relevant_var].isrobber = True
"""        
InitialHexTriggerRandomizer()
InitialHexResourceRandomizer()
ClusterToNode()
playerinput(play())
initialize(int(numplayers))
initializepart2(int(numplayers))
"""
def debugbypass():
    global P1
    global P2
    global P3
    global P4
    global playerdict
    global playerdict1
    P1 = Player("Carter", "Blue", 4)
    P2 = Player("Mikol", "Red", 3)
    P3 = Player("Peter", "Brown", 2)
    P4 = Player("John", "Green", 1)
    playerdict = {4 : P1, 3: P2, 2: P3, 1 : P4}
    playerdict1 = {1 : P1, 2 : P2, 3 : P3, 4 : P4}
    InitialHexTriggerRandomizer()
    InitialHexResourceRandomizer()
    ClusterToNode()
    
    