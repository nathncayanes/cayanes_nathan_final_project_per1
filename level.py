# This file was created by Nathan Cayanes on 11/16/2023

import pygame as pg
from settings import *
from player import Player

class Level:
    def __init__(self):
        # gets the display surface from main.py and allows me to "draw" directly on the display
        self.display_surface = pg.display.get_surface()
        # sprite groups
        self.all_sprites = pg.sprite.Group()
        self.setup()
    def setup(self):
        self.player = Player((640,360), self.all_sprites)
    def run(self, dt):
        self.display_surface.fill(BLACK)
        # allows us to draw directly onto the display surface which is why we pass self.display_surface from above
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)