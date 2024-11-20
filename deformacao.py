#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: carlosvitor
"""

def calcular_deformacao(carga, area_transversal_mm2, modulo_elasticidade):
    """
    Função para calcular a deformação em uma barra devido a uma carga axial conhecida.

    Args:
    - carga: A carga axial aplicada à barra (em Newtons).
    - area_transversal_mm2: A área transversal da barra (em milímetros quadrados).
    - modulo_elasticidade: O módulo de elasticidade do material (em Pascals).

    Returns:
    - deformacao: A deformação na barra (adimensional).
    """
    area_transversal_m2 = area_transversal_mm2 / (1000 ** 2)  # Convertendo mm² para m²
    deformacao = carga / (area_transversal_m2 * modulo_elasticidade)
    return deformacao

def main():
    # Dados do material
    area_transversal_mm2 = float(input("Digite a área transversal da barra (em mm^2): "))
    modulo_elasticidade = float(input("Digite o módulo de elasticidade do material (em Pa): "))

    # Carga axial
    carga = float(input("Digite a carga axial aplicada à barra (em N): "))

    # Chamada da função para calcular a deformação
    deformacao = calcular_deformacao(carga, area_transversal_mm2, modulo_elasticidade)

    # Exibição do resultado
    print("A deformação na barra é de", deformacao, "m/m.")

if __name__ == "__main__":
    main()
