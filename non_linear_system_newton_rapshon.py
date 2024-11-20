#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistemas de equações não lineares usando  método de Newton-Raphson.

@author: carlosvitor
"""
import numpy as np

def newton_raphson_system(funcs, jacobian, x0, tol=1e-6, max_iter=100):
    """
    Resolve um sistema de equações não lineares usando o método de Newton-Raphson.

    Args:
        funcs (list of callable): Lista de funções (f1, f2, ..., fn).
        jacobian (callable): Função que retorna a matriz Jacobiana.
        x0 (numpy array): Chute inicial para as variáveis.
        tol (float): Tolerância para o critério de parada.
        max_iter (int): Número máximo de iterações.

    Returns:
        numpy array: Solução aproximada.
    """
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        # Avaliar as funções no ponto atual
        F = np.array([f(*x) for f in funcs])
        # Avaliar a Jacobiana no ponto atual
        J = np.array(jacobian(*x))
        
        # Regularizar Jacobiana
        J += np.eye(len(x)) * 1e-6  # Adiciona um pequeno valor na diagonal
        
        # Resolver o sistema linear para Delta x
        try:
            delta_x = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("Jacobian não invertível no ponto atual!")
            print("Valores da Jacobiana:", J)
            return None
        
        # Atualizar x
        x += delta_x
        
        # Critério de parada
        if np.linalg.norm(delta_x) < tol:
            print(f"Solução encontrada em {i+1} iterações.")
            return x
    
    print("O método não convergiu dentro do número máximo de iterações.")
    return None

# Exemplo: Sistema de equações não lineares
# f1(x, y) = x^2 + y^2 - 4
# f2(x, y) = x * y - 1
def f1(x, y):
    return x**2 + y**2 - 4

def f2(x, y):
    return x * y - 1

# Matriz Jacobiana do sistema
def jacobian(x, y):
    return [
        [2 * x, 2 * y],  # Derivadas parciais de f1
        [y, x]           # Derivadas parciais de f2
    ]

# Chute inicial
x0 = [1.5, 1.5]

# Resolver o sistema
solution = newton_raphson_system([f1, f2], jacobian, x0)

if solution is not None:
    print("\nSolução do sistema:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x:.6f}")
