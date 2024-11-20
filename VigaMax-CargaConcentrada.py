# Dados da viga e carga
comprimento_viga = 10  # metros (L)
carga_concentrada = 10  # kN (P)
a = 3  # metros (posição da carga a partir do apoio esquerdo)
b = comprimento_viga - a  # metros (posição da carga a partir do apoio direito)

# Dimensões da seção transversal (em cm)
base = 30  # cm
altura = 50  # cm

# Conversão para metros
base_m = base / 100  # metros
altura_m = altura / 100  # metros

# Reações nos apoios
R_A = carga_concentrada * b / comprimento_viga  # kN
R_B = carga_concentrada * a / comprimento_viga  # kN

# Momento máximo
momento_maximo = R_A * a  # kN·m

# Cálculo do momento de inércia (I)
momento_inercia = (base_m * altura_m**3) / 12  # m^4

# Cálculo da distância máxima do centroide (y)
y_max = altura_m / 2  # metros

# Cálculo da tensão máxima
tensao_maxima_kPa = (momento_maximo * 1e3 * y_max) / momento_inercia  # Pa
tensao_maxima_MPa = tensao_maxima_kPa / 1000000 # MPa

# Exibindo resultados
print(f"Reação no apoio esquerdo (R_A): {R_A:.2f} kN")
print(f"Reação no apoio direito (R_B): {R_B:.2f} kN")
print(f"Momento máximo na viga: {momento_maximo:.2f} kN·m")
print(f"Tensão máxima na seção transversal: {tensao_maxima_MPa:.3f} MPa")
