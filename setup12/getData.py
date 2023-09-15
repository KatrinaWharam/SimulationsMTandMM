import numpy as np
from matplotlib import pyplot as plt
import linecache
import os


def loadSnapShot(file_path, snap_num):
    snap_start = 6+snap_num*(2+6)
    snap_stop = snap_start+2
    snap_data = np.zeros((2,12))
    for idx,lineno in enumerate(range(snap_start,snap_stop)):
        print(lineno)
        snap_data[idx] = np.asarray(linecache.getline(file_path,lineno).split(),dtype=float)
    return snap_data

def loadData(file_path,nb_snapshots,skipSnap):
    data = np.zeros((len(range(0, nb_snapshots, skipSnap)),2,12))

    for idx,snap_num in enumerate(range(0, nb_snapshots, skipSnap)):
        print(idx)
        data[idx] = loadSnapShot(file_path,snap_num)
    return data

def save_fiber_toXYZ(file_path,nb_snapshots,skipSnap):
    if not os.path.isdir('xyz_files'):
        os.mkdir('xyz_files')
    data = loadData(file_path, nb_snapshots,skipSnap)
    pos = data[:, :, 3:6]
    ori = data[:, :, 6:9]
    xyzName = os.path.split(file_path)[-1][:-3]+'xyz'
    myfileXY = open('xyz_files/'+xyzName, "w")
    for positions, orientations in zip(pos, ori):
        print(positions.shape[0])
        myfileXY.write(str(positions.shape[0]) + '\n')
        myfileXY.write('\n')
        mx = positions[:, 0]
        my = positions[:, 1]
        theta = np.arctan2(orientations[:, 1], orientations[:, 0])
        for x, y, nx, ny, color in zip(mx, my, orientations[:, 0], orientations[:, 1], theta):
             myfileXY.write("{}\t {}\t".format(x, y) + "{}\t {}\t {}\t ".format(nx, ny, color) + '\n')
    myfileXY.close()


