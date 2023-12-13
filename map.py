# This file was created by Nathan Cayanes on 12/13/23

import pygame as pg, sys
# this module allows me to import the tiled files much easier and I only need the load_pygame portion as this this gives me
# the map attributes in the file which then allows me to select the directories that I need to display
from pytmx.util_pygame import load_pygame

pg.init()
screen = pg.display.set_mode((1280,720))
# works similarly to how I grabbed the image files for my animation cycle
tmx_data = load_pygame("map/map.tmx")
# checking that it can access the file and seeing what it can access from it
print(dir(tmx_data))

# creates a window to hopefully display results
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill("BLACK")