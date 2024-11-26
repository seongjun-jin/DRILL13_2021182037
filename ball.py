from Lecture18_Scrolling.game_world import remove_collision_object
from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(50, server.background.w)
        self.y = y if y else random.randint(50, server.background.h)



    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        #draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - server.background.window_left - 10, self.y - server.background.window_bottom - 10, self.x - server.background.window_left + 10, self.y - server.background.window_bottom + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)
        pass
