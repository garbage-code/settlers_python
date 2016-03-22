#Settlers of Catan
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
    
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
        
    def isturn(self, turn): #Global turn must be implemented
        if self.position == turn:
            return True
        else:
            return False

