#%% Empty Declaration

class hand:
    def __init__(self):
        return(None)

h = hand()
h.index = 0
h.middle = 0
h.ring = 0
h.pinky = 0

print(vars(h))

#%% + Defined Properties


class hand:
    def __init__(self):
        self.index = 0
        self.middle = 0
        self.ring = 0
        self.pinky = 0
        self.thumb = 0
        
#%% + Assignment funtion

class hand:
    def __init__(self):
        self.index = 0
        self.middle = 0
        self.ring = 0
        self.pinky = 0
        self.thumb = 0
        
    def __Assign(self, assignvec):
        self.thumb = assignvec[0]
        self.index = assignvec[1]
        self.middle = assignvec[2]
        self.ring = assignvec[3]
        self.pinky = assignvec[4]
        
    def Okay(self):
        self.__Assign([0,0,1,1,1])        
        
        
# Private Function:
h = hand()
h.__Assign([0,0,0,0,0]) # This will not work!
    
# Question: Add the following methods:
# Marry
# Point
        
#%% + Report

class hand:
    def __init__(self):
        self.index = 0
        self.middle = 0
        self.ring = 0
        self.pinky = 0
        self.thumb = 0
        
    def __Assign(self, assignvec):
        self.thumb = assignvec[0]
        self.index = assignvec[1]
        self.middle = assignvec[2]
        self.ring = assignvec[3]
        self.pinky = assignvec[4]
        
    def Okay(self):
        self.__Assign([0,0,1,1,1])        
    
    def Report(self):
        print(self.thumb,self.index,self.middle,self.ring,self.pinky)        
    
    def __repr__(self):
        return "{},{},{},{},{}".format(self.thumb,self.index,self.middle,self.ring,self.pinky)
    
    def __str__(self):
        str1 = "This is my hand."
        str2 = "{},{},{},{},{}".format(self.thumb,self.index,self.middle,self.ring,self.pinky)
        return str1 + '\n' + str2

h = hand()
h.Okay()
h.Report()
print(h)
h

#%% Questions

# Create a handshake function that sets two hands to a handshake position = [0,1,1,1,1]