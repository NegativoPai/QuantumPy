import numpy as np

L = 1.0  # Comprimento da caixa
N = 500  # Número de pontos para plotar a função de onda

x = np.linspace(0, L, N)

# Δx é o passo entre os pontos, calculado como a diferença entre o segundo e o primeiro ponto
dx = x[1] - x[0]  # Passo entre os pontos

# V(x) é o potencial dentro da caixa, que é zero, e infinito fora da caixa. Para simplificar, consideramos apenas o potencial dentro da caixa.
V = np.zeros(N)  # Potencial dentro da caixa é zero

print(x[0])
print(x[-1])
print(len(x))

print(dx)
print(V[:5])