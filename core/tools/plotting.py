import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, pi

def set_up_circular_plot(rticks = [1], clockwise = True):
    '''
    Sets up a grid for a circular plot, such as in spectranspo.TimeDist.plot_circular()

    Parameters
    ----------
    r_max (numeric):
        The maximum radius to plot
    clockwise (bool):
        If True, the plot will be orientated clockwise starting at the top. Otherwise, it will be orientated counter-clockwise starting at the right.
    '''
    #Plot ticks indicating radius
    rticks = np.array(rticks)
    r_max = rticks.max()
    for tick in rticks:
        theta = np.linspace(0, 2*pi, 1000)
        z = tick*np.exp(1j*theta)
        z = np.append(z, z[0])
        plt.plot(np.real(z), np.imag(z), color = '#7f7f7f', linewidth = 0.5)
        plt.text(0, tick, '{:,}'.format(tick), ha = 'center', va = 'center')
        plt.text(0, -tick, '{:,}'.format(tick), ha = 'center', va = 'center')
        plt.text(tick, 0, '{:,}'.format(tick), ha = 'center', va = 'center', rotation = 90)
        plt.text(-tick, 0, '{:,}'.format(tick), ha = 'center', va = 'center', rotation = -90)
    
    #Plot ticks indicating time
    thetaticks = np.linspace(0, 2*np.pi, 24, False)
    for tick in thetaticks:
            h = tick*12/pi
            if clockwise:
                plt.plot([0, r_max*np.sin(tick)], [0, r_max*np.cos(tick)], linewidth = 0.5, color = '#7f7f7f')
                plt.text(1.1*r_max*np.sin(tick), 1.1*r_max*np.cos(tick), str(int(round(h))) + ':00', ha = 'center', va = 'center')
            else:
                plt.plot([0, r_max*np.cos(tick)], [0, r_max*np.sin(tick)], linewidth = 0.5, color = '#7f7f7f') 
                plt.text(1.1*r_max*np.cos(tick), 1.1*r_max*np.sin(tick), str(int(round(h))) + ':00', ha = 'center', va = 'center')

    plt.axis('equal')
    plt.axis('off')

def plot_dists(dists, resolution = 288, clockwise = True, pdf = False, filepath = None):
    '''
    Creates a circular plot of multiple TimeDists. Optionally saves them to a specified filepath.

    Parameters
    ----------
    dists (list):
        A list of TimeDist objects to plot
    resolution (int):
        Resolution of plot
    colckwise (bool):
        If True, the plot will be orientated clockwise starting at the top. Otherwise, it will be orientated counter-clockwise starting at the right.
    filepath (str, optional):
        If specified, the plot will be saved at this location
    '''
    fig = plt.Figure(facecolor = '#ffffff')

    #Calculate `r_max` parameter
    if pdf:
        r_max = 1
    else:
        r_max = 0
        for dist in dists:
            r_max = max(r_max, dist.total)

    #Create plot
    set_up_circular_plot(r_max, clockwise)
    for dist in dists:
        dist.plot_circular(resolution, pdf = pdf, clockwise = clockwise)

    #Save or show plot
    if filepath:
        plt.savefig(filepath)
        print(filepath + ' successfully saved')
    else:
        plt.show()