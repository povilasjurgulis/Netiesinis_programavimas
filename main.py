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


# ---------------------------------
# 2. Funkcijų reikšmių apskaičiavimas

# Taške X0 funkcijos reikšmės
X0 = [0, 0, 0]
print (f"f(X0) = {f(X0)}, g(X0) = {g(X0)}, h(X0) = {h(X0)}")

# Taške X1 funkcijos reikšmės
X1 = [1, 1, 1]
print (f"f(X1) = {f(X1)}, g(X1) = {g(X1)}, h(X1) = {h(X1)}")

# Taške Xm funkcijos reikšmės
Xm = [9/10, 3/10, 4/10]
print (f"f(Xm) = {f(Xm)}, g(Xm) = {g(Xm)}, h(Xm) = {h(Xm)}")


# ------------------
# 3. Baudos funkcija

def b(X):
    return max(0, g(X))**2 + h(X)[0]**2 + h(X)[1]**2 + h(X)[2]**2

def B(X, r):
    if g(X) == 0 and h(x) <= 0:
        return f(X)
    else:
        return f(X) + 1/r * b(X)

print (f"Baudos test: {B(X1, 0.2)}")   