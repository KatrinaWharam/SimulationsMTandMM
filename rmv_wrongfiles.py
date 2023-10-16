# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:44:53 2023

@author: Katrina
"""

import getData
import os
import shutil
import numpy as np


#Goal: Remove the files from the list, which are not corresponding to intersecting MT

def rmv_list(folder_name):
    file_list1 = [f"{folder_name}\\to_pi\\{fn}" for fn in os.listdir(f"{folder_name}\\to_pi") if fn.endswith(".txt")]
    file_list2 = [f"{folder_name}\\to_zero\\{fn}" for fn in os.listdir(f"{folder_name}\\to_zero") if fn.endswith(".txt")]
    if not os.path.isdir(f'{folder_name}/wrong'):
        os.mkdir(f'{folder_name}/wrong')
        
    for file_path in file_list1:
        file = os.path.split(file_path)[-1]
        data= getData.loadData(file_path,250,1)
        pos = data[:, :, 3:5][0]
        ori = data[:, :, 6:8][0]
        posMT1= pos[0]
        posMT2= pos[1]
        oriMT1= ori[0]
        oriMT2= ori[1]
        x1= data[0,0,3]
        x2= data[0,1,3]
        n1_x= oriMT1[0]
        n2_x= oriMT2[0]
        y1= data[0,0,4]
        y2= data[0,1,4]
        n1_y= oriMT1[1]
        n2_y= oriMT2[1]
        l1 = data[0,0,2]
        l2 = data[0,1,2]
        
        lambda_1 = (n2_y*(x1-x2)+n2_x*(y2-y1))/(n1_y*n2_x-n2_y*n1_x)
        lambda_2 = (n1_y*(x1-x2)+n1_x*(y2-y1))/(n1_y*n2_x-n2_y*n1_x)
        
        if abs(lambda_1) > l1/2 or abs(lambda_2) > l2/2:
            dest = f"{folder_name}\\wrong\\{file}"
            shutil.move(file_path, dest)
            
    for file_path in file_list2:
        file = os.path.split(file_path)[-1]
        data= getData.loadData(file_path,250,1)
        pos = data[:, :, 3:5][0]
        ori = data[:, :, 6:8][0]
        posMT1= pos[0]
        posMT2= pos[1]
        oriMT1= ori[0]
        oriMT2= ori[1]
        x1= data[0,0,3]
        x2= data[0,1,3]
        n1_x= oriMT1[0]
        n2_x= oriMT2[0]
        y1= data[0,0,4]
        y2= data[0,1,4]
        n1_y= oriMT1[1]
        n2_y= oriMT2[1]
        l1 = data[0,0,2]
        l2 = data[0,1,2]
        
        lambda_1 = (n2_y*(x1-x2)+n2_x*(y2-y1))/(n1_y*n2_x-n2_y*n1_x)
        lambda_2 = (n1_y*(x1-x2)+n1_x*(y2-y1))/(n1_y*n2_x-n2_y*n1_x)
        
        if abs(lambda_1) > l1/2 or abs(lambda_2) > l2/2:
            dest = f"{folder_name}\\wrong\\{file}"
            shutil.move(file_path, dest)
            
if __name__ == "__main__":
    rmv_list("setup13")