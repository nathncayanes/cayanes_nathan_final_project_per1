# This file was created by Nathan Cayanes on 11/16/2023

'''
Sources:
Game Base: https://www.youtube.com/watch?v=R9apl6B_ZgI&ab_channel=freeCodeCamp.org
Animation: https://www.youtube.com/watch?v=nXOVcOBqFwM&ab_channel=CodingWithRuss
Animation pt 2: modeled after Mr. Cozort's animated_spritesheet.py in Examples
Tiled + How to Use: https://www.youtube.com/watch?v=N6xqCwblyiw&ab_channel=ClearCode

Title:
Pydew Valley

Goals:
adjust bell sprite to a farmer (so before this i need to learn how to use photoshop to "animate")
animate bell sprite
open world
learn and use tiled to create the map
transaction area
farming
make multuple npc that can give you things (maybe specialize in a certain portion of the map)
create new sprite in photoshop and animate an idle animation for it
tools (pickaxes, axes, swords)
'''

# import programs here, sys is important to properly close the app
import pygame as pg, sys
from settings import *
from level import Level

# create Game class + game loop
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption("Something Valley")
        self.clock = pg.time.Clock()
        self.level = Level()

    def run(self):
        # game loop
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    # sys is basically only used here
                    sys.exit()
            # dt = delta time, this makes sure that updates are uneffected by the framerate
            # if we decided not to use delta time, then the movement would be affected depending on what framerate is set
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pg.display.update()

# creates an object from Game class and calls game loop
if __name__ == "__main__":
    game = Game()
    game.run()
