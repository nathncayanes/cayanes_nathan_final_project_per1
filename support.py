# This file was created by Nathan Cayanes on 11/17/2023

# all walk does is return the list with all the contents in the folder, which in this case would be the animations folder
from os import walk
# import pygame as pg

def import_folder(path):
    surface_list = []
    for folder_name, img_files in walk(path):
        print(img_files)
    #     for image in img_files:
    #         full_path = path + "/" + image
    #         image_surf = pg.image.load(full_path).convert_alpha()
    #         image_surf.append(image_surf)
    return surface_list