import numpy as np
import matplotlib.pyplot as plt

def calcular_campo_aislado(q, r0, x, y):
    dx = x - r0[0]
    dy = y - r0[1]
    dist_sq = dx**2 + dy**2
    dist_sq[dist_sq == 0] = 1e-12
    dist = np.sqrt(dist_sq)
    return q * dx / dist**3, q * dy / dist**3

# Configuración de la rejilla
n = 100
x_range = np.linspace(-5, 5, n)
y_range = np.linspace(-5, 5, n)
X, Y = np.meshgrid(x_range, y_range)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- LADO IZQUIERDO: FUENTE (+) ---
Ex1, Ey1 = calcular_campo_aislado(1, (0, 0), X, Y)
ax1.streamplot(X, Y, Ex1, Ey1, color='red', density=1.2, linewidth=1, arrowstyle='->')
ax1.plot(0, 0, 'o', markersize=20, color='red')
ax1.set_title('Carga Positiva: Fuente (Source)')
ax1.set_aspect('equal')
ax1.legend()

# --- LADO DERECHO: SUMIDERO (-) ---
Ex2, Ey2 = calcular_campo_aislado(-1, (0, 0), X, Y)
ax2.streamplot(X, Y, Ex2, Ey2, color='blue', density=1.2, linewidth=1, arrowstyle='->')
ax2.plot(0, 0, 'o', markersize=20, color='blue')
ax2.set_title('Carga Negativa: Sumidero (Sink)')
ax2.set_aspect('equal')
ax2.legend()

plt.tight_layout()
plt.show()