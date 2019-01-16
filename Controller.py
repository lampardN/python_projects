from graph import *
from random import randint
from Circle import Circle
from enemy import Enemy
from platform import Platform


class ControllerClass:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.x = 0
        self.y = 0
        self.radius = 10
        self.dots = []
        self.enemies = []
        self.platform = Platform(100, 20, self.window_width, self.window_height)
        self.score = 0
        self.score_label = 'Score >> '
        self.make_label()
        self.make_circles()
        self.set_enemies()

    def set_enemies(self):
        for i in range(self.window_height//100):
            for j in range(self.window_width//10):
                strength = randint(0, 6)
                if strength != 0:
                    self.enemies.append(Enemy(self.x, self.y, self.window_width, self.window_height, strength))
                self.x += self.window_width//10
            self.x = 0
            self.y += 20
        return self

    def make_circles(self):
        penSize(0)
        self.dots.append(Circle(self.platform.x + self.platform.width//2, self.platform.y - self.radius*2, 1, 1, self.radius))

    def make_label(self):
        label(self.score_label + str(self.score), 0, self.window_height + 20)

    def circle_move(self):
        for dot in self.dots:
            self.circle_block_contact()
            dot.circle_in_window(self.window_width, self.window_height)
            dot.check_platform_contact(self.platform.x, self.platform.y, self.platform.width)
            dot.move()

    def circle_block_contact(self):
        for dot in self.dots:
            for block in self.enemies:
                dot.block_contact(block.x, block.y, block.width, block.height)
