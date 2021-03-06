#Settlers of Catan
import random
import string

class Node:

    """
    This is a class that represents all the nodes on the board.

    Attributes
    ----------
    id : unique identifier of id. mostly for testing.
    resource : resource that the id holds
    claimed : if the node is claimed
    claimedby : who the node is claimed by
    iscity : if the node is a city
    """

    def __init__(self, id, claimed = False, iscity = False):
        """
        Initialize function for the class.
        """
        self.id = id
        self.resource = []
        self.claimed = claimed
        self.claimedby = ""
        self.iscity = iscity 
    
    def claim(self, color):
        """
        Claims nodes for a player

        Arguments
        ---------
        color : color of the player claiming the node
        """
        if canclaim(self, color) == True:
            self.claimed = True
            self.claimedby = color
            for i in playerlist:
                if i.color == color:
                    if i.color == P1.color:
                        P1.vp += 1
                    elif i.color == P2.color:
                        P2.vp += 1
                    elif i.color == P3.color:
                        P3.vp += 1
                    else:
                        P4.vp += 1
        else:
            print("Can't claim")
        
    
    def claimbypass(self, color):
        """
        Claims a node for a player. Mostly for testing.

        Arguments
        ---------
        color : what color is claiming
        """
        self.claimed = True
        self.claimedby = color
        for i in playerlist:
            if i.color == color:
                if i.color == P1.color:
                    P1.vp += 1
                elif i.color == P2.color:
                    P2.vp += 1
                elif i.color == P3.color:
                    P3.vp += 1
                else:
                    P4.vp += 1
    
    def makecity(self, color):
        """
        Makes a city and gives it to the respective player.
        
        Arguments
        ---------
        color : what color is claiming
        """
        if cancity(self, color) == True:
            self.iscity = True 
            for i in playerlist:
                if i.color == color:
                    if i.color == P1.color:
                        P1.vp += 1
                    elif i.color == P2.color:
                        P2.vp += 1
                    elif i.color == P3.color:
                        P3.vp += 1
                    else:
                        P4.vp += 1
            
class Road:
    
    """
    This is the class that represents all the pairs on the board.
    
    Attributes
    ----------
    claimed : if the road is claimed
    nodes : the nodes that the road connects
    claimedby : who the road is claimed by
    """
    def __init__(self, nodes = []):
        """Initializes the whole thing"""
        self.claimed = False
        self.nodes = []
        self.claimedby = ""
    
    def claim(self, color):
        """
        Claims the road for the color.

        Arguments
        ---------
        color : the color who is claiming
        """
        if canclaimroad(self, color) == True:
            self.claimed = True
            self.claimedby = color
        else:
            print("Can't claim")

    def claimbypass(self, color):
        """
        Claims the road for the color. Mostly for testing.
        
        Arguments
        ---------
        color : color to give the road to
        """
        self.claimed = True
        self.claimedby = color
            
class Cluster:

    """
    This is the class for all the hexes on the board.

    Attributes
    ----------
    id : unique identifier of the cluster
    resource : resource the cluster holds
    roads : the roads that the cluster is made of
    isrobber : if the robber occupies that cluster
    tempresource : backup for the resource. used for the robber.
    trigger : number that triggers the cluster to generate
    """

    def __init__(self, isrobber = False):
        self.id = ""        
        self.resource = ""
        self.roads = []
        self.isrobber = isrobber
        self.tempresource = ""
        self.trigger = 0
        
def roller():
    """
    This function acts as the dice. Picks a random number.
    """
    global trigger
    trigger = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

Nodes = []
#These lines create Node objects
for i in range(54):
    Nodes.append(Node(i+1))
    
