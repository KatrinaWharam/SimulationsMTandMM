# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:34:12 2023

@author: Katrina
"""

import filter_for_alignment
import Theta_against_t
import init_to_final_angle
import getData
import numpy as np
import matplotlib.pyplot as plt
import os

def get_xypos(file_path, snap_nb):
    if not os.path.isfile(file_path):
        raise ValueError("File does not exist")
    data = getData.loadData(file_path, 250, 1)
    xy_pos = data[:, :, 3:5][snap_nb]
    xy_MT1 = xy_pos[0]
    xy_MT2 = xy_pos[1]
    xy_pos_rel = xy_pos[1]-xy_pos[0]
    return xy_pos_rel

def plot_orientations(folder_name):
    to_zero = [f"{folder_name}\\to_zero\\{fn}" for fn in os.listdir(f"{folder_name}\\to_zero") if fn.endswith(".txt")]
    to_pi = [f"{folder_name}\\to_pi\\{fn}" for fn in os.listdir(f"{folder_name}\\to_pi") if fn.endswith(".txt")]
    posx_zero = np.zeros(len(to_zero))
    posy_zero = np.zeros(len(to_zero))
    posx_pi = np.zeros(len(to_pi))
    posy_pi = np.zeros(len(to_pi))
    for i, file in enumerate(to_zero):
        posx_zero[i] = get_xypos(file, 0)[0]
        posy_zero[i] = get_xypos(file, 0)[1]
    for i, file in enumerate(to_pi):
        posx_pi[i] = get_xypos(file, 0)[0]
        posy_pi[i] = get_xypos(file, 0)[1]
        
    fig, ax = plt.subplots()
    ax.set_xlabel("initial x-value")
    ax.set_ylabel("initial y-value")
    ax.scatter(posx_zero, posy_zero, marker='x', color = '#7091B8', label = 'parallel alignment')
    ax.scatter(posx_pi, posy_pi, marker='x', color = '#994040', label = 'antiparallel alignment')
    plt.arrow(-2, 0, 4, 0, length_includes_head = True, head_width = 0.1, color = 'black')
    ax.legend()
    
    return fig

if __name__ == "__main__":
    fig = plot_orientations("setup13")

    
    
    