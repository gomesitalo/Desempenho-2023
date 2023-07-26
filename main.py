# Função principal da classe desempenho - 2023

from desempenho import desempenho
import os
os.system("cls")

print("\nDigite o local o qual você deseja fazer a avaliação de desempenho\n")
AD = input("[F] para Fortaleza, [S] para São Paulo ou ainda [I] para o ITA: ") # AD = altitude-densidade

if AD == 'F':
    p = 1.225 # Densidade-padrão estimada em 0m (Apêndice A - ANDERSON, 2015)
elif AD == 'S':
    p = 1.156 # Densidade-padrão estimada em 600m (Apêndice A - ANDERSON, 2015)
elif AD == 'I':
    p = 1.090 # Densidade-padrão estimada em 1200m (Apêndice A - ANDERSON, 2015)

os.system("cls")

# Instâncias (inputs) das funções de desempenho
det1 = desempenho(9.80665, 0.09, 0.09666355488, 2.21, 0.0067, 0.28, 2.29, 1.366, p, '15x10', 30.0, 2.5)

'''
1º. gravidade em m/s² (g)
2º. coef. de atrito dinâmico (mu)
3º. const. de proporcionalidade (K)
4º. coef. de sustentação máximo (Clmax) # Antigo valor = 1.962293953, 2º Clmax = 2.524, 3º Clmax = 2.424
5º. coef. de arrasto mínimo (Cdmin ou Cd0)
6º. altura da asa em relação ao solo (hw)
7º. envergadura da asa (bw)
8º. área da asa (Sw)
9º. densidade padrão local de análise (p)
10º tipo de hélice (prop)
11º bank angle - ângulo da curva em graus (phi_turn)
12º fator de carga máx. positivo (n_max)
'''

# Mtow e Estol
print(f"O mtow máximo encontrado é {det1.Mtow:.4} kg\n")
#print(f"A densidade encontrada é {det1.altitude_densidade():.2} kg/m³\n")
print(f"A velocidade de estol é {det1.vel_estol():.4} m/s")
print(f"A velocidade de rotação é {det1.vel_liftoff():.5} m/s")
print(f"A velocidade de transição é {det1.vel_transition():.5} m/s")
print(f"A velocidade de subida é {det1.vel_climb():.5} m/s")
print(f"A tração máxima é {det1.tracao_max():.5} N\n")

# Decolagem
print(f"A velocidade de decolagem é {det1.vel_liftoff():.5} m/s")
print(f"A aceleração média no momento de decolagem é {det1.decolagem_obstaculo()[0]:.4} m/s²")
print(f"A distância de corrida no solo é {det1.decolagem_obstaculo()[1]:.5} m")
print(f"A distância de rotação é {det1.decolagem_obstaculo()[2]:.5} m")
print(f"A distância de transição é {det1.decolagem_obstaculo()[3]:.5} m")
print(f"A distância de subida ao obstáculo é {det1.decolagem_obstaculo()[4]:.5} m")
print(f"A distância total de decolagem é {det1.decolagem_obstaculo()[5]:.5} m")
print(f"A altura de transição é {det1.decolagem_obstaculo()[6]:.4} m")
print(f"O raio de curvatura é de {det1.decolagem_obstaculo()[7]:.6}")
print(f"O ângulo necessário para subida ao obstáculo é {det1.decolagem_obstaculo()[8]:.4}°")
print(f"O tempo total de decolagem é de {det1.decolagem_obstaculo()[9]:.4} s")
print(f"A razão de subida no momento de transição é {det1.decolagem_obstaculo()[10]:.4} m/s\n")

# Subida
print(f"A razão de subida no momento de decolagem é {det1.subida(det1.vel_liftoff())[3]:.4} m/s")
print(f"O ângulo de subida para a velocidade de decolagem é {det1.subida(det1.vel_liftoff())[4]:.4}°")
print(f"A máxima razão de subida é {det1.subida(det1.vel_liftoff())[0]:.4} m/s")
print(f"O ângulo de subida para a máxima razão de subida é {det1.subida(det1.vel_liftoff())[2]:.4}°")
print(f"A velocidade durante a máxima razão de subida é {det1.subida(det1.vel_liftoff())[1]:.5} m/s")
print(f"O tempo de subida para a máxima razão de subida é {det1.subida(det1.vel_liftoff())[5]:.4} s")
print(f"O tempo de subida para a velocidade mínima de subida é {det1.subida(det1.vel_liftoff())[6]:.5} s\n")
det1.gráfico()

# Cruzeiro
print(f"A velocidade de máximo alcance é {det1.vel_max_alcance():.5} m/s")
print(f"A velocidade de máxima autonomia é {det1.vel_max_autonomia():.5} m/s")
print(f'A velocidade mínima da aeronave é {det1.cruzeiro()[0]:.5} m/s')
print(f'A velocidade máxima da aeronave é {det1.cruzeiro()[1]:.5} m/s')
print(f'A velocidade mínima durante o voo de cruzeiro é {det1.cruzeiro()[2]:.5} m/s')
print(f'A velocidade máxima durante o voo de cruzeiro é {det1.cruzeiro()[3]:.5} m/s')
print(f"O tempo de cruzeiro para máximo alcance é {det1.cruzeiro()[4]:.5} s")
print(f"O tempo de cruzeiro para máxima autonomia é {det1.cruzeiro()[5]:.5} s\n")

# Manobra
print(f"A aceleração para realizar uma curva de {det1.phi_turn:.3}° é: {det1.manobra()[0]:.4} m/s²")
print(f"O raio para realizar uma curva de {det1.phi_turn:.3}° é: {det1.manobra()[1]:.5} m")
print(f"O tempo para realizar uma curva de {det1.phi_turn:.3}° é: {det1.manobra()[2]:.4} s")
print(f"A velocidade angular para um ângulo de curva de {det1.phi_turn:.3}° é: {det1.manobra()[3]:.4} rad/s\n")

# Descida
print(f"O ângulo de planeio para a máxima distância de planeio é {det1.descida()[0]:.3} °")
print(f"A velocidade de planeio para a condição de máxima distância de planeio é {det1.descida()[1]:.4} m/s")
print(f"A distância de descida para a máxima eficiência aerodinâmica é {det1.descida()[2]:.4} m")
print(f'A razão de descida para a condição de máxima eficiência aerodinâmica é {det1.descida()[3]:.4} m/s')
print(f'A mínima razão de descida é {det1.descida()[4]:.4} m/s')
print(f'A velocidade durante a mínima razão de descida é {det1.descida()[5]:.5} m/s')
print(f'O ângulo durante a mínima razão de descida é {det1.descida()[6]:.4} °')
print(f'O tempo de descida é de {det1.descida()[7]:.4} s\n')

# Pouso
#print(f"A distância de pouso (FAR-23) é de {det1.pouso()[0]:.6} m")
#print(f"A distância de pouso real é de {det1.pouso()[1]:.6} m")
#print(f"O ângulo de planeio mínimo para pouso é {det1.pouso()[2]:.4}°")
#print(f"A velocidade para o ângulo de planeio mínimo (máx distânca) é {det1.pouso()[3]:.5} m/s\n")

# Envelope de voo

# Carga útil em função da altitude-densidade