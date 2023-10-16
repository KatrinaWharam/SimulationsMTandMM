# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 01:27:50 2023

@author: Katrina
"""

from getData import save_fiber_toXYZ
import os

def dir_to_xyz(setup_number):
    dir_list = os.listdir(f"setup{setup_number}/fiberPos")
    for file_name in dir_list:
        path = f"setup{setup_number}/fiberPos/{file_name}"
        save_fiber_toXYZ(path, 250, 1, setup_number)
        
dir_to_xyz(9)