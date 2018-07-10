"""
Autogenerated ODE definition.

    model: {{ mid }}
"""
import numpy as np
import pandas as pd


# -------------------
# ids
# -------------------
xids = [{% for id in xids %}"{{ id }}", {% endfor %}]
pids = [{% for id in pids %}"{{ id }}", {% endfor %}]
yids = [{% for id in yids %}"{{ id }}", {% endfor %}]

# -------------------
# initial conditions
# -------------------
x0 = np.array([
{% for id in xids %}
    {{ x0[id] }},     # [{{ loop.index0 }}] {{ id }}
{% endfor %}
])

# -------------------
# parameters
# -------------------
p = np.array([
{% for id in pids %}
    {{ p[id] }},     # [{{ loop.index0 }}] {{ id }}
{% endfor %}
])


def f_dxdt(x, t, p):
    """ ODE system """
    _x = x
    {% for id in xids %}
    {{id}} = _x[{{loop.index0}}]  # [{{ loop.index0 }}] {{ id }}
    {% endfor %}

    {% for id in pids %}
    {{ id }} = {{ p[id] }}      # [{{ loop.index0 }}] {{ id }}
    {% endfor %}

    {% for id in yids %}
    {{ id }} = {{ y[id] }}      # [{{ loop.index0 }}] {{ id }}
    {% endfor %}

    # ode
    return [
        {% for id in xids %}
        {{ dxdt[id] }},       # [{{ loop.index0 }}] {{ id }}
        {% endfor %}
    ]


def f_y(x, t, p):
    """ Calculate y.
    :param x:
    :param t:
    :param p:
    :return:
    """

    {% for id in yids %}
    {{ id }} = {{y[id]}}  # [{{ loop.index0 }}] {{ id }}
    {% endfor %}

    # --------------------------------------

    y = np.empty(shape=({{yids | length}}))
    {% for id in yids %}
    y[{{loop.index0}}] = {{ id }}  # [{{ loop.index0 }}] {{ id }}
    {% endfor %}

    return y


def f_z(X, T, p):
    """ DataFrame of full timecourse of solution. """
    (Nt, Nx) = X.shape
    Ny = len(yids)
    Nz = 1 + Nx + Ny
    columns = ["time"] + xids + yids
    Z = np.empty(shape=(Nt, Nz))
    Z[:,0] = T
    Z[:,1:(Nx+1)] = X
    for kt in range(Nt):
        y = f_y(x=X[kt, :], t=T[kt], p=p)
        Z[kt, (Nx+1):] = y

    Z = pd.DataFrame(Z, columns = columns)
    return Z