# This file was created by Nathan Cayanes on 11/16/2023

import pygame as pg
from settings import *
from player import Player
from map import Map

class Level:
    def __init__(self):
        # gets the display surface from main.py and allows me to "draw" directly on the display
        self.display_surface = pg.display.get_surface()
        # sprite groups
        self.all_sprites = CameraGroup()
        self.setup()
    def setup(self):
        Map(
            pos = (0,0),
            surf = pg.image.load("map/map.png").convert_alpha(),
            groups = self.all_sprites)
        self.player = Player((640,360), self.all_sprites)
    def run(self, dt):
        self.display_surface.fill(BLACK)
        # allows us to draw directly onto the display surface which is why we pass self.display_surface from above
        # self.all_sprites.draw(self.display_surface)
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)