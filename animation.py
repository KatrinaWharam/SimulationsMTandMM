import os
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import getData
import Theta_against_t

plt.rcParams['animation.ffmpeg_path'] = r"C:\Users\Katrina\anaconda3\pkgs\ffmpeg-4.3.1-ha925a31_0\Library\bin\ffmpeg"


def loadData(file_path,nb_snapshots,skipSnap):
    t = Theta_against_t.get_t_series(file_path, nb_snapshots,skipSnap)
    Theta = Theta_against_t.get_theta_series(file_path, nb_snapshots, skipSnap)
    data = getData.loadData(file_path, nb_snapshots,skipSnap)

    return t, data, Theta


def formatVectors(data):
    xy_orient = data[:, :, 6:8]
    lengths = data[1, :, 2]
    xy_pos = data[:, :, 3:5]
    # vector encodes the orientation of both vectors with the correct lengths
    vector = np.transpose(np.transpose(xy_orient,(0,2,1)) * lengths, (0,2,1))
    # xy_pos_orig describes the position of the end of the vector
    xy_pos_orig = xy_pos - vector/2
    return xy_pos, xy_pos_orig, vector


def createAnimation(file_path,nb_snapshots,skipSnap):
    t, data, Theta = loadData(file_path, nb_snapshots,skipSnap)
    Theta = Theta * 180 / np.pi
    xy_pos, xy_pos_orig, vector = formatVectors(data)

    fig, (ax, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 2]},figsize = (12.5,4))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.minorticks_on()
    ax.grid(which='both', alpha=0.3)
    ax.set_axisbelow(True)
    ax.quiver(xy_pos_orig[0, :, 0], xy_pos_orig[0, :, 1], vector[0, :, 0], 
              vector[0, :, 1], angles='xy', scale_units='xy', scale=1)
    ax.scatter(xy_pos[0, :, 0], xy_pos[0, :, 1])
    ax.set_title('t = {}s'.format(round(t[0])))
    
    ax2.set_xlim(t[0]-1, t[-1]+1)
    ax2.set_ylim(-95, 275)
    ax2.set_xlabel("t (s)")
    ax2.set_ylabel(r"$\Theta$ (°)")
    ax2.plot(t[0], Theta[0])
    
    def update(frame):
        ax.clear()
        ax2.clear()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax2.set_xlim(t[0]-1, t[-1]+1)
        ax2.set_ylim(-95, 275)
        ax2.set_xlabel("t (s)")
        ax2.set_ylabel(r"$\Theta$ (°)")
        ax2.grid()
        plt.minorticks_on()
        ax.grid(which='both', alpha=0.3)
        ax.set_axisbelow(True)
        ax.quiver(xy_pos_orig[frame, :, 0], xy_pos_orig[frame, :, 1], vector[frame, :, 0], 
                  vector[frame, :, 1], angles='xy', scale_units='xy', scale=1)
        ax.scatter(xy_pos[frame, :, 0], xy_pos[frame, :, 1])
        ax.set_title('t = {}s'.format(round(t[frame])))
        
        ax2.plot(t[0:frame], Theta[0:frame])
        return ax, ax2
    
    ani = animation.FuncAnimation(fig=fig, func=update, frames=250, interval=50, repeat_delay = 1000)
    name = os.path.split(file_path)[-1][:-3]
    folder = os.path.split(file_path)[0].split("\\")[0]
    if not os.path.isdir(f'{folder}/animations'):
        os.mkdir(f'{folder}/animations')
    # Wenn du fps erhöst wird das Video schneller
    writervideo = animation.FFMpegWriter(fps=10)
    ani.save(f'{folder}/animations/{name}.mp4', writer=writervideo)
    plt.close()



if __name__ == "__main__":
    file_list = [f"setup10\\to_pi\\{fn}" for fn in os.listdir("setup10\\to_pi") if fn.endswith(".txt")]
    for file in file_list:
        ani = createAnimation(file, 250, 1)