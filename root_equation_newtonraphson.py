#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: carlosvitor
"""

def newton_raphson(func, deriv, x0, tol=1e-6, max_iter=100):
    """
    Resolve f(x) = 0 usando o método de Newton-Raphson.

    Args:
        func (callable): Função f(x).
        deriv (callable): Derivada f'(x).
        x0 (float): Chute inicial.
        tol (float): Tolerância para o critério de parada.
        max_iter (int): Número máximo de iterações.

    Returns:
        float: Raiz aproximada da equação.
    """
    x = x0
    for i in range(max_iter):
        f_x = func(x)
        f_prime_x = deriv(x)
        
        if abs(f_prime_x) < 1e-12:  # Evitar divisão por zero
            print("Derivada muito próxima de zero. Método falhou.")
            return None
        
        # Atualizar o valor de x
        x_new = x - f_x / f_prime_x
        
        # Critério de parada
        if abs(x_new - x) < tol:
            print(f"Solução encontrada em {i+1} iterações: x = {x_new:.6f}")
            return x_new
        
        x = x_new
    
    print("O método não convergiu dentro do número máximo de iterações.")
    return None

# Exemplo: Resolver f(x) = x^3 - x - 2
def func(x):
    return x**3 - x - 2

def deriv(x):
    return 3*x**2 - 1

# Chute inicial
x0 = 1.5

# Resolver a equação
root = newton_raphson(func, deriv, x0)

if root is not None:
    print(f"\nRaiz aproximada: x = {root:.6f}")
