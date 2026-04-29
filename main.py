# 3 Netiesinis programavimas
import numpy as np
import simplekso

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


# 5. Baudos funkcijos minimizavimas naudojant Simplekso algoritmą


def baudos_funkcija_su_r(r_value):
    return lambda X: B(X, r_value)


print("\n5. Baudos funkcijos minimizavimas naudojant Simplekso algoritma")
# Kad baudos narys stiprėtų, r mažiname keliais žingsniais ir kiekvieną kartą
# ankstesnį sprendinį naudojame kaip naują pradžios tašką.
r_sequence = [1.0, 0.2, 0.05, 0.01]

# Vykdome seką pradėdami iš kiekvieno pradinio taško: X0, X1 ir Xm
initial_points = [(X0, 'X0'), (X1, 'X1'), (Xm, 'Xm')]

# 5 punkto vykdymo rezultatai bus naudojami 6 punkto palyginimui
summary_by_start = []

for x_start, label in initial_points:
    x_pradinis = list(x_start)
    total_steps = 0
    total_func_calls = 0
    last_B_min = None
    last_x_min = None
    print(f"\n--- Pradinis taskas {label} = {np.round(x_start, 6)} ---")
    for r_value in r_sequence:
        x_min, k, f_min, func_count, trajektorija = simplekso.simplekso_fun(
            baudos_funkcija_su_r(r_value),
            x_pradinis,
            delta=0.05,
            eps=1e-6,
            Nmax=500,
        )
        print(f"  r={r_value}: iteracijos={k}, funkciju_skaiciavimai={func_count}")
        total_steps += k
        total_func_calls += func_count
        last_B_min = f_min
        last_x_min = x_min
        # Naudojame rastą sprendinį kaip pradinį tašką sekančiam r
        x_pradinis = x_min

    summary_by_start.append(
        {
            'label': label,
            'x_solution': last_x_min,
            'B_min_estimate': last_B_min,
            'f_value': f(last_x_min),
            'g_value': g(last_x_min),
            'h_value': h(last_x_min),
            'total_steps': total_steps,
            'total_func_calls': total_func_calls,
        }
    )


# 6. Palyginame rezultatus pagal pradinį tašką
print("\n6. Rezultatu palyginimas pagal pradini taska")
for row in summary_by_start:
    print(
        f"\n{row['label']}:"
    )
    print(
        f"  x* = {np.round(row['x_solution'], 6)}"
    )
    print(
        f"  f(x*) = {row['f_value']}"
    )
    print(
        f"  g(x*) = {row['g_value']}"
    )
    print(
        f"  h(x*) = {row['h_value']}"
    )
    print(
        f"  minimumo ivertis B = {row['B_min_estimate']}"
    )
    print(
        f"  zingsniu suma = {row['total_steps']}, funkciju skaiciavimu suma = {row['total_func_calls']}"
    )