import pyxel
import random
from Player import Player
from Projectile import ProjectileSpin
from Projectile import Projectile
from Enemy import Enemy



import math

asshoot = False

class ObjectList:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def delete_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
        else:
            print("Object not found in the list.")




class App:
    def __init__(self):
        pyxel.init(160, 160, title="SuperUltraMegaGame")
        pyxel.load("awsome.pyxres")
        pyxel.run(self.update, self.draw)  
        
    def update(self):
        global asshoot
        if pyxel.btn(pyxel.KEY_D):
            player1.mouve('Right')
            player1.state = "Active"
            counter = 0
            
        if pyxel.btn(pyxel.KEY_S):
            player1.mouve("Down")
            player1.state = "Active"
            counter = 0
            
        if pyxel.btn(pyxel.KEY_Q):
            player1.mouve('Left')
            player1.state = "Active"
            counter = 0
            
        if pyxel.btn(pyxel.KEY_Z):
            player1.mouve("Up")
            player1.state = "Active"
            counter = 0
                       
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and asshoot == False:
            unit_vector = generate_unit_vector(player1.pos, [pyxel.mouse_x, pyxel.mouse_y])
            newproj = Projectile(plustupl(player1.pos, (3, 3)), unit_vector, enemys, ToDraw)
            ToDraw.add_object(newproj)
            asshoot = True
            
        if not pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and asshoot == True:
            asshoot = False
            
        if not pyxel.btn(pyxel.KEY_Z) and not pyxel.btn(pyxel.KEY_D) and not pyxel.btn(pyxel.KEY_S) and not pyxel.btn(pyxel.KEY_Q):
            player1.mouving = False
            
        player1.update()
        
        
        for object in ToDraw.objects:
            if type(object) == Projectile or type(object) == ProjectileSpin:
                object.update()
            
        for enemy in enemys:
            enemy.update()
                
        player1.counter += 1
        
        if random.randint(0, 12) == 12:
            enm = Enemy((random.randint(0, 160), random.randint(0, 160)), player1)
            ToDraw.add_object(enm)
            enemys.append(enm)
        
        if player1.counter > 100:
            player1.skins[0] = "Passive"
            player1.counter = 0

    def draw(self):
        
        pyxel.cls(0)
        for object in ToDraw.objects:
            pyxel.blt(object.pos[0], object.pos[1], 0, object.skin[0], object.skin[1], object.wh[0], object.wh[1], 0)
        
        #cusor
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 24, 8, 5, 5, 0)
    
def plustupl(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
    
def generate_unit_vector(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    direction_vector = (dx, dy)
    unit_vector = normalize_vector(direction_vector)
    return unit_vector
    
def normalize_vector(vector):
    length = math.sqrt(vector[0] ** 2 / 4+ vector[1] ** 2 / 4)
    if length == 0:
        return (0, 0)
    else:
        return (vector[0] / length, vector[1] / length)
    

ToDraw = ObjectList()
player1 = Player([1, 5])
enemy1 = Enemy((5, 1), player1)
enemys = [enemy1]
projecticle = Projectile([1, 0], [1, 0], enemys, ToDraw)

ToDraw.add_object(player1)
ToDraw.add_object(enemy1)
ToDraw.add_object(projecticle)
App()