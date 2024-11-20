#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:23:28 2024

@author: carlosvitor
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def calcular_tensao_normal(forca, diametro):
    """
    Calcula a tensão normal em um cabo circular.

    Args:
        forca (float): Força aplicada em N (Newton).
        diametro (float): Diâmetro do cabo em m (metros).

    Returns:
        float: Tensão normal em MPa (Megapascal).
    """
    raio = diametro / 2
    area = math.pi * raio**2
    tensao = forca / area  # Tensão em Pascal
    return tensao / 10**6  # Converter para MPa


def converter_unidades(valor, unidade):
    """
    Converte unidades para o formato padrão.

    Args:
        valor (float): Valor numérico a ser convertido.
        unidade (str): Unidade atual do valor.

    Returns:
        float: Valor convertido.
    """
    if unidade == "kN":
        return valor * 10**3  # Converter kN para N
    elif unidade == "cm":
        return valor / 100  # Converter cm para m
    else:
        return valor


def salvar_resultado(forca, diametro, tensao):
    """
    Salva os resultados em um arquivo Excel.

    Args:
        forca (float): Força aplicada em N.
        diametro (float): Diâmetro do cabo em m.
        tensao (float): Tensão normal em MPa.
    """
    dados = {
        "Força Aplicada (N)": [forca],
        "Diâmetro do Cabo (m)": [diametro],
        "Tensão Normal (MPa)": [tensao],
    }
    df = pd.DataFrame(dados)
    file_path = "resultado_tensao.xlsx"
    df.to_excel(file_path, index=False)
    print(f"Resultado salvo no arquivo: {file_path}")


def plotar_grafico():
    """
    Plota um gráfico da relação entre força, diâmetro e tensão normal.
    """
    forcas = np.linspace(1000, 20000, 100)  # Forças variando de 1kN a 20kN
    diametros = [0.02, 0.05, 0.1]  # Três diferentes diâmetros
    plt.figure(figsize=(8, 6))
    for diametro in diametros:
        tensoes = [calcular_tensao_normal(f, diametro) for f in forcas]
        plt.plot(forcas / 10**3, tensoes, label=f"Diâmetro {diametro*100:.0f} cm")
    plt.title("Tensão Normal vs Força Aplicada")
    plt.xlabel("Força Aplicada (kN)")
    plt.ylabel("Tensão Normal (MPa)")
    plt.legend()
    plt.grid(True)
    plt.show()


def main_tkinter():
    """
    Interface gráfica para calcular a tensão normal em um cabo circular.
    """
    def calcular():
        try:
            forca = float(entry_forca.get())
            diametro = float(entry_diametro.get())
            resultado = calcular_tensao_normal(forca, diametro)
            salvar_resultado(forca, diametro, resultado)
            messagebox.showinfo(
                "Resultado",
                f"A tensão normal no cabo é {resultado:.2f} MPa. Resultado salvo no arquivo.",
            )
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

    # Criar a interface
    root = tk.Tk()
    root.title("Cálculo de Tensão Normal")

    tk.Label(root, text="Força Aplicada (N):").grid(row=0, column=0)
    entry_forca = tk.Entry(root)
    entry_forca.grid(row=0, column=1)

    tk.Label(root, text="Diâmetro do Cabo (m):").grid(row=1, column=0)
    entry_diametro = tk.Entry(root)
    entry_diametro.grid(row=1, column=1)

    btn_calcular = tk.Button(root, text="Calcular", command=calcular)
    btn_calcular.grid(row=2, columnspan=2)

    root.mainloop()


def main():
    """
    Menu principal para acessar todas as funcionalidades.
    """
    print("Bem-vindo ao programa de cálculo de tensão normal!")
    print("Escolha uma das opções abaixo:")
    print("1. Calcular a tensão normal diretamente")
    print("2. Plotar gráfico da relação força vs tensão")
    print("3. Usar interface gráfica (Tkinter) para cálculo interativo")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        forca = float(input("Digite a força aplicada: "))
        unidade_forca = input("Unidade da força (N ou kN): ").strip().lower()
        forca = converter_unidades(forca, unidade_forca)

        diametro = float(input("Digite o diâmetro do cabo: "))
        unidade_diametro = input("Unidade do diâmetro (m ou cm): ").strip().lower()
        diametro = converter_unidades(diametro, unidade_diametro)

        tensao = calcular_tensao_normal(forca, diametro)
        print(f"A tensão normal no cabo é {tensao:.2f} MPa.")
        salvar_resultado(forca, diametro, tensao)

    elif opcao == "2":
        plotar_grafico()

    elif opcao == "3":
        main_tkinter()

    else:
        print("Opção inválida. Encerrando o programa.")


if __name__ == "__main__":
    main()

