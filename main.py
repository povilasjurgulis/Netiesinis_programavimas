# 3 Netiesinis programavimas

import sympy as sp
import numpy as np

# ---------------------------------
# 1. Tikslo ir Apribojimų funkcijos

# Tikslo funkcija
def f(X):
    # Tikslo funkcija: f(X) = -xyz (minimizuoti)
    x, y, z = X
    return -x*y*z

# Lygybinis apribojimas
def g(X):
    # Lygybinis apribojimas: g(X) = 2xy + 2xz + 2yz - 1 = 0
    x, y, z = X
    return 2*x*y + 2*x*z + 2*y*z - 1

# Nelygybiniai apribojimai
def h(X):
    # Nelygybiniai apribojimai: h(X) <= 0, t.y. x >= 0, y >= 0, z >= 0
    x, y, z = X
    h1 = -x  # -x <= 0, t.y. x >= 0
    h2 = -y  # -y <= 0, t.y. y >= 0
    h3 = -z  # -z <= 0, t.y. z >= 0
    return np.array([h1, h2, h3])