# This file was created by Nathan Cayanes on 11/17/2023

# all walk does is return the list with all the contents in the folder, which in this case would be the animations folder
from os import walk
import pygame as pg

def import_folder(path):
    surface_list = []
    for folder_name, sub_folder, img_files in walk(path):
        for image in img_files:
            # prints the full path of each image
            full_path = path + "/" + image
            # this is going to allow us to load the images into a list and later call them in a loop
            image_surf = pg.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list