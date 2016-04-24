class Mold:

    
    def __init__(self, bd):

        self.basicDamage = bd

    def setBasicDamage(self, bd):
        if bd >= 0:
            self.basicDamage = bd
        else:
            self.basicDamage = 0
            
    def getBasicDamage(self):
        return self.basicDamage
        