#The below code creates roads and maps nodes to roads.
road0 = Road()
road0.nodes = [Nodes[3], Nodes[0]]
road1 = Road()
road1.nodes = [Nodes[0], Nodes[4]]
road2 = Road()
road2.nodes = [Nodes[4], Nodes[1]]
road3 = Road()
road3.nodes = [Nodes[1], Nodes[5]]
road4 = Road()
road4.nodes = [Nodes[5], Nodes[2]]
road5 = Road()
road5.nodes = [Nodes[2], Nodes[6]]
road6 = Road()
road6.nodes = [Nodes[3], Nodes[7]]
road7 = Road()
road7.nodes = [Nodes[4], Nodes[8]]
road8 = Road()
road8.nodes = [Nodes[5], Nodes[9]]
road9 = Road()
road9.nodes = [Nodes[6], Nodes[10]]
road10 = Road()
road10.nodes = [Nodes[11], Nodes[7]]
road11 = Road()
road11.nodes = [Nodes[7], Nodes[12]]
road12 = Road()
road12.nodes = [Nodes[12], Nodes[8]]
road13 = Road()
road13.nodes = [Nodes[8], Nodes[13]]
road14 = Road()
road14.nodes = [Nodes[13], Nodes[9]]
road15 = Road()
road15.nodes = [Nodes[9], Nodes[14]]
road16 = Road()
road16.nodes = [Nodes[14], Nodes[10]]
road17 = Road()
road17.nodes = [Nodes[10], Nodes[15]]
road18 = Road()
road18.nodes = [Nodes[11], Nodes[16]]
road19 = Road()
road19.nodes = [Nodes[12], Nodes[17]]
road20 = Road()
road20.nodes = [Nodes[13], Nodes[18]]
road21 = Road()
road21.nodes = [Nodes[14], Nodes[19]]
road22 = Road()
road22.nodes = [Nodes[15], Nodes[20]]
road23 = Road()
road23.nodes = [Nodes[21], Nodes[16]]
road24 = Road()
road24.nodes = [Nodes[16], Nodes[22]]
road25 = Road()
road25.nodes = [Nodes[22], Nodes[17]]
road26 = Road()
road26.nodes = [Nodes[17], Nodes[23]]
road27 = Road()
road27.nodes = [Nodes[23], Nodes[18]]
road28 = Road()
road28.nodes = [Nodes[18], Nodes[24]]
road29 = Road()
road29.nodes = [Nodes[24], Nodes[19]]
road30 = Road()
road30.nodes = [Nodes[19], Nodes[25]]
road31 = Road()
road31.nodes = [Nodes[25], Nodes[20]]
road32 = Road()
road32.nodes = [Nodes[20], Nodes[26]]
road33 = Road()
road33.nodes = [Nodes[21], Nodes[27]]
road34 = Road()
road34.nodes = [Nodes[22], Nodes[28]]
road35 = Road()
road35.nodes = [Nodes[23], Nodes[29]]
road36 = Road()
road36.nodes = [Nodes[24], Nodes[30]]
road37 = Road()
road37.nodes = [Nodes[25], Nodes[31]]
road38 = Road()
road38.nodes = [Nodes[26], Nodes[32]]
road39 = Road()
road39.nodes = [Nodes[27], Nodes[33]]
road40 = Road()
road40.nodes = [Nodes[33], Nodes[28]]
road41 = Road()
road41.nodes = [Nodes[28], Nodes[34]]
road42 = Road()
road42.nodes = [Nodes[34], Nodes[29]]
road43 = Road()
road43.nodes = [Nodes[29], Nodes[35]]
road44 = Road()
road44.nodes = [Nodes[35], Nodes[30]]
road45 = Road()
road45.nodes = [Nodes[30], Nodes[36]]
road46 = Road()
road46.nodes = [Nodes[36], Nodes[31]]
road47 = Road()
road47.nodes = [Nodes[31], Nodes[37]]
road48 = Road()
road48.nodes = [Nodes[33], Nodes[38]]
road49 = Road()
road49.nodes = [Nodes[34], Nodes[39]]
road50 = Road()
road50.nodes = [Nodes[35], Nodes[40]]
road51 = Road()
road51.nodes = [Nodes[36], Nodes[41]]
road52 = Road()
road52.nodes = [Nodes[37], Nodes[42]]
road53 = Road()
road53.nodes = [Nodes[43], Nodes[39]]
road54 = Road()
road54.nodes = [Nodes[39], Nodes[44]]
road55 = Road()
road55.nodes = [Nodes[44], Nodes[40]]
road56 = Road()
road56.nodes = [Nodes[40], Nodes[45]]
road57 = Road()
road57.nodes = [Nodes[45], Nodes[41]]
road58 = Road()
road58.nodes = [Nodes[41], Nodes[46]]
road59 = Road()
road59.nodes = [Nodes[46], Nodes[42]]
road60 = Road()
road60.nodes = [Nodes[43], Nodes[47]]
road61 = Road()
road61.nodes = [Nodes[44], Nodes[48]]
road62 = Road()
road62.nodes = [Nodes[45], Nodes[49]]
road63 = Road()
road63.nodes = [Nodes[46], Nodes[50]]
road64 = Road()
road64.nodes = [Nodes[47], Nodes[51]]
road65 = Road()
road65.nodes = [Nodes[51], Nodes[48]]
road66 = Road()
road66.nodes = [Nodes[48], Nodes[52]]
road67 = Road()
road67.nodes = [Nodes[52], Nodes[49]]
road68 = Road()
road68.nodes = [Nodes[49], Nodes[53]]
road69 = Road()
road69.nodes = [Nodes[53], Nodes[50]]
road70 = Road()
road70.nodes = [Nodes[32], Nodes[37]]
road71 = Road()
road71.nodes = [Nodes[43], Nodes[38]]
#The below code invokes clusters. Allocates roads to clusters.
Cluster1 = Cluster()
Cluster1.roads = [road0, road6, road11, road12, road7, road1]
Cluster1.id = 1
Cluster2 = Cluster()
Cluster2.id = 2
Cluster2.roads = [road3, road8, road14, road13, road7, road2]
Cluster3 = Cluster()
Cluster3.roads = [road5, road9, road16, road15, road8, road4]
Cluster3.id = 3
Cluster4 = Cluster()
Cluster4.id = 4
Cluster4.roads = [road11, road19, road25, road24, road18, road10]
Cluster5 = Cluster()
Cluster5.id = 5
Cluster5.roads = [road13, road20, road27, road26, road19, road12]
Cluster6 = Cluster()
Cluster6.id = 6
Cluster6.roads = [road15, road21, road29, road28, road20, road14]
Cluster7 = Cluster()
Cluster7.id = 7
Cluster7.roads = [road17, road22, road31, road30, road21, road16]
Cluster8 = Cluster()
Cluster8.id = 8
Cluster8.roads = [road24, road34, road40, road39, road33, road23]
Cluster9 = Cluster()
Cluster9.id = 9
Cluster9.roads = [road26, road35, road42, road41, road34, road25]
Cluster10 = Cluster()
Cluster10.id = 10
Cluster10.roads = [road28, road36, road44, road43, road35, road27]
Cluster11 = Cluster()
Cluster11.id = 11
Cluster11.roads = [road30, road37, road46, road45, road36, road29]
Cluster12 = Cluster()
Cluster12.id = 12
Cluster12.roads = [road32, road38, road70, road47, road37, road31]
Cluster13 = Cluster()
Cluster13.id = 13
Cluster13.roads = [road41, road49, road53, road71, road48, road40]
Cluster14 = Cluster()
Cluster14.id = 14
Cluster14.roads = [road43, road50, road55, road54, road49, road42]
Cluster15 = Cluster()
Cluster15.id = 15
Cluster15.roads = [road45, road51, road57, road56, road50, road44]
Cluster16 = Cluster()
Cluster16.id = 16
Cluster16.roads = [road47, road52, road59, road58, road52, road46]
Cluster17 = Cluster()
Cluster17.id = 17
Cluster17.roads = [road54, road61, road65, road64, road60, road53]
Cluster18 = Cluster()
Cluster18.id = 18
Cluster18.roads = [road56, road62, road67, road66, road61, road66]
Cluster19 = Cluster()
Cluster19.id = 19
Cluster19.roads = [road58, road63, road69, road68, road62, road57]
clusters = [Cluster1, Cluster2, Cluster3, Cluster4, Cluster5, Cluster6, Cluster7, Cluster8, Cluster9, Cluster10, Cluster11, Cluster12, Cluster13, Cluster14, Cluster15, Cluster16, Cluster17, Cluster18, Cluster19]
Roads = [road0, road1, road2, road3, road4, road5, road6, road7, road8, road9, road10, road11, road12, road13, road14, road15, road16, road17, road18, road19, road20, road21, road22, road23, road24, road25, road26, road27, road28, road29, road30, road31, road32, road33, road34, road35, road36, road37, road38, road39, road40, road41, road42, road43, road44, road45, road46, road47, road48, road49, road50, road51, road52, road53, road54, road55, road56, road57, road58, road59, road60, road61, road62, road63, road64, road65, road66, road67, road68, road69, road70, road71]
nodedict = {1 : Nodes[0], 2 : Nodes[1], 3 : Nodes[2], 4 : Nodes[3], 5 : Nodes[4], 6 : Nodes[5], 7 : Nodes[6], 8 : Nodes[7], 9 : Nodes[8], 10 : Nodes[9], 11 : Nodes[10], 12 : Nodes[11], 13 : Nodes[12], 14 : Nodes[13], 15 : Nodes[14], 16 : Nodes[15], 17 : Nodes[16], 18 : Nodes[17], 19 : Nodes[18], 20 : Nodes[19], 21 : Nodes[20], 22 : Nodes[21], 23 : Nodes[22], 24 : Nodes[23], 25 : Nodes[24], 26 : Nodes[25], 27 : Nodes[26], 28 : Nodes[27], 29 : Nodes[28], 30 : Nodes[29], 31 : Nodes[30], 32 : Nodes[31], 33 : Nodes[32], 34 : Nodes[33], 35 : Nodes[34], 36 : Nodes[35], 37 : Nodes[36], 38 : Nodes[37], 39 : Nodes[38], 40 : Nodes[39], 41 : Nodes[40], 42 : Nodes[41], 43 : Nodes[42], 44 : Nodes[43], 45 : Nodes[44], 46 : Nodes[45], 47 : Nodes[46], 48 : Nodes[47], 49 : Nodes[48], 50 : Nodes[49], 51 : Nodes[50], 52 : Nodes[51], 53 : Nodes[52], 54 : Nodes[53]}       
roaddict = {0 : road0, 1 : road1, 2 : road2, 3 : road3, 4 : road4, 5 : road5, 6 : road6, 7 : road7, 8 : road8, 9 : road9, 10 : road10, 11 : road11, 12 : road12, 13 : road13, 14 : road14, 15 : road15, 16 : road16, 17 : road17, 18 : road18, 19 : road19, 20 : road20, 21 : road21, 22 : road22, 23 : road23, 24 : road24, 25 : road25, 26 : road26, 27 : road27, 28 : road28, 29 : road29, 30 : road30, 31 : road31, 32 : road32, 33 : road33, 34 : road34, 35 : road35, 36 : road36, 37 : road37, 38 : road38, 39 : road39, 40 : road40, 41 : road41, 42 : road42, 43 : road43, 44 : road44, 45 : road45, 46 : road46, 47 : road47, 48 : road48, 49 : road49, 50 : road50, 51 : road51, 52 : road52, 53 : road53, 54 : road54, 55 : road55, 56 : road56, 57 : road57, 58 : road58, 59 : road59, 60 : road60, 61 : road61, 62 : road62, 63 : road63, 64 : road64, 65 : road65, 66 : road66, 67 : road67, 68 : road68, 69 : road69, 70 : road70, 71 : road71}
class Player:

    """
    This class manages Players.

    Attributes
    ----------
    name : name of player
    color : color of player
    position : position in the rotation
    resources : how many resources the player has.
    development : how many development cards the player has
    nodes : how many nodes the player has
    roads : how many roads the player has built
    knights : how many knights the player owns
    vp : victory points the player has
    """

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
        self.nodes = []
        self.roads = []
        self.knights = 0
        self.vp = 0
        self.received = []
        
    def trade(self, r1, r2, r3, r4, amount1, amount2, amount3, amount4):
        """
        Trades between players.
        
        Arguments:
        r1 : first resource
        r2 : second resource
        r3 : third resource
        r4 : fourth resource
        amount1 : first amount (corresponds to r1)
        amount2 : second amount (corresponds to r2)
        amount3 : third amount (corresponds to r3)
        amount4 : fourth amount (corresponds to r4)
        """
        input1 = ""
        input3 = ""
        input2 = ""
        if amount3 == 0 and amount4 == 0 and r3 == 0 and r4 == 0:
            print(self.name, "Wishes to trade ", amount1, r1, "for", amount2, r2, ", Does any player wish to accept?")
        else:
            print(self.name, "Wishes to trade ", amount1, r1, "and", amount3, r3, "for", amount2, r2, "and", amount4, r4)
            input1 = input("Does any player wish to accept?")
        while input1 != "yes" and input1 != "no":
            input1 = input("Does any player wish to accept?")
        if input1 == "yes":
            input3 = input("Please indicate the number of the player who wishes to accept the trade: ")
            while int(input3) != 1 and int(input3) != 2 and int(input3) != 3 and int(input3) != 4:
                input3 = input("Please indicate the number of the player who wishes to accept the trade: ")
            input2 = int(input3)
            if self.resources[r1] >= amount1 and self.resources[r3] >= amount3 and playerdict1[int(input2)].resources[r2] >= amount2 and playerdict1[int(input2)].resources[r4] >= amount4:
                self.resources[r1] = self.resources[r1] - amount1
                self.resources[r3] = self.resources[r3] - amount3
                self.resources[r2] = self.resources[r2] + amount2
                self.resources[r4] = self.resources[r4] + amount4
                playerdict1[int(input2)].resources[r2] = playerdict1[int(input2)].resources[r2] - amount2
                playerdict1[int(input2)].resources[r4] = playerdict1[int(input2)].resources[r4] - amount4
                playerdict1[int(input2)].resources[r1] = playerdict1[int(input2)].resources[r1] + amount1
                playerdict1[int(input2)].resources[r3] = playerdict1[int(input2)].resources[r3] + amount3
            else:
                print("You are dumb")
        else:
            print("Nothing was traded!")

    
    def KnightsToVictory(self, knights, vp):
        """
        Checks if the player has 3 knights. If so, they get 2 victory points.

        Arguments
        ---------
        knights : how many knights
        vp : how many victory points
        """
        if self.knights == 3:
            self.vp += 2
        
        
    def payoff(self):
        """
        Checks if the player owns a node that borders a hex that is producing.
        """
        for cluster in clusters:
            if cluster.trigger == trigger:
                if cluster.resource == "ham":
                    self.received.append("one ham")
                    self.resources['ham'] += 1
                elif cluster.resource == "pineapple":
                    self.resources['pineapple'] += 1
                    self.received.append("one pineapple")
                elif cluster.resource == "bread":
                    self.resources['bread'] += 1
                    self.received.append("one bread")
                elif cluster.resource == "cheese":
                    self.resources['cheese'] += 1
                    self.received.append("one cheese")
                elif cluster.resource == "sauce":
                    self.received.append("one sauce")
                    self.resources['sauce'] += 1
        if self.received == []:
            self.received = "nothing"
    
    def claimnode(self, node):
        """
        claims a node to the player if the color owns it.

        Arguments
        ---------
        node : what node is being claimed
        """
        for loopnode in Nodes:
            if loopnode == node:
                loopnode.claim(self.color)
    
    def claimroad(self, road):
        """
        claims a road to the player if the color owns it.

        Arguments
        ---------
        road : what road is being claimed
        """
        for looproad in Roads:
            if looproad == road:
                looproad.claim(self.color)
            
    def makepapa(self, node):
        """
        creates a papa johns if a papa johns can be made.

        Arguments
        ---------
        node : where the papa johns is being built
        """
        for peyton in Nodes:
            if peyton == node:
                peyton.makecity(self.color)

