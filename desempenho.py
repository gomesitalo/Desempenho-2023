# Classe desempenho do código de integração de desempenho - 2023

from curvas import curvas
import math as m
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt

class desempenho:

    def __init__(self, g, mu, K, Clmax, Cdmin, hw, bw, Sw, p, prop):
        self.g = g
        self.mu = mu
        self.K = K
        self.Clmax = Clmax
        self.Cdmin = Cdmin
        self.hw = hw
        self.bw = bw
        self.Sw = Sw
        self.p = p
        self.rho = desempenho.altitude_densidade(self)
        self.prop = prop
        #self.Mtow = 19.7 # Mtow máximo definido pelo MDO
        self.Mtow = desempenho.mtow_obstaculo(self) # Mtow máximo calculado
        self.W = self.Mtow*self.g
        pass

    def altitude_densidade(self):
        # Pressão e Temperatura locais, e Densidade e Altitude-Densidade encontradas/especuladas:
        ''' Fortaleza =  1014 hPa, 30°C (303.15 K), 1.165 kg/m³, 517.817 m
            São Paulo =   980 hPA, 25°C (298.15 K), 1.081 kg/m³, 697.336 m
            S.J.C.    =   950 hPa, 22°C (295.15 K), 0.998 kg/m³, 911.870 m
        '''
        P0, T0 = 1013.25, 288.15 # pressão e temperatura de referência ao nível do mar (Regulamento de 2023 / Apêndice 4)
        
        if self.p == 1.225:
            rho_local = self.p # densidade-padrão à nivel do mar para 0m
            P_local, T_local = 1014, 303.15 # pressão e temperatura máx médias em hPa e Kelvin (Fortaleza)
        elif self.p == 1.156:
            rho_local = self.p # densidade-padrão à nivel do mar para 600m
            P_local, T_local = 980, 298.15 # pressão e temperatura máx médias em hPa e Kelvin (São Paulo)
        elif self.p == 1.090:
            rho_local = self.p # densidade-padrão à nivel do mar para 1200m
            P_local, T_local = 950, 295.15 # pressão e temperatura máx médias em hPa e Kelvin (São José dos Campos)
        hp = (T0/0.0065)*(1-((P_local/P0)/(T_local/T0))**0.234959) # Altitude-Densidade (Regulamento de 2023 / Apêndice 4)
        rho =  round((rho_local*(1-(0.000022558*hp))**4.2561),3) # Densidade do ar (kg/m³) (Gudmundsson - Capítulo 16 / Eq. 19)
        return rho # Retorna a densidade do ar corrigida pela altitude-densidade
    
    def efeito_solo(self):
        return ((16*self.hw/self.bw)**2)/((1+(16*self.hw/self.bw)**2)) # Efeito solo durante a decolagem e o pouso (McCormick)
    
    def vel_estol(self): # Velocidade na qual a aeronave entra em 'stall'
        return m.sqrt((2*(self.W))/(self.rho*self.Sw*self.Clmax))
    
    # Vrot, Vlof, Vtr e Vclimb(ou V2) são estabelecidas pela norma: 14 CFR Part 23, § 23.51 Takeoff Speeds #

    def vel_liftoff(self): # Velocidade estimada para o início da rotação da aeronave, Vr ou Vlof (Gudmundsson, 2014)
        return 1.1*desempenho.vel_estol(self)
    
    def vel_liftoff_070(self): # Velocidade ideal estimada para a subida "Vlof/raiz(2)"
        return desempenho.vel_liftoff(self)/m.sqrt(2)
    
    def vel_transition(self): # Velocidade para a aeronave atingir o ângulo de subida (θclimb), "Vtr" (Gudmundsson, 2014)
        return 1.15*desempenho.vel_estol(self)
    
    def vel_climb(self): # Velocidade estimada no momento inicial de subida do obstáculo "V2" (Gudmundsson, 2014)
        return 1.2*desempenho.vel_estol(self)
    
    def vel_aprroch(self): # Velocidade com que a aeronave se aproxima da pista de pouso (FAR Part-23)
        return 1.3*desempenho.vel_estol(self)

    def vel_landing(self): # Velocidade ideal estimada durante o pouso "Vappr/raiz(2)"
        return (desempenho.vel_aprroch(self)/m.sqrt(2))

    def vel_max_alcance(self): # Velocidade de máximo alcance, tração mínima requerida ou de máxima eficiência aerodinâmica
        return ((2*(self.W)/(self.rho*self.Sw))**0.5)*(((self.K)/self.Cdmin)**0.25)

    def vel_max_autonomia(self): # Velocidade de máxima autonomia ou de potência requerida mínima
        return ((2*(self.W)/(self.rho*self.Sw))**0.5)*(((self.K)/(3*self.Cdmin))**0.25)

    def Cl_ideal(self):
        # Cl0 + Cl_alfa*alfa_tof
        return self.mu/(2*desempenho.efeito_solo(self)*self.K)

    def Cd_ideal(self):
        return self.Cdmin + desempenho.efeito_solo(self)*self.K*(desempenho.Cl_ideal(self)**2) # CDi(IGE) = phi*self.K*Cllof**2

    def ponto_projeto(self):
        Cl_asterix = m.sqrt(self.Cdmin/self.K) # Coef. de sustentação que maximiza a eficiência aerodinâmica - ou o alcance, (Cl*)
        #Cl_asterix =  m.sqrt((3*self.Cdmin)/self.K) # Coef. de sustentação que permite planeio com máxima autonomia (Cl*)
        #Cd_asterix = self.Cdmin + self.K*Cl_asterix**2 # Coef. de arrasto para o ponto de projeto [Equivale ao "(2*self.Cdmin)"]
        E_max = Cl_asterix/(2*self.Cdmin) # Eficiência aerodinâmica máxima também escrito como (L/D)max
        return E_max
    
    def decolagem_obstaculo(self): # Corrida de decolagem com obstáculo
        # CDi = Cl**2/(m.pi*AR*e), Cl = 2*L/(rho*v**2*self.Sw), Cl_alfa = Cl/(alfa - alfa_azl), alfa_i = Cl**2/(m.pi*AR)
        hob, Sc = 0.70 + 0.15, float(0) # Altura do obstáculo + margem de segurança, Distância ao obstáculo
        
        # Determinação da corrida em solo (SG) #
        T_Vlof = curvas.tracao(self, desempenho.vel_liftoff_070(self)) # Tração na velocidade de "Vlof/sqrt(2)"
        D_Vlof = 0.5*self.rho*((desempenho.vel_liftoff_070(self))**2)*self.Sw*desempenho.Cd_ideal(self) # Arrasto na velocidade de "Vlof/sqrt(2)"
        L_Vlof = 0.5*self.rho*((desempenho.vel_liftoff_070(self))**2)*self.Sw*desempenho.Cl_ideal(self) # Lift na velocidade de "Vlof/sqrt(2)"
        ac_SG = (self.g/self.W)*(T_Vlof-D_Vlof-self.mu*((self.W)-L_Vlof)) # Aceleração média durante a corrida no solo (ac_média_SG)
        Sg = (desempenho.vel_liftoff(self)**2)/(2*ac_SG) # Distância de Ground Roll (SG)
        tSG = m.sqrt(2*Sg/ac_SG) # Tempo de corrida no solo (tSG)
         
        # Determinação do segmento de rotação (SROT) #
        Srot = desempenho.vel_liftoff(self) # A distância de rotação (SROT) é de aproximadamente o módulo da velocidade de rotação (VROT)
        tROT = 1 # O tempo da rotação é de aproximadamente 1s
         
        # Determinação do momento de transição (STR) #
        r = desempenho.vel_transition(self)**2/(self.g*0.1903) # Raio de subida (R) durante a transição [17-30] (Gudmundsson, 2014)
        T_tr = curvas.tracao(self, desempenho.vel_transition(self)) # Tração no durante a transição
        Cl_tr = 2*self.W/(self.rho*desempenho.vel_transition(self)**2*self.Sw)
        Cd_tr = self.Cdmin + desempenho.efeito_solo(self)*self.K*(Cl_tr)**2 # Coef. de arrasto durante a transição
        D_tr = 0.5*self.rho*((desempenho.vel_transition(self))**2)*self.Sw*Cd_tr # Arrasto durante a transição
        #L_tr = 0.5*self.rho*((desempenho.vel_transition(self))**2)*self.Sw*Cl_tr # Lift durante a transição
        sin_climb = m.sin((T_tr-D_tr)/(self.W)) # Seno do ângulo de subida "θ_climb"
        theta_climb = m.asin(sin_climb) # Ângulo de subida "θ_climb" em radianos
        Str = r*sin_climb # Distância de transição (STR)
        ac_STR = (desempenho.vel_transition(self)**2-desempenho.vel_liftoff(self)**2)/(2*Str) # Aceleração média durante a transição
        tTR = (desempenho.vel_transition(self)-desempenho.vel_liftoff(self))/ac_STR # Tempo que leva o momento de transição

        # Avaliação da superação do obstáculo #
        tTotal = tSG + tROT + tTR # Tempo total até o fim do segmento de transição
        Stotal = Sg + Srot + Str # Distância total percorrida até o alinhamento da aeronave com o ângulo de subida
        htr = r*(1-m.cos(theta_climb)) # Altura de transição (hTR)
        roc_lof = curvas.razao_subida(self, desempenho.vel_transition(self))
        if Stotal < 55:
            if htr < hob:
                Sc = (hob-htr)/m.tan(theta_climb) # Distância do ponto em que terminou a transição "Str" até o ponto que alcança o obstáculo
                ac_Sc = (desempenho.vel_climb(self)**2-desempenho.vel_transition(self)**2)/(2*Sc) # Aceleração média durante a subida ao obstáculo
                tSc = (desempenho.vel_climb(self)-desempenho.vel_transition(self))/ac_Sc # Tempo de subida do fim da transição até alcançar obstáculo
                Stotal += Sc # Aumenta a distância total na distância percorrida, desde o fim de "Str" até alcançar o obstáculo
                tTotal += tSc
            else:
                Sc = 55 - Stotal
        return ac_SG, Sg, Srot, Str, Sc, Stotal, htr, r, m.degrees(theta_climb), tTotal, roc_lof

    def subida(self, V):
        h = 30 # Altura definida como distância segura para aplicação de profundor e retorno à altitude desejada "h"
        v = 0.01 # Velocidade inicial para o loop 'while'
        rate_climb = [] # Cria uma lista que irá conter a razão de subida em cada velocidade de V = 0 até V = 40 m/s
        while v <= 40:
            rate_climb.append(curvas.razao_subida(self, v)) # Guarda os valores de R/C em rate_climb
            v += 0.01 # Diferencial que funciona como contador
        max_rate_c = max(rate_climb) # Pega a maior razão de subida (R/C_max) em m/s
        vel_h = (rate_climb.index(max_rate_c)+1)*0.01 # Pega a velocidade durante R/C_max - Pegamos index + 1, pois o index_inical = 0
        #print(rate_climb)
        #print(vel_h, max_rate_c, m.pi) # Testa os valores
        max_ang_subida = m.asin(max_rate_c/vel_h)*(180/m.pi) # Calcula o ângulo de subida para o R/C_max em graus
        rate_c = curvas.razao_subida(self, V) # Calcula a razão de subida  para um dado 'V' em m/s
        ang_subida = m.asin(curvas.razao_subida(self, V)/V)*(180/m.pi) # Calcula o ângulo de subida para um dado 'V' em graus
        ts = h/max_rate_c # Tempo de subida com base na máxima razão de subida
        tsmáx = h/curvas.razao_subida(self, desempenho.vel_climb(self)) # Tempo máximo de subida com velocidade de subida 'V2' constante
        return max_rate_c, vel_h, max_ang_subida, rate_c, ang_subida, ts, tsmáx
    
    def tmax(self):
        return curvas.tracao(self, 0.01)

    def gráfico(self):
        curvas.curva_ROC(self) # plota o gráfico da razão de subida # R/C
        curvas.curva_TRxTD(self) # plota o gráfico de Td x Tr em função da velocidade # Td(v) x Tr(v)

    def cruzeiro(self):
        Scr = 300 # Distância de cruzeiro em SJC
        vt = [] # Vetor que guardará os valores de V.mín e V.máx, bem como as de Tmin e Tmáx. # vt = [[Vmin, Tmin],[Vmax, Tmax]]
        Vcmin, Vcmax = 0, 0 # De acordo com a JAR-VLA 335, são as velocidades mínima e máxima durante o voo de cruzeiro
        x = sp.symbols('x')
        #tr = 0.07315*x**2 - 4.319*x + 70.77    #    0m (18,5kg)
        #tr = 0.08017*x**2 - 4.676*x + 73.99    #  600m (17,1kg)
        tr = 0.08797*x**2 - 5.058*x + 77.07     # 1200m (15,8kg)
        #td = -0.02562*x**2 + 0.03855*x + 47.5  #    0m
        #td = -0.02377*x**2 + 0.03576*x + 44.08 #  600m
        td = -0.02195*x**2 + 0.03304*x + 40.69  # 1200m
        equation = sp.Eq(td, tr) # Acha a equação de 'Td - Tr = 0'
        solutions = sp.solveset(equation) # sp.solveset() = devolve os valores de 'x' nas raízes da equação
        for i in solutions:
            vt.append([i,td.subs(x,i)]) # Guarda os valores de V[i], Td[i] em 'vt'
        Vmin, Tmin = vt[0][0], vt[0][1] # Velocidade mínima 'Vmín' da aeronave pelo gráfico de tração
        Vmax, Tmax = vt[1][0], vt[1][1] # Velocidade máxima 'Vmáx' da aeronave pelo gráfico de tração
        Vcmin = 2.4*m.sqrt(self.W/self.Sw) # Mínima velocidade permitida pela norma JAR-VLA 335 para o cruzeiro
        Vcmax = 0.9*Vmax # Máxima velocidade permitida pela norma JAR-VLA 335 para o cruzeiro
        #tcr_safe = Scr/Vcmin # Tempo máximo de voo em voo reto e nivelado (margem de segurança para Vcmin)
        tcr_max_alcance = Scr/desempenho.vel_max_alcance(self) # Tempo de cruzeiro para máximo alcance
        tcr_max_autonomia = Scr/desempenho.vel_max_autonomia(self) # Tempo de cruzeiro para máxima autonomia
        return Vmin, Vmax, Vcmin, Vcmax, tcr_max_alcance, tcr_max_autonomia

    def pouso(self):
        D_Vland = 0.5*self.rho*((desempenho.vel_landing(self))**2)*self.Sw*desempenho.Cd_ideal(self)
        L_Vland = 0.5*self.rho*((desempenho.vel_landing(self))**2)*self.Sw*desempenho.Cl_ideal(self)
        Sland_FAR = (1.69*(self.W)**2)/(self.g*self.rho*self.Sw*self.Clmax*(D_Vland+self.mu*((self.W)-L_Vland)))
        D_Vstall = 0.5*self.rho*((desempenho.vel_estol(self)/m.sqrt(2))**2)*self.Sw*desempenho.Cd_ideal(self)
        L_Vstall = 0.5*self.rho*((desempenho.vel_estol(self)/m.sqrt(2))**2)*self.Sw*desempenho.Cl_ideal(self)
        Sland_real = ((self.W)**2)/(self.g*self.rho*self.Sw*self.Clmax*(D_Vstall+self.mu*((self.W)-L_Vstall)))
        ang_planeio = m.atan(1/desempenho.ponto_projeto(self))*(180/m.pi) # Calcula o ângulo de planeio para (L/D)max em graus - que provê a máxima distância de planeio
        vel_planeio = m.sqrt((2*self.W*m.cos(ang_planeio*m.pi/180))/(self.rho*self.Sw*desempenho.Cl_ideal(self))) # Distância máxima de planeio
        return Sland_FAR, Sland_real, ang_planeio, vel_planeio

    #def envelope_de_voo():

    def mtow_obstaculo(self): # Mtow máximo para uma decolagem em 'x' metros com obstáculo
        rho = 1
        hob, Sc = 0.70 + 0.15, 0 # Altura do obstáculo + margem de segurança, Distância ao obstáculo
        carga = []
        data = {
            'Distância_total':[],
            'Peso':[],
            'Densidade':[],
            'Ângulo_subida':[],
            'Altura_transição':[],
            'S_groll':[],
            'S_rotation':[],
            'S_transition':[],
            'S_climb':[],
            'S_total':[],
        }
        while rho <= 3:
            mtow = 7.0 # Mtow inicial
            if rho == 1: rho = 1.165 # Troca o valor de rho = 1 para rho = 1.165 kg/m³
            elif rho == 2: rho = 1.081 # Troca o valor de rho = 2 para rho = 1.081 kg/m³
            elif rho == 3: rho = 0.998 # Troca o valor de rho = 3 para rho = 0.998 kg/m³
            while mtow <= 20:
                Stotal, ang_real = 0, 0 # Distância total de decolagem percorrida, Ângulo de subida real para 'VTR' em radianos
                W = mtow*self.g
                # Determinação da corrida em solo (SG) #
                T_Vlof = curvas.tracao(self, 1.1*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax)))/m.sqrt(2), rho) # Tração na velocidade de "Vlof/sqrt(2)"
                D_Vlof = 0.5*rho*((1.1*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax)))/m.sqrt(2))**2)*self.Sw*desempenho.Cd_ideal(self) # Arrasto na velocidade de "Vlof/sqrt(2)"
                L_Vlof = 0.5*rho*((1.1*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax)))/m.sqrt(2))**2)*self.Sw*desempenho.Cl_ideal(self) # Lift na velocidade de "Vlof/sqrt(2)"
                ac_SG = (self.g/W)*(T_Vlof-D_Vlof-self.mu*((W)-L_Vlof)) # Aceleração média durante a corrida no solo (ac_média_SG)
                Sg = ((1.1*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax))))**2)/(2*ac_SG) # Distância de Ground Roll (SG)
                # Determinação do segmento de rotação (SROT) #
                Srot = (1.1*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax)))) # A distância de rotação (SROT) é de aproximadamente o módulo da velocidade de rotação (VROT)
                # Determinação do momento de transição (STR) #
                r = (1.15*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax))))**2/(self.g*0.1903) # Raio de subida (R) durante a transição [17-30] (Gudmundsson, 2014)
                T_tr = curvas.tracao(self, 1.15*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax))), rho) # Tração no durante a transição
                Cl_tr = 2*W/(rho*(1.15*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax))))**2*self.Sw)
                Cd_tr = self.Cdmin + desempenho.efeito_solo(self)*self.K*(Cl_tr)**2 # Coef. de arrasto durante a transição
                D_tr = 0.5*rho*((1.15*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax))))**2)*self.Sw*Cd_tr # Arrasto durante a transição
                sin_climb = m.sin((T_tr-D_tr)/(W)) # Seno do ângulo de subida "θ_climb"
                theta_climb = m.asin(sin_climb) # Ângulo de subida "θ_climb" em radianos
                Str = r*sin_climb # Distância de transição (STR)
                # Avaliação da superação do obstáculo #
                Stotal = Sg + Srot + Str # Distância total percorrida até o alinhamento da aeronave com o ângulo de subida
                htr = r*(1-m.cos(theta_climb)) # Altura de transição (hTR)
                #print(Stotal, htr)
                if Stotal < 55:
                    #ang_real = m.asin(curvas.razao_subida(self, (1.1*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax)))), rho, W)/(1.1*(m.sqrt((2*W)/(rho*self.Sw*self.Clmax))))) # Calcula o ângulo de subida real para 'VTR' em radianos
                    if htr < hob:
                        Sc = (hob-htr)/m.tan(theta_climb) # Distância do ponto em que terminou a transição "Str" até o ponto que alcança o obstáculo
                        Stotal += Sc # Aumenta a distância total na distância percorrida, desde o fim de "Str" até alcançar o obstáculo
                        #print(m.degrees(theta_climb), m.degrees(ang_real))
                        if Stotal < 55: # Avalia se o ângulo necessário para ultrapassar o obstáculo "θ_climb" é menor que o fornecido pela razão de subida
                            carga.append([Stotal, W, rho, m.degrees(theta_climb), htr, Sg, Srot, Str, Sc, Stotal])
                    else:
                        Sc = 55 - Stotal
                        carga.append([Stotal, W, rho, m.degrees(theta_climb), htr, Sg, Srot, Str, Sc, Stotal])
                elif Stotal >= 55:
                    if htr >= hob: # Avalia se a aeronave vai ter uma altura maior que o obstáculo quando estiver no fim da transição (STR)
                        carga.append([Stotal, W, rho, m.degrees(theta_climb), htr, Sg, Srot, Str, Sc, Stotal])
                mtow += 0.1
                #print(mtow) # Usado para testar se não estaria preso em loop infinito (Não descomentar!)
            if rho == 1.165: rho = 2
            elif rho == 1.081: rho = 3
            else: break
        data['Distância_total'] = [i[0] for i in carga]
        data['Peso'] = [i[1] for i in carga]
        data['Densidade'] = [i[2] for i in carga]
        data['Ângulo_subida'] = [i[3] for i in carga]
        data['Altura_transição'] = [i[4] for i in carga]
        data['S_groll'] = [i[5] for i in carga]
        data['S_rotation'] = [i[6] for i in carga]
        data['S_transition'] = [i[7] for i in carga]
        data['S_climb'] = [i[8] for i in carga]
        data['S_total'] = [i[9] for i in carga]
        dataFrame = pd.DataFrame(data = data)
        print(dataFrame)
        # Coloque na linha abaixo o endereço do diretório que você deseja salvar os dados de análise do MTOW
        #dataFrame.to_excel(r'C:\Users\italo\OneDrive\Desktop\Códigos Python, MATLAB, Arduino e VHDL\Códigos Python\Projetos de Desempenho\resultados\dados'+'.xlsx', index=False)
        mtowF = [i[1]/self.g for i in carga if i[2] == 1.165] # Retorna o valor máximo do Mtow em 0m
        mtowF = float(mtowF[-1])
        mtowS = [i[1]/self.g for i in carga if i[2] == 1.081] # Retorna o valor máximo do Mtow em 600m
        mtowS = float(mtowS[-1])
        mtowI = [i[1]/self.g for i in carga if i[2] == 0.998] # Retorna o valor máximo do Mtow em 1200m
        mtowI = float(mtowI[-1])
        if self.p == 1.225:
            return mtowF
        elif self.p == 1.156:
            return mtowS
        elif self.p == 1.090:
            return mtowI