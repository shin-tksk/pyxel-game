import pyxel
import random

enemies = [] 

class Player:
    def __init__(self, x, y, u, v, h, w):
        # 表示位置の座標を示す変数
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.h = h
        self.w = w

    def update(self):
        # キーボード入力を座標に反映（*壁をすり抜けないように）
        if pyxel.btnp(pyxel.KEY_LEFT, hold=1, repeat=1):
            if pyxel.pget(self.x-1,self.y+7) != 3 and pyxel.pget(self.x-1,self.y+8) != 3:
                self.x -= 8
        elif pyxel.btnp(pyxel.KEY_RIGHT, hold=1, repeat=1):
            if pyxel.pget(self.x+16,self.y+7) != 3 and pyxel.pget(self.x+16,self.y+8) != 3:
                self.x += 8
        elif pyxel.btnp(pyxel.KEY_UP, hold=1, repeat=1):
            if pyxel.pget(self.x+7,self.y-1) != 3 and pyxel.pget(self.x+8,self.y-1) != 3:
                self.y -= 8
        elif pyxel.btnp(pyxel.KEY_DOWN, hold=1, repeat=1):
            if pyxel.pget(self.x+7,self.y+16) != 3 and pyxel.pget(self.x+8,self.y+16) != 3:
                self.y += 8

    def draw(self):
        #進行方向に合わせて描画する
        if pyxel.btnp(pyxel.KEY_LEFT, hold=1, repeat=1):
            self.u = 16
            self.v = 16*(pyxel.frame_count % 2)
        elif pyxel.btnp(pyxel.KEY_RIGHT, hold=1, repeat=1):
            self.u = 0
            self.v = 16*(pyxel.frame_count % 2)
        elif pyxel.btnp(pyxel.KEY_UP, hold=1, repeat=1):
            self.u = 32
            self.v = 16*(pyxel.frame_count % 2)
        elif pyxel.btnp(pyxel.KEY_DOWN, hold=1, repeat=1):
            self.u = 48
            self.v = 16*(pyxel.frame_count % 2)
        else:
            self.v = 0

        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, 0)