class Devcard:
    
    """
    Manages development cards. !!!NOT IMPLEMENTED!!!

    Attributes
    ----------
    variant : what kind of card the dev card is.
    """

    def __init__(self, variant):
        """
        Initializes the class with the argument variant.
        
        Arguments
        ---------
        variant : what kind of card the development card is
        """
        self.variant = variant 
        
    def monopoly(self, color):
        """
        The monopoly card allows the player to grab all the resources.
        
        Arguments
        ---------
        color : what color the player is
        
        Globals
        -------
        playerlist : list of all players. used in order for a for loop traversal.
        """
        global playerlist
        if self.variant == "monopoly":
            colors = []
            for i in playerlist:
                colors.append(i.color)
            colors.remove(color)
            input1 = input("What resource do you want all of, you greedy swine? ")
            while input1.lower() != "ham" and input1.lower() != "pineapple" and input1.lower() != "cheese" and input1.lower() != "sauce" and input1.lower() != "bread":
                input1 = input("What resource do you want all of, you greedy swine? ")
            total = 0
            players = []
            for i in playerlist:
                players.append(i)
            for i in playerlist:
                if i.color == color:
                    players.remove(i)
                    for y in players:
                        total += y.resources[input1]
                        y.resources[input1] -= y.resources[input1]
                    i.resources[input1] += total
                    
    def vp(self, color):
        """
        Allows the player to use a victory point card, and gain one victory point.
        
        Arguments
        ---------
        color : color of player

        Globals
        -------
        playerlist : list of players
        """
        global playerlist
        if self.variant == "vp":
            for i in playerlist:
                if i.color == color:
                    i.vp += 1

    def knight(self):
        """
        Allows the player to pull the knight card. Moves the robber.

        Globals
        -------
        robber_loc : location of robber.
        """
        global robber_loc
        if self.variant == "knight":
            hamburglar_newloc = int(input("Where would you like to move the hamburglar?"))
            relevant_var = hamburglar_newloc - 1
            robber_loc = False
            clusters[relevant_var].isrobber = True
            for cluster in clusters:
                for road in cluster.roads:
                    for node in road.nodes:
                        if cluster == clusters[relevant_var]:
                            if node.claimed == True:
                                for player in playerlist:
                                    if player.color == node.claimedby:
                                        resourcetaken = random.choice(["ham", "pineapple", "bread", "sauce", "cheese"])
                                        player.resources[resourcetaken] -= 1
                                        Player.resources[resourcetaken] += 1
                                        Player.knights += 1
                                        
    def roadbuilding(self, color):
        """
        Mainly for testing. Builds roads.
        
        Arguments
        ---------
        color : who owns the roads
        """
        global playerlist
        input1 = int(input("Where would you like to put your first road? "))
        input2 = int(input("Where would you like to put your second road? "))
        while input1 > 73 or input1 < 0 or input1 > 73 or input1 < 0:
            input1 = int(input("Where would you like to put your first road? "))
            input2 = int(input("Where would you like to put your second road? "))
        for i in playerlist:
                if i.color == color:
                    i.claimroad(input1)
                    i.claimroad(input2)
                                        
                                        

