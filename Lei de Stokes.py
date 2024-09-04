import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a velocidade de sedimentação com base na Lei de Stokes
def calc_velocidade_sedimentacao(g, rho_p, rho_f, d, mu):
    """
    Calcula a velocidade de sedimentação de uma partícula esférica.

    Parâmetros:
    g (float): aceleração gravitacional (m/s²)
    rho_p (float): densidade da partícula (kg/m³)
    rho_f (float): densidade do fluido (kg/m³)
    d (float): diâmetro da partícula (m)
    mu (float): viscosidade do fluido (Pa.s)

    Retorna:
    float: velocidade de sedimentação (m/s)
    """
    return (g * (rho_p - rho_f) * d**2) / (18 * mu)

# Função para calcular o tempo necessário para percorrer uma altura dada a velocidade de sedimentação
def calc_tempo_sedimentacao(h, v_s):
    """
    Calcula o tempo de sedimentação com base na altura e na velocidade de sedimentação.

    Parâmetros:
    h (float): altura (m)
    v_s (float): velocidade de sedimentação (m/s)

    Retorna:
    float: tempo necessário (s)
    """
    return h / v_s

# Parâmetros para os cálculos - modifique esses valores de acordo com o seu caso

g = 9.81  # aceleração gravitacional (m/s²)
rho_p = 2600  # densidade da partícula (kg/m³) - exemplo para partículas de bentonita
rho_f = 997  # densidade do fluido (kg/m³) - exemplo para água
mu = 0.00095  # viscosidade do fluido (Pa.s) - exemplo para água a 20°C
d = 2e-6  # diâmetro da partícula (m) - exemplo de 2 micrômetros
h = 0.09  # altura da proveta (m) - exemplo de 9 cm, *VALOR ARBITRÁTIO ESCOLHIDO PELO PESQUISADOR*

# Cálculo da velocidade de sedimentação e tempo de sedimentação
v_s = calc_velocidade_sedimentacao(g, rho_p, rho_f, d, mu) # Velocidade de sedimentação em m/s
t = calc_tempo_sedimentacao(h, v_s) # Tempo de sedimentação em Segundos
t_h = t/3600 # Tempo em Horas

# Exibir os resultados
print(f'Velocidade de sedimentação: {v_s:.10f} m/s')
print(f'Tempo necessário para sedimentação: {t_h:.4f} h')

