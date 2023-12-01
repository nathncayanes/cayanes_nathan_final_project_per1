# This file was created by Nathan Cayanes on 11/16/2023

import pygame as pg
from settings import *
from support import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.import_assets()
        # player setup
        self.image = pg.Surface((32,64))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center = pos)
        # player movement
        self.direction = pg.math.Vector2()
        self.pos = pg.math.Vector2(self.rect.center)
        self.speed = 200
    # this is a big decision, either i can create multiple spritesheets or just get multiple pngs with each frame
    # if i choose the first, i can model the spritesheets after Mr. Cozort's
    # if i choose the second, i can follow the tutorial more closely
    # either way i need to make all the designs in photoshop and decide whether to export individually or in one file
    def import_assets(self):
        self.animations = {"up": [], "down": [], "left": [], "right": [],
                           "right_idle":[], "left_idle":[], "up_idle":[], "down_idle":[]}

        for animation in self.animations.keys():
            full_path = "animations/code file/" + animation
            self.animations[animation] = import_folder(full_path)
    # just like in the myGame project, we are defining the controls
    def input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_s]:
            self.direction.y = 1
        # needs this else statement so that the character stops when we let go of w/s
        else:
            self.direction.y = 0
        if keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_d]:
            self.direction.x = 1
        # same as above, needs this else statement so that the character stops when we let go of a/d
        else:
            self.direction.x = 0
    def move(self, dt):
        # we need to add the line of code below so that python knows what direction the vector is going
        if self.direction.magnitude() > 0:
            # normalizing a vector, since by default the movement going diagonally is faster than it is going in one direction,
            # we need to make sure that the direction of the vector, no matter what direction, is always the same
            self.direction = self.direction.normalize()
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
    def update(self, dt):
        self.input()
        self.move(dt)