def play():
    """
    Prompts for how many players to start code.
    
    Globals
    -------
    numplayers : decides how many players are in the game
    """

    global numplayers
    input1 = input("How Many Players?:   ")
    numplayers = input1
    return str(input1)

numplayers = 0
colors = ['red', 'blue', 'white', 'orange', 'green', 'brown']
playernames = [] 
playercolor = [] 
playerposition = []
turn = 1
playerlist = []      

def makelist():
    """
    Creates a list of players depending on how many players are present in the game.

    Globals
    -------
    playerlist : list of player objects
    """
    global playerlist
    if numplayers == '3':
        playerlist = [P1, P2, P3]
    elif numplayers == '2':
        playerlist = [P1, P2]
    else:
        playerlist = [P1, P2, P3, P4]      
    
def init():
    """
    Begins code depending on how many players. Maps players to numbers.

    Globals
    -------
    P1 : player 1 object
    P2 : player 2 object
    P3 : player 3 object
    P4 : player 4 object
    playerdict : mapping players to numbers
    playerdict1 : mapping players to numbers the other way
    """
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
    """
    Prompts for input to create player classes and attribute color and name to players.

    Globals
    -------
    playernames : list of player names
    colors : list of all colors

    Arguments
    ---------
    string : amount of players in the game. deduced from play()
    """
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
    """
    Randomly assigns resources to certain hexes.

    Globals
    -------
    desert_loc : tracks where the desert is
    """
    global desert_loc
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
    for cluster in clusters:
        cluster.resource = usedResources[clusters.index(cluster)]
        if cluster.resource == "desert":
            cluster.trigger == 7
            
