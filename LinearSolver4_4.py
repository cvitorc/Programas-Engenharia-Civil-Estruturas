"""


Entrada dos dados:
O usuário digita os coeficientes das equações a,b,c,d e os termos independentes 

A matriz Acontém os coeficientes das variáveis.
O vetor B B contém os resultados de cada equação.
Resolução do sistema:
O programa utiliza numpy.linalg.solve, que resolve sistemas lineares usando a decomposição LU.
Validação:
Caso o sistema seja inconsistente ou dependente, o programa exibirá uma mensagem de erro.

@author: carlosvitor
"""


import numpy as np




def solve_system():
    print("Bem-vindo ao resolvedor de sistemas de equações 4x4!")
    
    # Coletar os coeficientes das equações
    print("Digite os coeficientes das 4 equações na forma ax + by + cz + dw = e:")
    A = []  # Matriz dos coeficientes
    for i in range(4):
        print(f"Equação {i+1}:")
        row = list(map(float, input(f"Digite os coeficientes a{i+1}, b{i+1}, c{i+1}, d{i+1} separados por espaço: ").split()))
        if len(row) != 4:
            print("Por favor, insira exatamente 4 coeficientes!")
            return
        A.append(row)
    
    B = []  # Vetor de resultados
    for i in range(4):
        b = float(input(f"Digite o termo independente da equação {i+1} (e{i+1}): "))
        B.append(b)
    
    # Convertendo listas para arrays numpy
    A = np.array(A)
    B = np.array(B)
    
    try:
        # Resolvendo o sistema de equações
        X = np.linalg.solve(A, B)
        print("\nSolução do sistema:")
        for i, x in enumerate(X):
            print(f"x{i+1} = {x:.4f}")
    except np.linalg.LinAlgError:
        print("O sistema não possui solução única (pode ser inconsistente ou dependente).")

# Executar o programa
if __name__ == "__main__":
    solve_system()
