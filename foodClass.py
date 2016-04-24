class Food:
    def __init__(self, hp):

        self.hitPoints = hp

    def setHitPoints(self, hp):
        if hp >= 0:
            self.hitPonts = hp
        else:
            self.hitPoints = 0

    def getHitPoints(self):
        return self.hitPoints

