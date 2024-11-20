#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
desenha 2 funcoes

@author: carlosvitor
"""

import numpy as np
import matplotlib.pyplot as plt

# Definição das funções
def f1(x, y):
    return x**2 + y**2 - 4

def f2(x, y):
    return x * y - 1

# Geração dos valores de x e y
x = np.linspace(-3, 3, 500)
y = np.linspace(-3, 3, 500)
X, Y = np.meshgrid(x, y)

# Calcular os valores de f1 e f2
Z1 = f1(X, Y)
Z2 = f2(X, Y)

# Criar o gráfico
plt.figure(figsize=(8, 8))

# Contornos de f1(x, y) = 0 (curva da primeira equação)
plt.contour(X, Y, Z1, levels=[0], colors='blue', linewidths=2, label="f1(x, y) = 0")

# Contornos de f2(x, y) = 0 (curva da segunda equação)
plt.contour(X, Y, Z2, levels=[0], colors='red', linewidths=2, label="f2(x, y) = 0")

# Configurações do gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Curvas das funções f1(x, y) e f2(x, y)", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True)
plt.legend(["f1(x, y) = 0", "f2(x, y) = 0"], loc="upper left")

# Mostrar o gráfico
plt.show()
