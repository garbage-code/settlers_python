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

Nodes = []

for i in range(54):
    Nodes.append(Node(i+1))
    

road0 = Road([Nodes[3], Nodes[0]])
road1 = Road([Nodes[0], Nodes[4]])
road2 = Road([Nodes[4], Nodes[1]])
road3 = Road([Nodes[1], Nodes[5]])
road4 = Road([Nodes[5], Nodes[2]])
road5 = Road([Nodes[2], Nodes[6]])
road6 = Road([Nodes[3], Nodes[7]])
road7 = Road([Nodes[4], Nodes[8]])
road8 = Road([Nodes[5], Nodes[9]])
road9 = Road([Nodes[6], Nodes[10]])
road10 = Road([Nodes[11], Nodes[7]])
road11 = Road([Nodes[7], Nodes[12]])
road12 = Road([Nodes[12], Nodes[8]])
road13 = Road([Nodes[8], Nodes[13]])
road14 = Road([Nodes[13], Nodes[9]])
road15 = Road([Nodes[9], Nodes[14]])
road16 = Road([Nodes[14], Nodes[10]])
road17 = Road([Nodes[10], Nodes[15]])
road18 = Road([Nodes[11], Nodes[16]])
road19 = Road([Nodes[12], Nodes[17]])
road20 = Road([Nodes[13], Nodes[18]])
road21 = Road([Nodes[14], Nodes[19]])
road22 = Road([Nodes[15], Nodes[20]])
road23 = Road([Nodes[21], Nodes[16]])
road24 = Road([Nodes[16], Nodes[22]])
road25 = Road([Nodes[22], Nodes[17]])
road26 = Road([Nodes[17], Nodes[23]])
road27 = Road([Nodes[23], Nodes[18]])
road28 = Road([Nodes[18], Nodes[24]])
road29 = Road([Nodes[24], Nodes[19]])
road30 = Road([Nodes[19], Nodes[25]])
road31 = Road([Nodes[25], Nodes[20]])
road32 = Road([Nodes[20], Nodes[26]])
road33 = Road([Nodes[21], Nodes[27]])
road34 = Road([Nodes[22], Nodes[28]])
road35 = Road([Nodes[23], Nodes[29]])
road36 = Road([Nodes[24], Nodes[30]])
road37 = Road([Nodes[25], Nodes[31]])
road38 = Road([Nodes[26], Nodes[32]])
road39 = Road([Nodes[27], Nodes[33]])
road40 = Road([Nodes[33], Nodes[28]])
road41 = Road([Nodes[28], Nodes[34]])
road42 = Road([Nodes[34], Nodes[29]])
road43 = Road([Nodes[29], Nodes[35]])
road44 = Road([Nodes[35], Nodes[30]])
road45 = Road([Nodes[30], Nodes[36]])
road46 = Road([Nodes[36], Nodes[31]])
road47 = Road([Nodes[31], Nodes[37]])
road48 = Road([Nodes[33], Nodes[38]])
road49 = Road([Nodes[34], Nodes[39]])
road50 = Road([Nodes[35], Nodes[40]])
road51 = Road([Nodes[36], Nodes[41]])
road52 = Road([Nodes[37], Nodes[42]])
road53 = Road([Nodes[43], Nodes[39]])
road54 = Road([Nodes[39], Nodes[44]])
road55 = Road([Nodes[44], Nodes[40]])
road56 = Road([Nodes[40], Nodes[45]])
road57 = Road([Nodes[45], Nodes[41]])
road58 = Road([Nodes[41], Nodes[46]])
road59 = Road([Nodes[46], Nodes[42]])
road60 = Road([Nodes[43], Nodes[47]])
road61 = Road([Nodes[44], Nodes[48]])
road62 = Road([Nodes[45], Nodes[49]])
road63 = Road([Nodes[46], Nodes[50]])
road64 = Road([Nodes[47], Nodes[51]])
road65 = Road([Nodes[51], Nodes[48]])
road66 = Road([Nodes[48], Nodes[52]])
road67 = Road([Nodes[52], Nodes[49]])
road68 = Road([Nodes[49], Nodes[53]])
road69 = Road([Nodes[53], Nodes[50]])
road70 = Road([Nodes[32], Nodes[37]])
road71 = Road([Nodes[43], Nodes[38]])
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
nodedict = {1 : Nodes[0], 2 : Nodes[1], 3 : Nodes[2], 4 : Nodes[3], 5 : Nodes[4], 6 : Nodes[5], 7 : Nodes[6], 8 : Nodes[7], 9 : Nodes[8], 10 : Nodes[9], 11 : Nodes[10], 12 : Nodes[11], 13 : Nodes[12], 14 : Nodes[13], 15 : Nodes[14], 16 : Nodes[15], 17 : Nodes[16], 18 : Nodes[17], 19 : Nodes[18], 20 : Nodes[19], 21 : Nodes[20], 22 : Nodes[21], 23 : Nodes[22], 24 : Nodes[23], 25 : Nodes[24], 26 : Nodes[25], 27 : Nodes[26], 28 : Nodes[27], 29 : Nodes[28], 30 : Nodes[29], 31 : Nodes[30], 32 : Nodes[31], 33 : Nodes[32], 34 : Nodes[33], 35 : Nodes[34], 36 : Nodes[35], 37 : Nodes[36], 38 : Nodes[37], 39 : Nodes[38], 40 : Nodes[39], 41 : Nodes[40], 42 : Nodes[41], 43 : Nodes[42], 44 : Nodes[43], 45 : Nodes[44], 46 : Nodes[45], 47 : Nodes[46], 48 : Nodes[47], 49 : Nodes[48], 50 : Nodes[49], 51 : Nodes[50], 52 : Nodes[51], 53 : Nodes[52], 54 : Nodes[53]}       
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
        for loopnode in Nodes:
            if loopnode == node:
                loopnode.claim(self.color)
    
    def claimroad(self, road):
        for looproad in Roads:
            if looproad == road:
                looproad.claim(self.color)
            
    def makepapa(self, node):
        for peyton in Nodes:
            if peyton == node:
                peyton.makecity(self.color)

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

