#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Desenha 2 funcoes

@author: carlosvitor
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir as funções
def f1(x):
    return 2*x**2 - 3*x + 1  # Função de 2º grau: ax^2 + bx + c

def f2(x):
    return 4*x - 2  # Função de 1º grau: mx + b

# Geração de valores para x
x = np.linspace(-5, 5, 500)  # Intervalo de -5 a 5

# Calcular os valores das funções
y1 = f1(x)
y2 = f2(x)

# Criar o gráfico
plt.figure(figsize=(8, 6))

# Plotar a função de 2º grau
plt.plot(x, y1, label="f1(x) = 2x² - 3x + 1", color="blue", linewidth=2)

# Plotar a função de 1º grau
plt.plot(x, y2, label="f2(x) = 4x - 2", color="red", linestyle="--", linewidth=2)

# Configurações do gráfico
plt.title("Gráfico das Funções de 2º Grau e 1º Grau", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Eixo x
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Eixo y
plt.grid(True)
plt.legend(fontsize=12)

# Mostrar o gráfico
plt.show()
