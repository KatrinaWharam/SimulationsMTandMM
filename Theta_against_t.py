import os
import numpy as np
from matplotlib import pyplot as plt
import linecache

# ich musste den file_path immer in der form
# "setup\\fiberPos\\fibers_pos__0.0_1.0_0.05_n2__0_1_0.txt"
# angeben, sonst hat er den nicht gefunden
def get_t(file_path, snap_nb):
    if not os.path.isfile(file_path):
        raise ValueError("File does not exist")
    t = float(linecache.getline(file_path, 2 + snap_nb*8).split()[2])
    return t


def get_theta(file_path, snap_nb):
    if not os.path.isfile(file_path):
        raise ValueError("File does not exist")
    orient_xy = np.zeros((2,2))
    orient_xy[0,:] = np.asarray(linecache.getline(file_path, 6 + snap_nb*8).split()[6:8],dtype=float)
    orient_xy[1,:] = np.asarray(linecache.getline(file_path, 7 + snap_nb*8).split()[6:8],dtype=float)
    angles = np.arctan2(orient_xy[:,1],orient_xy[:,0])
    theta = (angles[0] - angles[1] + np.pi/2) % (2 * np.pi) - np.pi/2
    return theta



def get_t_series(file_path, nb_snapshots,skipSnap):
    nb_datapoints = (len(range(0, nb_snapshots, skipSnap)))
    t = np.zeros(nb_datapoints)
    for idx, snap_nb in enumerate(range(0, nb_snapshots, skipSnap)):
        t[idx] = get_t(file_path, snap_nb)
    return t


def get_theta_series(file_path, nb_snapshots,skipSnap):
    nb_datapoints = (len(range(0, nb_snapshots, skipSnap)))
    theta = np.zeros(nb_datapoints)
    for idx, snap_nb in enumerate(range(0, nb_snapshots, skipSnap)):
        theta[idx] = get_theta(file_path, snap_nb)

    return theta


def getMultiDataSeries(file_path_list, nb_snapshots,skipSnap):
    nb_datapoints = (len(range(0, nb_snapshots, skipSnap)))
    t = np.zeros(nb_datapoints)
    theta = np.zeros((len(file_path_list), nb_datapoints))

    for idx, file_path in enumerate(file_path_list):
        t = get_t_series(file_path, nb_snapshots,skipSnap)
        theta[idx] = get_theta_series(file_path, nb_snapshots,skipSnap)

    return t, theta


def plotData(file_path, nb_snapshots,skipSnap):
    t = get_t_series(file_path, nb_snapshots,skipSnap)
    theta = get_theta_series(file_path, nb_snapshots,skipSnap)
    plt.plot(t, theta * 180 / np.pi)
    plt.show()


def plotMultiData(file_path_list, nb_snapshots,skipSnap):
    t, theta = getMultiDataSeries(file_path_list, nb_snapshots,skipSnap)
    for idx, file_path in enumerate(file_path_list):
        plt.plot(t, theta[idx] * 180 / np.pi)
    plt.show()


if __name__ == "__main__":
    filename = 'setup3\\fiberPos\\fibers_pos__-0.08599999999999997_0.08600000000000008_0.05_n2__-0.07071_0.07071_0.txt'
    #plotData(filename, 250, 1)

    file_list = [f"setup\\to_pi\\{fn}" for fn in os.listdir("setup\\to_pi") if fn.endswith(".txt")]
    plotMultiData(file_list, 250, 1)
    """
    numb = 6
    for idx, file in enumerate(file_list[numb:numb+1]):
        plt.figure(idx)
        plt.ylim(-95, 275)
        plotData(file, 250, 1)
    """