movelog = open("playerlog.txt", "w")

def turns():
    global turn
    roller()
    for place, obj in playerdict1.items():
        obj.payoff()
        obj.trade()
        build()
        #playDevCard()
        turn += 1
    turns()
            
        
        
        
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
            if P1.resources['bread'] >= 1 and P1.resources['cheese'] >= 1 and P1.resources['pineapple'] >= 1 and P1.resources['sauce'] >= 1:
                P1.claimnode(int(input3))
                P1.resources['bread'] -= 1
                P1.resources['cheese'] -= 1
                P1.resources['pineapple'] -= 1
                P1.resources['sauce'] -= 1
            else:
                print(P1.name, ", you don't enough resources for that!")
                build()
        if turn == 2:
            if P2.resources['bread'] >= 1 and P2.resources['cheese'] >= 1 and P2.resources['pineapple'] >= 1 and P2.resources['sauce'] >= 1:
                P2.claimnode(int(input3))
                P2.resources['bread'] -= 1
                P2.resources['cheese'] -= 1
                P2.resources['pineapple'] -= 1
                P2.resources['sauce'] -= 1
            else:
                print(P2.name, ", you don't have enough resources for that!")
                build()
        if turn == 3:
            if P3.resources['bread'] >= 1 and P3.resources['cheese'] >= 1 and P3.resources['pineapple'] >= 1 and P3.resources['sauce'] >= 1:
                P3.claimnode(int(input3))
                P3.resources['bread'] -= 1
                P3.resources['cheese'] -= 1
                P3.resources['pineapple'] -= 1
                P3.resources['sauce'] -= 1
            else:
                print(P3.name, ", you don't have enough resources for that!")
                build()
        if turn == 4:
            if P4.resources['bread'] >= 1 and P4.resources['cheese'] >= 1 and P4.resources['pineapple'] >= 1 and P4.resources['sauce'] >= 1:
                P4.claimnode(int(input3))
                P4.resources['bread'] -= 1
                P4.resources['cheese'] -= 1
                P4.resources['pineapple'] -= 1
                P4.resources['sauce'] -= 1
            else:
                print(P4.name, ", you don't have enough resources for that!")
                build()
    if input2 == "Road":
        input3 = input("Where would you like to to place this?  ")
        if turn == 1:
            if P1.resources['pineapple'] >= 1 and P1.resources['cheese'] >= 1:
                P1.claimroad(int(input3))
                P1.resources['pineapple'] -= 1
                P1.resources['cheese'] -= 1
            else:
                print(P1.name, ", you don't have enough resources for that!")
                build()
        if turn == 2:
            if P2.resources['pineapple'] >= 1 and P2.resources['cheese'] >= 1:
                P2.claimroad(int(input3))
                P2.resources['pineapple'] -= 1
                P2.resources['cheese'] -= 1
            else:
                print(P2.name, ", you don't have enough resources for that!")
                build()
        if turn == 3:
            if P3.resources['pineapple'] >= 1 and P3.resources['cheese'] >= 1:
                P3.claimroad(int(input3))
                P3.resources['pineapple'] -= 1
                P3.resources['cheese'] -= 1
            else:
                print(P3.name, ", you don't have enough resources for that!")
                build()
        if turn == 4:
            if P4.resources['pineapple'] >= 1 and P4.resources['cheese'] >= 1:
                P4.claimroad(int(input3))
                P4.resources['pineapple'] -= 1
                P4.resources['cheese'] -= 1
            else:
                print(P4.name, ", you don't have enough resources for that!")
                build()
    if input2 == "Papa Johns":
        input3 = input("Where would you like to to place this?  ")
        if turn == 1:
            if P1.resources['ham'] >= 3 and P1.resources['bread'] >= 2:
                P1.makepapa(int(input3))
                P1.resources['ham'] -= 3
                P1.resources['cheese'] -= 2
            else:
                print(P1.name, ", you don't have enough resources for that!")
                build()
        if turn == 2:
            if P2.resources['ham'] >= 3 and P2.resources['bread'] >= 2:
                P2.makepapa(int(input3))
                P2.resources['ham'] -= 3
                P2.resources['cheese'] -= 3
            else:
                print(P2.name, ", you don't have enough resources for that!")
                build()
        if turn == 3:
            if P3.resources['ham'] >= 3 and P3.resources['bread'] >= 2:
                P3.makepapa(int(input3))
                P3.resources['ham'] -= 3
                P3.resources['bread'] -= 2
            else:
                print(P3.name, ", you don't have enough resources for that!")
                build()
        if turn == 4:
            if P4.resources['ham'] >= 3 and P4.resources['bread'] >= 2:
                P4.makepapa(int(input3))
                P4.resources['ham'] -= 3
                P4.resources['bread'] -= 2
            else:
                print(P4.name, ", you don't have enough resources for that!")
                build()

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
            a += 1
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
    
    