import numpy as np
import matplotlib.pyplot as plt

L = 1.0  # Comprimento da caixa
N = 500  # Número de pontos para plotar a função de onda

hbar = 1.0  # Constante de Planck reduzida (h/2π)
m = 1.0  # Massa da partícula

x = np.linspace(0, L, N)

# Δx é o passo entre os pontos, calculado como a diferença entre o segundo e o primeiro ponto
dx = x[1] - x[0]  # Passo entre os pontos

# V(x) é o potencial dentro da caixa, que é zero, e infinito fora da caixa. Para simplificar, consideramos apenas o potencial dentro da caixa.
V = np.zeros(N)  # Potencial dentro da caixa é zero

coef_diagonal = hbar**2 / (m * dx**2)       # valor da diagonal principal (parte cinética)
coef_off       = -hbar**2 / (2 * m * dx**2)  # valor das diagonais laterais

diag_principal = coef_diagonal + V  # A diagonal principal é a soma do termo cinético e do potencial
diag_lateral = np.full(N - 1, coef_off)  # As diagonais laterais são constantes e iguais a coef_off

np.diag(diag_principal, k=0)
np.diag(diag_lateral, k=1)
np.diag(diag_lateral, k=-1)

H = np.diag(diag_principal) + np.diag(diag_lateral, k=1) + np.diag(diag_lateral, k=-1)

energias, autoestados = np.linalg.eigh(H)

print(x[0])
print(x[-1])
print(len(x))

print(dx)
print(V[:5])

print("\nCoeficientes:")
print(f"Diagonal principal: {coef_diagonal}")
print(f"Diagonais laterais: {coef_off}")

# Construção da matriz Hamiltoniana usando as diagonais
print("\nMatriz Hamiltoniana (diagonais):")
print("Diagonal principal:", diag_principal[:3])  # Mostra os primeiros 3
print("Diagonais laterais:", diag_lateral[:3])   # Mostra os primeiros 3
print(len(diag_principal), len(diag_lateral))
print("\nMatriz Hamiltoniana completa:")
print(H.shape)
print(H[0, :4])
print(H[1, :4])

# Cálculo dos autovalores e autovetores
print("\nEnergias (autovalores):")
print(energias[:7])  # Mostra as 7 primeiras energias
print("\nAutoestados (autovetores):")
print(autoestados.shape) # Verifica a forma da matriz de autovetores

# Matplotlib

psi_1 = autoestados[:, 0]  # Primeiro autovetor (estado fundamental)

ffig, axes = plt.subplots(2, 3, figsize=(12, 6))
ffig.patch.set_facecolor('black')

for i in range(6):
    linha  = i // 3
    coluna = i % 3
    ax = axes[linha, coluna]

    psi_n  = autoestados[:, i]
    prob_n = psi_n ** 2

    ax.set_facecolor('black')
    ax.plot(x, psi_n, color='cyan', linewidth=1.5, label='ψ(x)')
    ax.fill_between(x, prob_n, alpha=0.4, color='lime', label='|ψ|²')
    ax.set_title(f"n={i+1}  E={energias[i]:.2f}", color='white')
    ax.set_xlabel("x", color='white')
    ax.set_ylabel("ψ(x)", color='white')
    ax.tick_params(colors='white')
    ax.grid(True, color='green', linewidth=0.4, alpha=0.5)
    ax.legend(fontsize=7, labelcolor='white', facecolor='black')
    for spine in ax.spines.values():
        spine.set_edgecolor('green')

plt.tight_layout()
plt.show()