class Player:
    def __init__(self, pos):
        self.pos = pos
        self.wh = 8, 8
        self.mouving = False
        self.dirrection = None
        
        self.skin = [0, 0]
        self.skins = ['Passive', 0]
        self.skin_list = {
            "Passive" : ([16, 0], [16, 8]),
            "Left" : ([8, 0], [8, 8], [8, 16]),
            "Right" :([0, 0], [0, 8], [0, 16])
        }

        
        self.speed = 1
        self.counter = 0
        self.counter2 = 0

    def mouve(self, dirrection):
        
        self.pos = [self.pos[0] + (1 if dirrection == 'Right' else -1 if dirrection == 'Left' else 0), self.pos[1] + (1 if dirrection == 'Down' else -1 if dirrection == 'Up' else 0)]
        print(self.pos)
        
        dirrection = None if dirrection == 'Down' or dirrection == 'Up' else dirrection
        self.skins[1] += 1
        self.skins[0] = dirrection if dirrection != None else self.skins[0]
        if self.skins[1] >= len(self.skin_list[self.skins[0]]):
            self.skins[1] = 0
        self.skin = self.skin_list[self.skins[0]][self.skins[1]]
        
        



    def update(self):
        if self.skins[0] == 'Passive':
            self.counter2 += 1
            if self.counter2 > 20:
                self.counter2 = 0
                self.skins[1] += 1
                if self.skins[1] >= len(self.skin_list[self.skins[0]]):
                    self.skins[1] = 0
                self.skin = self.skin_list[self.skins[0]][self.skins[1]]
        
