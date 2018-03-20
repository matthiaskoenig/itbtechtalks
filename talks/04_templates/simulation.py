"""
Test scipy ode file.
"""

import os
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

out_dir = './results'

def example_scipy(model_id):

    # ----------------------
    # import odes
    # ----------------------
    py_file = os.path.join('.', 'results', "{}.py".format(model_id))
    from importlib.machinery import SourceFileLoader
    ode = SourceFileLoader("module.name", py_file).load_module()

    # ----------------------
    # Lorenz simulation
    # ----------------------
    # Simulation time
    T = np.arange(0, 20, 0.01)

    x0 = np.empty_like(ode.x0)
    x0[:] = ode.x0
    p = np.empty_like(ode.p)
    p[:] = ode.p

    # Integration
    X = odeint(ode.f_dxdt, x0, T, args=(p, ))
    # Solution DataFrame
    s = ode.f_z(X, T, p)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
    axes = (ax1, ax2, ax3, ax4)
    ax1.plot(s.time, s.x, label="x")
    ax1.plot(s.time, s.y, label="y")
    ax1.plot(s.time, s.z, label="z")

    ax2.plot(s.x, s.y, label="y ~ x")
    ax3.plot(s.x, s.z, label="z ~ x")
    ax4.plot(s.y, s.z, label="z ~ y")

    ax1.set_title("Lorenz Time Course")
    ax1.set_xlabel("time")
    for ax in (ax2, ax3, ax4):
        ax.set_title("Lorenz State Space")
        ax.set_xlabel("value")

    for ax in axes:
        ax.legend()
        ax.set_ylabel("value")

    fig.savefig(os.path.join('.', 'results', "lorenz_scipy.png"),
                dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    model_id = "lorenz"
    example_scipy(model_id)