usedID = []
IDGenned = []
ClustersForMapping = [Cluster1, Cluster2, Cluster3, Cluster4, Cluster5, Cluster6, Cluster7, Cluster8, Cluster9, Cluster10, Cluster11, Cluster12, Cluster13, Cluster14, Cluster15, Cluster16, Cluster17, Cluster18, Cluster19]

def InitialHexTriggerRandomizer():
    """
    Randomly assigns triggers to each hex. Always assigns 7 to the desert.
    """
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
    for cluster in ClustersForMapping:
        if cluster.resource == 'desert':
            cluster.trigger = 7
            ClustersForMapping.pop(ClustersForMapping.index(cluster))
        else:
            for ID in IDGenned:
                cluster.trigger = IDGenned[ClustersForMapping.index(cluster)]

def isNeighbor(point1, point2):
    """
    Checks if two points neighbor each other.
    
    Arguments
    ---------
    point1 : the first point
    point2 : the second point
    """
    for road in Roads:
        if [point1, point2] == road.nodes:
            return True
        if [point2, point1] == road.nodes:
            return True
    
def ClusterToNode():
    """
    Assigns cluster attributes to nodes.
    
    Globals
    -------
    robber_loc : location of robber
    """
    global robber_loc
    for cluster in clusters:
        for road in cluster.roads:
            for node in road.nodes:
                node.resource.append(cluster.resource)
                if cluster.isrobber == True:
                    robber_loc = True
                    cluster.tempresource = clusters.resource
                    cluster.resource = ""
                if cluster.isrobber == False:
                    if cluster.resource == "":
                        cluster.resource = clusters.tempresource   
                        node.isrobber = cluster.isrobber          
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
    """
    Tests if road can be claimed.

    Arguments
    ---------
    roadr : the road looking to be claimed
    color : the color by which the road is going to be claimed
    """
    a = False
    for roads in Roads:
        if roads.claimed == True and roads.claimedby == color:
            for node in roads.nodes:
                for node1 in roadr.nodes:
                    if node == node1:
                        a = True
    return a
    
