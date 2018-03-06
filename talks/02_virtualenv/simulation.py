"""
Simple ODE model demonstrating virtual environments.
"""

import numpy as np
import pandas as pd
from scipy.integrate import odeint
from matplotlib import pyplot as plt

# global settings for plots
plt.rcParams.update({
        'axes.labelsize': 'large',
        'axes.labelweight': 'bold',
        'axes.titlesize': 'large',
        'axes.titleweight': 'bold',
        'legend.fontsize': 'large',
        'xtick.labelsize': 'large',
        'ytick.labelsize': 'large',
        'figure.facecolor': '1.00'
    })


def lorenz_dxdt(x, t):
    """ Differential equations for Lorenz.

    :param x: state vector
    :param t: time
    :return: ode system
    """
    r = 45.92
    b = 4.0
    sig = 16.0
    return [
        sig*(x[1] - x[0]),
        -x[0]*x[2] + r*x[0] - x[1],
        x[0]*x[1] - b*x[2],
    ]


def lorenz_plot(s):
    """ Plot the Lorenz attractor.

    :param s: Data Frame with results
    :return:
    """
    # plot results
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
    axes = (ax1, ax2)
    ax1.plot(s.time, s.x0, label="x0")
    ax1.plot(s.time, s.x1, label="x1")
    ax1.plot(s.time, s.x2, label="x2")

    ax2.plot(s.x0, s.x1, label="x1 ~ x0")
    ax2.plot(s.x0, s.x2, label="x2 ~ x0")
    ax2.plot(s.x1, s.x2, label="x2 ~ x1")

    ax1.set_title("Lorenz Time Course")
    ax1.set_xlabel("time")
    ax2.set_title("Lorenz State Space")
    ax2.set_xlabel("value")

    for ax in axes:
        ax.legend()
        ax.set_ylabel("value")

    plt.show()

    return fig


if __name__ == "__main__":

    # simulate
    time = np.arange(0, 20, 0.001)
    x0 = [1, 1, 1]
    xids = ['x0', 'x1', 'x2']
    X = odeint(lorenz_dxdt, x0, time)

    # create data frame
    s = pd.DataFrame(X, columns=xids)
    s['time'] = time
    print(s.head())

    # plot attractor
    lorenz_plot(s)
