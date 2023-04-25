import pyxel
import random
from player import Player 
from enemy import Enemy

enemies = [] 

class App:
    def __init__(self): # 初期化
        pyxel.init(256, 256, fps=5)
        pyxel.load("image.pyxres")
        self.player = Player(16, 16, 0, 0, 16, 16)
        enemies.append(Enemy(224, 16, 0, 32, 16, 16, 'left', 224, 16))
        enemies.append(Enemy(16, 224, 0, 64, 16, 16, 'right', 16, 224))
        enemies.append(Enemy(224, 224, 0, 96, 16, 16, 'up', 224, 224))

        self.point_tile = [2] * 196
        self.scene = 'title' 

    def run(self):
        pyxel.playm(0,loop=True)
        pyxel.run(self.update, self.draw) 

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if self.scene == 'title':
            self.update_title_scene()
        elif self.scene == 'play':
            pyxel.stop()
            self.update_play_scene()
        elif self.scene == 'gameover' or self.scene == 'gameclear':
            self.update_over_clear_scene()

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = 'play'

    def update_play_scene(self): 
        self.player.update()
        if self.player.x % 16 == 0 and self.player.y % 16 == 0:
                x = (self.player.x - 16) // 16
                y = (self.player.y - 16) // 16
                num = x + y*14
                self.point_tile[num] = 0
        for enemy in enemies:
            enemy.update()
            if self.colligion(self.player, enemy):
                self.scene = 'gameover'
        if all([c != 2 for c in self.point_tile]):
            self.scene = 'gameclear'

    def update_over_clear_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.player.x = 16
            self.player.y = 16
            for enemy in enemies:
                enemy.x = enemy.sx
                enemy.y = enemy.sy
            self.point_tile = [2] * 196
            self.scene = 'title'
        
    def colligion(self, p, e):
        if (p.x == e.x and -16 < p.y - e.y < 16) or (p.y == e.y and -16 < p.x - e.x < 16):
            return True
        else:
            return False

    def draw(self):
        pyxel.cls(0)
        if self.scene == 'title':
            self.draw_title_scene()
        elif self.scene == 'play':
            self.draw_play_scene()
        elif self.scene == 'gameover':
            self.draw_gameover_scene()
        elif self.scene == 'gameclear':
            self.draw_gameclear_scene()

    def draw_title_scene(self):
        pyxel.text(112, 96, "Pack Man", pyxel.frame_count % 16)
        pyxel.text(99, 160, "- PRESS ENTER -", 13)

    def draw_play_scene(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,256,256,0)
        for i,c in enumerate(self.point_tile):
            x = (i % 14) * 16 + 16
            y = (i // 14) * 16 + 16
            if pyxel.pget(x,y) != 3:
                pyxel.rect(x+6,y+6,4,4,c)
            else:
                self.point_tile[i] = 3
        self.player.draw()
        for enemy in enemies:
            enemy.draw()

    def draw_gameover_scene(self):
        pyxel.rect(0, 124, 256, 16, 8)
        pyxel.text(110, 129, "GAME OVER", 7)
        pyxel.text(99, 160, "- PRESS ENTER -", 13)

    def draw_gameclear_scene(self):
        pyxel.rect(0, 124, 256, 16, 8)
        pyxel.text(110, 129, "GAME CLEAR", 7)
        pyxel.text(99, 160, "- PRESS ENTER -", 13)

App().run()