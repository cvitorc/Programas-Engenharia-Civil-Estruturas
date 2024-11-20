#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Entrada do arquivo: O usuário fornece o caminho para o arquivo Excel.
Leitura dos dados: O programa lê as 5 primeiras colunas como coeficientes e a última como termos independentes.
Validação: O programa valida o número de colunas (6) e linhas (5).
Resolução: O sistema é resolvido com numpy.linalg.solve.
Resultado: A solução é exibida no terminal.

@author: carlosvitor
"""

import numpy as np
import pandas as pd

def solve_system_5x5_from_excel(file_path):
    try:
        # Ler o arquivo Excel
        data = pd.read_excel(file_path)
        
        # Verificar se o arquivo contém as colunas esperadas
        if len(data.columns) != 6:
            print("Erro: O arquivo deve conter exatamente 6 colunas (5 coeficientes e 1 termo independente).")
            return
        
        # Extrair a matriz de coeficientes (A) e o vetor de resultados (B)
        A = data.iloc[:, :-1].values  # As 5 primeiras colunas
        B = data.iloc[:, -1].values   # A última coluna
        
        if A.shape != (5, 5) or B.shape != (5,):
            print("Erro: O arquivo deve conter exatamente 5 linhas de dados.")
            return
        
        # Resolver o sistema de equações
        X = np.linalg.solve(A, B)
        
        # Exibir a solução
        print("\nSolução do sistema:")
        for i, x in enumerate(X):
            print(f"x{i+1} = {x:.4f}")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o caminho fornecido.")
    except ValueError:
        print("Erro: Os dados no arquivo não estão formatados corretamente.")
    except np.linalg.LinAlgError:
        print("Erro: O sistema não possui solução única (pode ser inconsistente ou dependente).")

# Caminho para o arquivo Excel
file_path = input("Digite o caminho para o arquivo Excel: ")

# Executar o programa
solve_system_5x5_from_excel(file_path)