def canclaim(noder, color):
    """
    Tests if the node can be claimed.

    Arguments
    ---------
    noder : the node looking to be claimed
    color : the color of which the node is going to be claimed
    """
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
    """
    Checks if the city can be built on the specified node.
    
    Arguments
    ---------
    noder : the node looking to have a newly built city
    color : the color of the player doing the whole thing
    """
    if noder.claimedby == color:
        return True
    else:
        print("Can't Papa")
        return False
 
def build(): #Needs to be finished
    """
    Prompts user for input, checks if they have the resource, builds accordingly.

    Globals
    -------
    turn : checks which turn it is.
    """
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

def trade():
    """
    Sets up trades between players.
    
    Globals
    -------
    turn : checks which player is actively doing things.
    """
    global turn
    input5 = ""
    input6 = ""
    input10 = ""
    input11 = ""
    while validresource(input5) == False:
        input5 = input("What resource do you wish to offer?   ")
    while validresource(input6) == False:
        input6 = input("What resource do you wish to receive?   ")
    input7 = input("How many " + input5 + " do you wish to offer?   ")
    input8 = input("How many " + input6 + " do you wish to receive?   ")
    input9 = input("Would you like to add another resource to your offer? (yes / no)   ")
    while input9.lower() != "yes" and input9.lower() != "no":
        input9 = input("Would you like to add another resource to your offer? (yes / no)   ")
    if input9.lower() == "yes":
        while validresource(input10) == False:
            input10 = input("What second resource do you wish to offer?   ")
        while validresource(input11) == False:
            input11 = input("What second resource do you wish to receive?   ")
        input12 = input("How many " + input10 + " do you wish to offer?   ")
        input13 = input("How many " + input11 + " do you wish to receive?   ")
        if turn == 1:
            P1.trade(input5, input6, input10, input11, int(input7), int(input8), int(input12), int(input13))
        elif turn == 2:
            P2.trade(input5, input6, input10, input11, int(input7), int(input8), int(input12), int(input13))
        elif turn == 3:
            P3.trade(input5, input6, input10, input11, int(input7), int(input8), int(input12), int(input13))
        elif turn == 4:
            P4.trade(input5, input6, input10, input11, int(input7), int(input8), int(input12), int(input13))
    elif input9.lower() == "no": 
        if turn == 1:
            P1.trade(input5, input6, 0, 0, int(input7), int(input8), 0, 0)
        elif turn == 2:
            P2.trade(input5, input6, 0, 0, int(input7), int(input8), 0, 0)
        elif turn == 3:
            P3.trade(input5, input6, 0, 0, int(input7), int(input8), 0, 0)
        elif turn == 4:
            P4.trade(input5, input6, 0, 0, int(input7), int(input8), 0, 0)

