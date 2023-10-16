# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 15:12:32 2023

@author: Katrina
"""

import filter_for_alignment
import Theta_against_t
import numpy as np
import matplotlib.pyplot as plt
import os


def plot_final_init(folder_name):
    to_zero = [f"{folder_name}\\to_zero\\{fn}" for fn in os.listdir(f"{folder_name}\\to_zero") if fn.endswith(".txt")]
    to_pi = [f"{folder_name}\\to_pi\\{fn}" for fn in os.listdir(f"{folder_name}\\to_pi") if fn.endswith(".txt")]
    theta_zero = np.zeros(len(to_zero))
    theta_pi = np.zeros(len(to_pi))
    for i, file in enumerate(to_zero):
        theta_zero[i] = Theta_against_t.get_theta(file,0)
    for i, file in enumerate(to_pi):
        theta_pi[i] = Theta_against_t.get_theta(file,0)
        
    fig, ax = plt.subplots()
    ax.scatter(theta_zero,np.zeros(len(to_zero)))
    ax.scatter(theta_pi,np.ones(len(to_pi)))
    
    return fig

def multiplot(folder_list):
    zero = []
    pi = []
    for folder_name in folder_list:
        to_zero = [f"{folder_name}\\to_zero\\{fn}" for fn in os.listdir(f"{folder_name}\\to_zero") if fn.endswith(".txt")]
        to_pi = [f"{folder_name}\\to_pi\\{fn}" for fn in os.listdir(f"{folder_name}\\to_pi") if fn.endswith(".txt")]
        theta_zero = np.zeros(len(to_zero))
        theta_pi = np.zeros(len(to_pi))
        for i, file in enumerate(to_zero):
            theta_zero[i] = Theta_against_t.get_theta(file,0)
        for i, file in enumerate(to_pi):
            theta_pi[i] = Theta_against_t.get_theta(file,0)
        zero.append(to_zero)
        


if __name__ == "__main__":
    fig = plot_final_init("setup13")
    