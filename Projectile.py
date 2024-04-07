import math
from BigBrain import check_collition

class Projectile:
    
    def __init__(self, pos, vector, target, ToDraw):
        self.pos = pos
        self.wh = 2, 2
        self.skin = [24, 0]
        self.vector = vector
        self.target = target
        self.ToDraw = ToDraw
    def update(self):
        self.pos = plustupl(self.vector, self.pos)
        for enemy in self.target:
            if check_collition([enemy.pos, enemy.wh], [self.pos, self.wh]):
                self.ToDraw.delete_object(self)
                enemy.heal -= 1

class ProjectileSpin:
    def __init__(self, pos, vector):
        self.pos = pos
        self.wh = 2, 2
        self.skin = [24, 0]
        self.vector = vector
        self.centre = pos
        self.ray = 5
        self.angle = 0
    def update(self):
        self.pos = self.pos[0] + self.ray * math.cos(self.angle), self.pos[1] + self.ray * math.sin(self.angle)
        self.pos = plustupl(self.vector, self.pos)
        self.angle = self.angle + 0.5
        if self.angle > 360:
            self.angle = 0

class SpiningProjectile:
    def __init__(self, pos, vector):
        self.pos = pos
        self.centre = pos
        self.wh = 2, 2
        self.skin = [24, 0]
        self.angle = 0
        self.ray = 10
        
    def update(self):
        self.pos = self.centre[0] + self.ray * math.cos(self.angle), self.centre[1] + self.ray * math.sin(self.angle)
        self.angle = self.angle + 1
        if self.angle > 360:
            self.angle = 0



def plustupl(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])