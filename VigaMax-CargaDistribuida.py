# Dados da viga
carga_distribuida = 150  # kN/m
comprimento_viga = 8     # metros

# Dimensões da seção transversal (em cm)
base = 20  # cm
altura = 50  # cm

# Conversão para metros
base_m = base / 100  # metros
altura_m = altura / 100  # metros

# Cálculo do momento máximo
momento_maximo = (carga_distribuida * comprimento_viga**2) / 8  # kN·m

# Cálculo do momento de inércia (I)
momento_inercia = (base_m * altura_m**3) / 12  # m^4

# Cálculo da distância máxima do centroide (y)
y_max = altura_m / 2  # metros

# Cálculo da tensão máxima
tensao_maxima = (momento_maximo * 1e3 * y_max) / momento_inercia  # kPa
tensao_maxima = tensao_maxima/1000000 # MPa
# Exibindo resultados
print(f"O momento máximo na viga biapoiada é {momento_maximo:.2f} kN·m.")
print(f"A tensão máxima na seção transversal é {tensao_maxima:.2f} MPa.")
