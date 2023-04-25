import pyxel
import random

enemies =[]
class Enemy:
    def __init__(self, x, y, u, v, h, w, dir, sx, sy):
        # 表示位置の座標を示す変数
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.h = h
        self.w = w
        self.dir = dir
        self.sx = sx 
        self.sy = sy  

    def check_wall(self):
        # 進める方向の確認
        left = pyxel.pget(self.x-1,self.y+7) != 3 and pyxel.pget(self.x-1,self.y+8) != 3
        right = pyxel.pget(self.x+16,self.y+7) != 3 and pyxel.pget(self.x+16,self.y+8) != 3
        up = pyxel.pget(self.x+7,self.y-1) != 3 and pyxel.pget(self.x+8,self.y-1) != 3
        down = pyxel.pget(self.x+7,self.y+16) != 3 and pyxel.pget(self.x+8,self.y+16) != 3
        dir_list = {'left':left,'right':right,'up':up,'down':down}

        if self.dir == 'left':
            if left:
                return 'left'
        elif self.dir == 'right':
            if right:
                return 'right'         
        elif self.dir == 'up':
            if up:
                return 'up'  
        elif self.dir == 'down':
            if down:
                return 'down'
        else:
            keys = [k for k, v in dir_list.items() if v]
            return random.choice(keys)

    def update(self):
        self.dir = self.check_wall()
        if self.dir == 'left':
            self.x -= 8
        elif self.dir == 'right':
            self.x += 8
        elif self.dir == 'up':
            self.y -= 8
        elif self.dir == 'down':
            self.y += 8

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v+16*(pyxel.frame_count % 2), self.w, self.h, 0)