def validresource(a):
    """
    Checks if given input is a valid resource. Sanitizes input.

    Arguments
    ---------
    a : input of the user. 
    """
    if a.lower() == "ham" or a.lower() == "pineapple" or a.lower() == "sauce" or a.lower() == "bread" or  a.lower() == "cheese":
        return True
    else:
        return False

def initialize(n):
    """
    Initializes game, places starter settlements and roads. Part 1.

    Arguments
    ---------
    n : how many players
    """
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
    """
    Initializes game, places starter settlements and roads. Part 2.

    Arguments
    ---------
    n : how many players
    """
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
    """
    Checks how many nodes are owned by a color.

    Argument
    --------
    color : which color to test how many nodes are claimed
    """
    a = 0
    for node in Nodes:
        if node.claimedby == color:
            a += 1
    return a
            
def haswon():
    """
    Checks if anyone has won.
    """
    for i in playerlist:
        if i.vp == 10:
            print("Congratulations, " + i.name + "!!! You have just won the game!")            
            
def hamburglar():
    """
    Triggers the robber.
    """
    if cluster.isrobber == True:
        cluster.tempresource = clusters.resource
        cluster.resource = ""
    if cluster.isrobber == False:
        if cluster.resource == "":
            cluster.resource = clusters.tempresource            

def move_hamburglar():
    """
    Moves the robber if a 7 is rolled.
    """
    if trigger == 7:
        hamburglar_newloc = int(input("Where would you like to move the hamburglar?"))
        relevant_var = hamburglar_newloc - 1
        robber_loc = False
        clusters[relevant_var].isrobber = True
        
def turns():
    """
    Moderates turns.

    Globals
    -------
    turn : which player is active.
    """
    global turn
    roller()
    print("The Dice has been rolled and resources have been given!")
    for player in playerlist:
        print(player.name + " " + "got " + " ".join(player.received))
    for place, obj in playerdict1.items():
        obj.payoff()
        move_hamburglar()
        trade()
        obj.trade()
        build()
        haswon()
        #playDevCard()
        if turn >= 4:
            turn == 1
        else:
            turn += 1
    turns()
    




InitialHexResourceRandomizer()
InitialHexTriggerRandomizer()
ClusterToNode()
playerinput(play())
makelist()
initialize(int(numplayers))
initializepart2(int(numplayers))
turns()