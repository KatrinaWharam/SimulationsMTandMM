# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:34:41 2023

@author: Katrina
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def ori_avrg(folder_name):
    nmb_to_zero = 0
    nmb_to_pi = 0
    files_to_zero = [f"{folder_name}\\to_zero\\{fn}" for fn in os.listdir(f"{folder_name}\\to_zero") if fn.endswith(".txt")]
    files_to_pi = [f"{folder_name}\\to_pi\\{fn}" for fn in os.listdir(f"{folder_name}\\to_pi") if fn.endswith(".txt")]
    for fn in files_to_zero:
        nmb_to_zero += 1
    for fn in files_to_pi:
        nmb_to_pi += 1
    
    average_ori = nmb_to_pi*180/(nmb_to_zero + nmb_to_pi)
    return average_ori

#takes a list ["setupa", "setupb", ...]
def plot_critical_angle(file_list):
    angles = np.zeros(len(file_list))
    for i in np.arange(len(file_list)):
        angles[i] = (i+1) * np.pi/10 /(2* np.pi) * 360
        
    avrg_ori = np.zeros(len(file_list))
    for i,folder_name in enumerate(file_list):
        avrg_ori[i] = ori_avrg(folder_name)
        
    fig, ax = plt.subplots()
    ax.set_xlabel("initial orientation")
    ax.set_ylabel("average of final angle betweent the microtubules")
    ax.scatter(angles, avrg_ori, color = 'black',marker = 'x')
    ax.grid()
        

if __name__ == "__main__":
    file_list = ["setup10","setup11","setup12","setup13","setup", "setup14","setup15","setup16","setup17"]
    plot_critical_angle(file_list)