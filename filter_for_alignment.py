# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 13:19:10 2023

@author: Katrina
"""

import numpy as np
import Theta_against_t
import os
import shutil

# die winkel in data müssen in Bogenmaß angegeben werden
def analyse_slice(data):
    if np.sum(data * data) / len(data) < 1e-3:
        return 0
    elif np.sum((data-np.pi) * (data-np.pi)) / len(data) < 1e-3:
        return 1
    else:
        return 2
    

def determine_cetegory(file_path, length_slice_window, stepsize):
    theta = Theta_against_t.get_theta_series(file_path, 250, 1)
    for i in range(0, 250 - length_slice_window, stepsize):
        data = theta[i: i+stepsize]
        a = analyse_slice(data)
        if a in [0,1]:
            return a
            break
    return 2

# folder_name ist z.b. "setup3"
def sort_folder(folder_name):
    file_list = [f"{folder_name}\\fiberPos\\{fn}" for fn in os.listdir(f"{folder_name}\\fiberPos") if fn.endswith(".txt")]
    if not os.path.isdir(f'{folder_name}/to_zero'):
        os.mkdir(f'{folder_name}/to_zero')
    if not os.path.isdir(f'{folder_name}/to_pi'):
        os.mkdir(f'{folder_name}/to_pi')
    if not os.path.isdir(f'{folder_name}/no_align'):
        os.mkdir(f'{folder_name}/no_align')
        
    for file_path in file_list:
        cat = determine_cetegory(file_path, 30, 10)
        file = os.path.split(file_path)[-1]
        if cat == 0:
            dest = f"{folder_name}\\to_zero\\{file}"
            shutil.copyfile(file_path, dest)
        if cat == 1:
            dest = f"{folder_name}\\to_pi\\{file}"
            shutil.copyfile(file_path, dest)
        if cat == 2:
            dest = f"{folder_name}\\no_align\\{file}"
            shutil.copyfile(file_path, dest)
        
        
if __name__ == "__main__":
    sort_folder("setup4")
    sort_folder("setup5")
    sort_folder("setup6")
    sort_folder("setup7")
    sort_folder("setup8")
    sort_folder("setup9")
            
        