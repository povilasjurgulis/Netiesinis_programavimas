# 3 Netiesinis programavimas

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


# -----------------------------
# 3. Kvadratinė Baudos funkcija

# Lygybinis apribojimas g(X) baudžiamas kvadratu.
# Nelygybinius apribojimus baudžiame tik tada, kai h_i(X) > 0.
# Bauda:
def b(X):
    return sum(max(0, hi)**2 for hi in h(X)) + g(X)**2

# Baudos funkcija:
def B(X, r):
    return f(X) + 1/r * b(X)

print (f"Baudos testas: {B(X1, 0.2)}")   


# 4. Baudos daugiklio r įtaką baudos funkcijos reikšmėms

r = np.array([0.1, 0.2, 0.5, 0.8, 1, 3, 5, 10])

print(f"f(Xm) = {f(Xm)}")
print(f"b(Xm) = {b(Xm)}")

for r_value in r:
    print(f"Baudos funkcijos reiksme su r = {r_value} taske Xm yra {B(Xm, r_value)}")