#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:06:31 2024

@author: carlosvitor
"""

import math

def calcular_tensao_normal(forca, diametro):
    """
    Calcula a tensão normal em um cabo circular.

    Args:
        forca (float): Força aplicada em N (Newton).
        diametro (float): Diâmetro do cabo em m (metros).

    Returns:
        float: Tensão normal em MPa (Megapascal).
    """
    # Raio do cabo
    raio = diametro / 2
    
    # Área da seção transversal
    area = math.pi * raio**2
    
    # Tensão normal
    tensao = forca / area  # Pa (Pascal)
    
    # Converter para MPa
    tensao_mpa = tensao / 10**6
    return tensao_mpa

# Dados fornecidos
forca = 15000  # Força aplicada (N)
diametro = 0.05  # Diâmetro do cabo (m)

# Calcular a tensão normal
tensao_normal = calcular_tensao_normal(forca, diametro)

# Exibir o resultado
print(f"A tensão normal no cabo é {tensao_normal:.2f} MPa.")
