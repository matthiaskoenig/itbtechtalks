"""
Simple ODE model demonstrating virtual environments.
"""

import pandas as pd
import tellurium as te
from matplotlib import pyplot as plt


# Integrate ODE system
r = te.loada("""
    J0: X1 -> X2; k1*X1;
    X1 = 10.0; X2 = 0.0; k1 = 0.1;
""")
s = r.simulate(start=0, end=10, steps=200)
s = pd.DataFrame(s, columns=s.colnames)


fig, ax = plt.subplots(nrow=1, ncol=1)
ax.plot(s.time, s.X1)
ax.plot(s.time, s.X2)
plt.show()
