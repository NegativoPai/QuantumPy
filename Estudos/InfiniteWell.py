import numpy as np
import matplotlib.pyplot as plt

V0 = 50.0
L = 1.0
N = 1000
x = np.linspace(0, L, N)
V = np.full(N, V0)
V[(x >= L/4) & (x <= 3*L/4)] = 0.0

print("Potential V(x):")
print(V)

plt.plot(x, V)
plt.title("Potential V(x) for the Infinite Well")
plt.xlabel("Position x")
plt.ylabel("Potential V(x)")
plt.grid()
plt.show()