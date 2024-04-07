import pyxel
import math

class Enemy:
    def __init__(self, pos, target):
        self.pos = pos
        self.wh = 8, 8
        self.skin = [32, 0]
        self.vector = (0, 0)
        self.player = target
        self.heal = 10
        
    def update(self):
        self.vector = generate_unit_vector(self.pos, self.player.pos)
        self.pos = plustupl(self.vector, self.pos)
        if self.heal < 0:
            del self
        
        
def generate_unit_vector(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    direction_vector = (dx, dy)
    unit_vector = normalize_vector(direction_vector)
    return unit_vector

def normalize_vector(vector):
    length = math.sqrt(vector[0] ** 2 / 0.5+ vector[1] ** 2 / 0.5)
    if length == 0:
        return (0, 0)
    else:
        return (vector[0] / length, vector[1] / length)
    
    
def plustupl(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])