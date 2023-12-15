# This file was created by Nathan Cayanes on 11/16/2023

import pygame as pg
from settings import *
from support import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.import_assets()
        # imports the folder and the frame_index will cylce through the different images in each folder
        self.status = "down"
        self.frame_index = 0
        # player setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        # player movement
        self.direction = pg.math.Vector2()
        self.pos = pg.math.Vector2(self.rect.center)
        self.speed = 200
# this is a directory/list of a list that basically uses the full_path variable below to access all of the folders that
# contain all the image files for the game and compiles them with a list
    def import_assets(self):
        self.animations = {"up": [], "down": [], "left": [], "right": [],
                           "right_idle":[], "left_idle":[], "up_idle":[], "down_idle":[]}

        for animation in self.animations.keys():
            # tells the computer where to look and opens up the folders listed above
            full_path = "animations/images/" + animation
            # imports them into pygame and I printed it to make sure that it works properly
            self.animations[animation] = import_folder(full_path)
        print(self.animations)
    # this is the function used to animate the character
    def animate(self, dt):
        # sets the speed of how fast the animation will cycle
        self.frame_index += 3 * dt
        # this continues the animation loop and prevent an error
        # len is used to find the amount of files in the folder of the direction specified in self.status in self.animations
        # without this line, the computer will continue adding to the frame_index number and will error as there are only 4
        # images in each folder but this prevents it from going beyond the amount of images in the folder
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        # this just cycles through the images in the folder based on the status and the number specified from the frame_index
        self.image = self.animations[self.status][int(self.frame_index)]
    # just like in the myGame project, we are defining the controls
    def input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pg.K_s]:
            self.direction.y = 1
            self.status = "down"
        # needs this else statement so that the character stops when we let go of w/s
        else:
            self.direction.y = 0
        if keys[pg.K_a]:
            self.direction.x = -1
            self.status = "left"
        elif keys[pg.K_d]:
            self.direction.x = 1
            self.status = "right"
        # same as above, needs this else statement so that the character stops when we let go of a/d
        else:
            self.direction.x = 0
    def get_status(self):
        # figures out when the player is stopped
        if self.direction.magnitude() == 0:
            # self.status.split splits up the string in the folder name preventing errors such as down_idle_idle
            self.status = self.status.split("_")[0] + "_idle"
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
        self.get_status()
        self.move(dt)
        self.animate(dt)