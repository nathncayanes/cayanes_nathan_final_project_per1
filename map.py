# This file was created by Nathan Cayanes on 12/13/23

import pygame as pg, sys
# this module allows me to import the tiled files much easier and I only need the load_pygame portion as this this gives me
# the map attributes in the file which then allows me to select the directories that I need to display
from pytmx.util_pygame import load_pygame

pg.init()
screen = pg.display.set_mode((1280,720))
# works similarly to how I grabbed the image files for my animation cycle
tmx_data = load_pygame("map/map.tmx")
# getting all layers in the tiled file
print(tmx_data.layers)
# get all visible layers
for layer in tmx_data.visible_layers:
    print(layer)
# gets all layernames so I can isolate the ones I need
print(tmx_data.layernames)
# gets the floor layer that has the map
print(tmx_data.get_layer_by_name("floor"))

layer = tmx_data.get_layer_by_name("floor")
for x, y, surf in layer.tiles():
    print(x * 128)
    print(y * 128)
    print(surf)

# creates a window to hopefully display results
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill("BLACK")
    pg.display.update()