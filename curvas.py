# Classe das curvas de gráficos do código de integração de Desempenho - 2023
# pylint: disable=E1101

import numpy as np
import math as m
import matplotlib.pyplot as plt

x_14x7 = np.array([0.00,1.16,2.28,3.44,4.56,5.72,6.88,8.00,9.16,10.28,11.44,12.61,13.72,14.89,16.05,17.17,18.33,19.45,20.61,21.77,22.89,24.05,25.17,26.33,27.49,28.61,29.77,30.89,32.05,33.21])
y_14x7 = np.array([32.868,32.525,32.112,31.627,31.080,30.470,29.803,29.069,28.268,27.405,26.476,25.479,24.421,23.295,22.108,20.858,19.559,18.233,16.877,15.484,14.070,12.615,11.138,9.630,8.091,6.521,4.924,3.301,1.655,-0.009])
yS_14x7 = np.array([30.498,30.180,29.796,29.346,28.839,28.273,27.654,26.973,26.230,25.429,24.567,23.642,22.660,21.616,20.514,19.354,18.149,16.919,15.660,14.368,13.055,11.706,10.335,8.936,7.508,6.051,4.569,3.063,1.535,-0.008])
yI_14x7 = np.array([28.156,27.863,27.509,27.093,26.625,26.102,25.531,24.902,24.216,23.477,22.681,21.827,20.920,19.956,18.939,17.868,16.755,15.620,14.457,13.265,12.053,10.807,9.542,8.250,6.931,5.586,4.218,2.827,1.418,-0.008])
x_15x7 = np.array([0.00,1.16,2.32,3.49,4.65,5.81,6.97,8.14,9.30,10.42,11.58,12.74,13.90,15.06,16.23,17.39,18.55,19.71,20.88,22.04,23.20,24.36,25.53,26.69,27.85,29.01,30.13,31.29,32.45,33.62])
y_15x7 = np.array([42.543,41.942,41.262,40.523,39.718,38.842,37.890,36.867,35.773,34.603,33.362,32.045,30.657,29.198,27.677,26.089,24.461,22.802,21.107,19.363,17.579,15.720,13.905,12.010,10.075,8.114,6.121,4.057,2.068,0.000])
yS_15x7 = np.array([39.475,38.918,38.287,37.601,36.854,36.041,35.158,34.209,33.193,32.108,30.956,29.734,28.447,27.093,25.681,24.208,22.697,21.158,19.585,17.967,16.312,14.587,12.903,11.144,9.349,7.529,5.679,3.764,1.919,0.000])
yI_15x7 = np.array([36.444,35.930,35.347,34.714,34.025,33.274,32.459,31.582,30.645,29.642,28.579,27.451,26.263,25.013,23.709,22.349,20.954,19.533,18.081,16.587,15.059,13.467,11.912,10.289,8.631,6.950,5.243,3.475,1.772,0.000])
x_15x10 = np.array([0.00,1.52,3.08,4.60,6.12,7.69,9.21,10.77,12.29,13.81,15.38,16.90,18.42,19.98,21.50,23.07,24.59,26.11,27.67,29.19,30.71,32.28,33.80,35.32,36.88,38.40,39.96,41.48,43.00,44.57])
y_15x10 = np.array([46.751,46.729,46.684,46.604,46.493,46.337,46.128,45.803,45.270,44.398,43.223,41.844,40.314,38.615,36.760,34.767,32.637,30.386,28.104,25.786,23.420,21.000,18.536,16.022,13.478,10.867,8.216,5.511,2.771,0.000])
yS_15x10 = np.array([43.380,43.359,43.318,43.244,43.141,42.996,42.802,42.501,42.005,41.196,40.107,38.827,37.407,35.831,34.110,32.260,30.283,28.195,26.077,23.927,21.731,19.486,17.199,14.867,12.506,10.083,7.623,5.114,2.571,0.000])
yI_15x10 = np.array([40.049,40.030,39.992,39.923,39.828,39.695,39.516,39.238,38.780,38.033,37.027,35.846,34.535,33.080,31.491,29.783,27.958,26.030,24.075,22.090,20.063,17.990,15.879,13.726,11.546,9.309,7.038,4.721,2.374,0.000])
x_16x8 = np.array([0.00,1.30,2.59,3.89,5.19,6.48,7.78,9.07,10.37,11.67,13.01,14.30,15.60,16.90,18.19,19.49,20.79,22.08,23.38,24.68,25.97,27.27,28.57,29.86,31.16,32.45,33.75,35.05,36.34,37.64])
y_16x8 = np.array([57.671,57.128,56.390,55.474,54.420,53.267,52.009,50.634,49.157,47.578,45.888,44.091,42.191,40.190,38.099,35.919,33.664,31.378,29.038,26.649,24.203,21.716,19.172,16.596,13.950,11.254,8.492,5.703,2.860,0.000])
yS_16x8 = np.array([53.513,53.009,52.324,51.474,50.496,49.427,48.259,46.983,45.613,44.148,42.579,40.912,39.149,37.292,35.352,33.329,31.237,29.115,26.944,24.728,22.458,20.150,17.789,15.400,12.944,10.443,7.879,5.291,2.654,0.000])
yI_16x8 = np.array([49.404,48.939,48.307,47.522,46.619,45.632,44.553,43.376,42.111,40.758,39.310,37.770,36.143,34.429,32.638,30.770,28.838,26.880,24.875,22.829,20.733,18.603,16.424,14.217,11.950,9.641,7.274,4.885,2.450,0.000])

class curvas:

    def tracao(self, V, **kwargs):
        n = 2  # Número de grau do polinômio

        if 'prop' in kwargs:
            if kwargs['prop'] == '14x7':
                z_14x7 = np.polyfit(x_14x7,y_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
                zS_14x7 = np.polyfit(x_14x7,yS_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
                zI_14x7 = np.polyfit(x_14x7,yI_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

                p_14x7 = np.poly1d(z_14x7) # Função ajustada para rho = 1.225kg/m³
                pS_14x7 = np.poly1d(zS_14x7) # Função ajustada para rho = 1.156kg/m³
                pI_14x7 = np.poly1d(zI_14x7) # Função ajustada para rho = 1.090kg/m³

                if 'rho' in kwargs:
                    if kwargs['rho'] == 1.165:
                        return p_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif kwargs['rho'] == 1.081:
                        return pS_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif kwargs['rho'] == 0.998:
                        return pI_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                else:
                    if self.rho == 1.165:
                        return p_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.225kg/m³
                    elif self.rho == 1.081:
                        return pS_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.156kg/m³
                    elif self.rho == 0.998:
                        return pI_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.090kg/m³
                    
            elif kwargs['prop'] == '15x7':
                z_15x7 = np.polyfit(x_15x7,y_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
                zS_15x7 = np.polyfit(x_15x7,yS_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
                zI_15x7 = np.polyfit(x_15x7,yI_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

                p_15x7 = np.poly1d(z_15x7) # Função ajustada para rho = 1.225kg/m³
                pS_15x7 = np.poly1d(zS_15x7) # Função ajustada para rho = 1.156kg/m³
                pI_15x7 = np.poly1d(zI_15x7) # Função ajustada para rho = 1.090kg/m³

                if 'rho' in kwargs:
                    if kwargs['prop'] == 1.165:
                        return p_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif kwargs['prop'] == 1.081:
                        return pS_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif kwargs['prop'] == 0.998:
                        return pI_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                else:
                    if self.rho == 1.165:
                        return p_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.225kg/m³
                    elif self.rho == 1.081:
                        return pS_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.156kg/m³
                    elif self.rho == 0.998:
                        return pI_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.090kg/m³

            elif kwargs['prop'] == '15x10':
                z_15x10 = np.polyfit(x_15x10,y_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
                zS_15x10 = np.polyfit(x_15x10,yS_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
                zI_15x10 = np.polyfit(x_15x10,yI_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

                p_15x10 = np.poly1d(z_15x10) # Função ajustada para rho = 1.225kg/m³
                pS_15x10 = np.poly1d(zS_15x10) # Função ajustada para rho = 1.156kg/m³
                pI_15x10 = np.poly1d(zI_15x10) # Função ajustada para rho = 1.090kg/m³

                if 'rho' in kwargs:
                    if kwargs['rho'] == 1.165:
                        return p_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif kwargs['rho'] == 1.081:
                        return pS_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif kwargs['rho'] == 0.998:
                        return pI_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                else:
                    if self.rho == 1.165:
                        return p_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif self.rho == 1.081:
                        return pS_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif self.rho == 0.998:
                        return pI_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                    
            elif kwargs['prop'] == '16x8':
                z_16x8 = np.polyfit(x_16x8,y_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
                zS_16x8 = np.polyfit(x_16x8,yS_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
                zI_16x8 = np.polyfit(x_16x8,yI_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

                p_16x8 = np.poly1d(z_16x8) # Função ajustada para rho = 1.225kg/m³
                pS_16x8 = np.poly1d(zS_16x8) # Função ajustada para rho = 1.156kg/m³
                pI_16x8 = np.poly1d(zI_16x8) # Função ajustada para rho = 1.090kg/m³

                if 'rho' in kwargs:
                    if kwargs['rho'] == 1.165:
                        return p_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif kwargs['rho'] == 1.081:
                        return pS_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif kwargs['rho'] == 0.998:
                        return pI_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                else:
                    if self.rho == 1.165:
                        return p_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif self.rho == 1.081:
                        return pS_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif self.rho == 0.998:
                        return pI_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³

        else:
            if self.prop == '14x7':
                z_14x7 = np.polyfit(x_14x7,y_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
                zS_14x7 = np.polyfit(x_14x7,yS_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
                zI_14x7 = np.polyfit(x_14x7,yI_14x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

                p_14x7 = np.poly1d(z_14x7) # Função ajustada para rho = 1.225kg/m³
                pS_14x7 = np.poly1d(zS_14x7) # Função ajustada para rho = 1.156kg/m³
                pI_14x7 = np.poly1d(zI_14x7) # Função ajustada para rho = 1.090kg/m³
                
                if 'rho' in kwargs:
                    if kwargs['rho'] == 1.165:
                        return p_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif kwargs['rho'] == 1.081:
                        return pS_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif kwargs['rho'] == 0.998:
                        return pI_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                else:
                    if self.rho == 1.165:
                        return p_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.225kg/m³
                    elif self.rho == 1.081:
                        return pS_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.156kg/m³
                    elif self.rho == 0.998:
                        return pI_14x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.090kg/m³

            if self.prop == '15x7':
                z_15x7 = np.polyfit(x_15x7,y_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
                zS_15x7 = np.polyfit(x_15x7,yS_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
                zI_15x7 = np.polyfit(x_15x7,yI_15x7,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

                p_15x7 = np.poly1d(z_15x7) # Função ajustada para rho = 1.225kg/m³
                pS_15x7 = np.poly1d(zS_15x7) # Função ajustada para rho = 1.156kg/m³
                pI_15x7 = np.poly1d(zI_15x7) # Função ajustada para rho = 1.090kg/m³

                if 'rho' in kwargs:
                    if kwargs['rho'] == 1.165:
                        return p_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif kwargs['rho'] == 1.081:
                        return pS_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif kwargs['rho'] == 0.998:
                        return pI_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                else:
                    if self.rho == 1.165:
                        return p_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.225kg/m³
                    elif self.rho == 1.081:
                        return pS_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.156kg/m³
                    elif self.rho == 0.998:
                        return pI_15x7(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para self.rho = 1.090kg/m³

            if self.prop == '15x10':
                z_15x10 = np.polyfit(x_15x10,y_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
                zS_15x10 = np.polyfit(x_15x10,yS_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
                zI_15x10 = np.polyfit(x_15x10,yI_15x10,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

                p_15x10 = np.poly1d(z_15x10) # Função ajustada para rho = 1.225kg/m³
                pS_15x10 = np.poly1d(zS_15x10) # Função ajustada para rho = 1.156kg/m³
                pI_15x10 = np.poly1d(zI_15x10) # Função ajustada para rho = 1.090kg/m³

                if 'rho' in kwargs:
                    if kwargs['rho'] == 1.165:
                        return p_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif kwargs['rho'] == 1.081:
                        return pS_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif kwargs['rho'] == 0.998:
                        return pI_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                else:
                    if self.rho == 1.165:
                        return p_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif self.rho == 1.081:
                        return pS_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif self.rho == 0.998:
                        return pI_15x10(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³

            if self.prop == '16x8':
                z_16x8 = np.polyfit(x_16x8,y_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.225kg/m³
                zS_16x8 = np.polyfit(x_16x8,yS_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.156kg/m³
                zI_16x8 = np.polyfit(x_16x8,yI_16x8,n) # Encontra os coeficientes da equação de grau 'n' para rho = 1.090kg/m³

                p_16x8 = np.poly1d(z_16x8) # Função ajustada para rho = 1.225kg/m³
                pS_16x8 = np.poly1d(zS_16x8) # Função ajustada para rho = 1.156kg/m³
                pI_16x8 = np.poly1d(zI_16x8) # Função ajustada para rho = 1.090kg/m³

                if 'rho' in kwargs:
                    if kwargs['rho'] == 1.165:
                        return p_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif kwargs['rho'] == 1.081:
                        return pS_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif kwargs['rho'] == 0.998:
                        return pI_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³
                else:
                    if self.rho == 1.165:
                        return p_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.225kg/m³
                    elif self.rho == 1.081:
                        return pS_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.156kg/m³
                    elif self.rho == 0.998:
                        return pI_16x8(V) # Retorna a Tração disponível para a velocidade 'V' passada como parâmetro, para rho = 1.090kg/m³

    def tracao_requerida(self, V, **kwargs):
        if 'rho' and 'W' in kwargs:
            Cl = (2*kwargs['W'])/(kwargs['rho']*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            return kwargs['W']/(Cl/Cd)
        elif 'rho' in kwargs:
            Cl = (2*self.W)/(kwargs['rho']*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            return self.W/(Cl/Cd)
        else:
            Cl = (2*self.W)/(self.rho*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            return self.W/(Cl/Cd)

    def potencia_requerida(self, V, **kwargs):
        if 'rho' and 'W' in kwargs:
            return curvas.tracao_requerida(self, V, rho=kwargs['rho'], W=kwargs['W'])*V
        elif 'rho' in kwargs:
            return curvas.tracao_requerida(self, V, rho=kwargs['rho'])*V
        else:
            return curvas.tracao_requerida(self, V)*V

    def potencia(self, V, **kwargs):
        if 'rho' in kwargs:
            return curvas.tracao(self, V, rho=kwargs['rho'])*V
        else:
            return curvas.tracao(self, V)*V

    def razao_subida(self, V, **kwargs): # Rate of Climb
        if 'rho' and 'W' in kwargs:
            RoC = (curvas.potencia(self, V, rho=kwargs['rho'])-curvas.potencia_requerida(self, V, rho=kwargs['rho'], W=kwargs['W']))/kwargs['W']
        elif 'rho' in kwargs:
            RoC = (curvas.potencia(self, V, rho=kwargs['rho'])-curvas.potencia_requerida(self, V, rho=kwargs['rho']))/self.W
        else:
            RoC = (curvas.potencia(self, V)-curvas.potencia_requerida(self, V))/self.W
        if RoC < 0: return float(0)
        else: return RoC

    def razao_descida(self, V, **kwargs): # Rate of Descent ou Sink Rate
        if 'rho' and 'W' in kwargs:
            Cl = (2*kwargs['W'])/(kwargs['rho']*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            RoD = (-Cd*m.sqrt((2*kwargs['W'])/(Cl**3*kwargs['rho']*self.Sw)))
        elif 'rho' in kwargs:
            Cl = (2*self.W)/(kwargs['rho']*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            RoD = (-Cd*m.sqrt((2*self.W)/(Cl**3*kwargs['rho']*self.Sw)))
        else:
            Cl = (2*self.W)/(self.rho*V**2*self.Sw)
            Cd = self.Cdmin + self.K*Cl**2
            RoD = (-Cd*m.sqrt((2*self.W)/(Cl**3*self.rho*self.Sw)))
        if RoD > 0: return float(0)
        else: return RoD

    def curva_ROC(self): # Curvas de razão de subida para diversas altitude-densidades
        matriz_RoC = []
        rho = 0
        while rho < 3:
            v = 1
            if rho == 0: rho = 1.165
            elif rho == 1: rho = 1.081
            elif rho == 2: rho = 0.998
            while v <= 40:
                RoC = (curvas.potencia(self, v, rho=rho)-curvas.potencia_requerida(self, v, rho=rho))/self.W
                if RoC >= 0: matriz_RoC.append([RoC, v, rho])
                v += 0.01
            if rho == 1.165: rho = 1
            elif rho == 1.081: rho = 2
            else: break
        xF = [i[1] for i in matriz_RoC if i[2] == 1.165]
        xS = [i[1] for i in matriz_RoC if i[2] == 1.081]
        xI = [i[1] for i in matriz_RoC if i[2] == 0.998]
        yF = [i[0] for i in matriz_RoC if i[2] == 1.165]
        yS = [i[0] for i in matriz_RoC if i[2] == 1.081]
        yI = [i[0] for i in matriz_RoC if i[2] == 0.998]
        plt.plot(xF, yF, ls='solid', lw='1', color='g', label='RoC em 0m')
        plt.plot(xS, yS, ls='solid', lw='1', color='b', label='RoC em 600m')
        plt.plot(xI, yI, ls='solid', lw='1', color='r', label='RoC em 1200m')
        plt.title('Razão de subida em função da velocidade')
        plt.xlabel('V ($m/s$)', fontsize=10)
        plt.ylabel('RoC ($m/s$)', fontsize=10)
        #plt.xlim(7, 30)
        #plt.ylim(0, 2)
        plt.legend()
        plt.axis('auto')
        plt.show()
        pass

    def curva_ROD(self):
        matriz_RoD = []
        aux = 0
        while aux < 3:
            v = 1
            if aux == 0: rho = 1.165
            elif aux == 1: rho = 1.081
            elif aux == 2: rho = 0.998
            while v <= 40:
                Cl = (2*self.W)/(self.rho*v**2*self.Sw)
                Cd = self.Cdmin + self.K*Cl**2
                Vv = -Cd*m.sqrt((2*self.W)/(Cl**3*rho*self.Sw))
                if v >= 7.85: matriz_RoD.append([Vv, v, rho])
                v += 0.01
            aux += 1
        xF = [i[1] for i in matriz_RoD if i[2] == 1.165]
        xS = [i[1] for i in matriz_RoD if i[2] == 1.081]
        xI = [i[1] for i in matriz_RoD if i[2] == 0.998]
        yF = [i[0] for i in matriz_RoD if i[2] == 1.165]
        yS = [i[0] for i in matriz_RoD if i[2] == 1.081]
        yI = [i[0] for i in matriz_RoD if i[2] == 0.998]
        plt.plot(xF, yF, ls='solid', lw='1', color='g', label='RoD em 0m')
        plt.plot(xS, yS, ls='solid', lw='1', color='b', label='RoD em 600m')
        plt.plot(xI, yI, ls='solid', lw='1', color='r', label='RoD em 1200m')
        plt.title('Razão de descida em função da velocidade')
        plt.xlabel('V ($m/s$)', fontsize=10)
        plt.ylabel('RoD ($m/s$)', fontsize=10)
        plt.legend()
        plt.axis('auto')
        plt.show()
        pass

    def curva_TDxV(self): # Curvas de trações de várias hélices listadas
        aux = 0 # Variável auxiliar que percorrerá a lista de hélices para o cálculo de tração
        prop = '-' # Inicializa a variável que receberá o tipo de hélice como uma string
        Td = [] # Lista que guardará os valores de: tração disponível, velocidade e tipo de hélice
        while aux <= 3:
            v = 1 # velocidade inicial
            if aux == 0: prop = '14x7'
            elif aux == 1: prop = '15x7'
            elif aux == 2: prop = '15x10'
            elif aux == 3: prop = '16x8'
            while v <= 32: # velocidade final (máxima)
                if prop == '14x7': Td.append([curvas.tracao(self, v, prop=prop), v, prop])
                elif prop == '15x7': Td.append([curvas.tracao(self, v, prop=prop), v, prop])
                elif prop == '15x10': Td.append([curvas.tracao(self, v, prop=prop), v, prop])
                elif prop == '16x8': Td.append([curvas.tracao(self, v, prop=prop), v, prop])
                v += 0.01
            aux += 1
        x = [i[1] for i in Td if i[2] == '14x7']
        yt_14x7 = [i[0] for i in Td if i[2] == '14x7'] # Guarda os valores de tração disponível da hélice 14x7E
        yt_15x7 = [i[0] for i in Td if i[2] == '15x7'] # Guarda os valores de tração disponível da hélice 15x7E
        yt_15x10 = [i[0] for i in Td if i[2] == '15x10'] # Guarda os valores de tração disponível da hélice 15x10E
        yt_16x8 = [i[0] for i in Td if i[2] == '16x8'] # Guarda os valores de tração disponível da hélice 16x8E
        plt.plot(x, yt_14x7, ls='solid', lw='1', color='c', label='$T_{14x7}$   em 1200m')
        plt.plot(x, yt_15x7, ls='solid', lw='1', color='r', label='$T_{15x7}$   em 1200m')
        plt.plot(x, yt_15x10, ls='solid', lw='1', color='y', label='$T_{15x10}$ em 1200m')
        plt.plot(x, yt_16x8, ls='solid', lw='1', color='m', label='$T_{16x8}$   em 1200m')
        plt.title('Comparação entre as Trações por hélice')
        plt.xlabel('V ($m/s$)', fontsize=10)
        plt.ylabel('$T$ ($N$)', fontsize=10)
        plt.legend()
        plt.show()
        pass

    def curva_TD(self, prop): # Curva de tração para uma hélice específica
        aux = 0
        Td = []
        while aux < 3:
            v = 0.01
            if aux == 0: rho = 1.165
            elif aux == 1: rho = 1.081
            elif aux == 2: rho = 0.998
            while v <= 40:
                if prop == '14x7': Td.append([curvas.tracao(self, v, rho=rho, prop=prop), v, rho])
                elif prop == '15x7': Td.append([curvas.tracao(self, v, rho=rho, prop=prop), v, rho])
                elif prop == '15x10': Td.append([curvas.tracao(self, v, rho=rho, prop=prop), v, rho])
                elif prop == '16x8': Td.append([curvas.tracao(self, v, rho=rho, prop=prop), v, rho])
                v += 0.01
            aux += 1
        xF = [i[1] for i in Td if i[2] == 1.165 and i[0] >= 0]
        xS = [i[1] for i in Td if i[2] == 1.081 and i[0] >= 0]
        xI = [i[1] for i in Td if i[2] == 0.998 and i[0] >= 0]
        yF = [i[0] for i in Td if i[2] == 1.165 and i[0] >= 0]
        yS = [i[0] for i in Td if i[2] == 1.081 and i[0] >= 0]
        yI = [i[0] for i in Td if i[2] == 0.998 and i[0] >= 0]
        plt.plot(xF, yF, ls='solid', lw='1', color='g', label='Tração em 0m')
        plt.plot(xS, yS, ls='solid', lw='1', color='b', label='Tração em 600m')
        plt.plot(xI, yI, ls='solid', lw='1', color='r', label='Tração em 1200m')
        plt.title(f'Tração em função da velocidade - {prop}')
        plt.xlabel('V ($m/s$)', fontsize=10)
        plt.ylabel('$T_d$ ($N$)', fontsize=10)
        plt.legend()
        plt.show()
        pass

    def curva_TRxTD(self): # Curvas de trações disponível (hélice escolhida) e requerida em diversas altitude-densidades
        n = 2 # Número de grau do polinômio
        rho = 0 # parâmetro de densidade que auxiliará a percorrer a lista
        Tracao = [] # lista vazia para receber os valores de Td, Tr, v e rho
        while rho < 3:
            v = 1 # velocidade inicial
            if self.rho == 1.165: vmin = 8.5 # velocidade inicial ajustada para análise em 0m
            elif self.rho == 1.081: vmin = 8 # velocidade inicial ajustada para análise em 600m
            elif self.rho == 0.998: vmin = 7 # velocidade inicial ajustada para análise em 1200m
            if rho == 0: rho = 1.165
            elif rho == 1: rho = 1.081
            elif rho == 2: rho = 0.998
            while v < 40:
                Cl = (2*self.W)/(rho*v**2*self.Sw)
                Cd = self.Cdmin + self.K*Cl**2
                Tracao.append([curvas.tracao(self, v, rho=rho), self.W/(Cl/Cd), v, rho])
                v += 0.01
            if rho == 1.165: rho = 1
            elif rho == 1.081: rho = 2
            else: break
        x = [i[2] for i in Tracao if i[3] == 1.165 and i[2] >= vmin]
        ydF = [i[0] for i in Tracao if i[3] == 1.165 and i[2] >= vmin]
        ydS = [i[0] for i in Tracao if i[3] == 1.081 and i[2] >= vmin]
        ydI = [i[0] for i in Tracao if i[3] == 0.998 and i[2] >= vmin]
        yrF = [i[1] for i in Tracao if i[3] == 1.165 and i[2] >= vmin]
        yrS = [i[1] for i in Tracao if i[3] == 1.081 and i[2] >= vmin]
        yrI = [i[1] for i in Tracao if i[3] == 0.998 and i[2] >= vmin]
        plt.plot(x, yrF, ls='solid', lw='1', color='c', label='$T_R$ em 0m')
        plt.plot(x, yrS, ls='solid', lw='1', color='y', label='$T_R$ em 600m')
        plt.plot(x, yrI, ls='solid', lw='1', color='m', label='$T_R$ em 1200m')
        plt.plot(x, ydF, ls='solid', lw='1', color='g', label='$T_D$ em 0m')
        plt.plot(x, ydS, ls='solid', lw='1', color='b', label='$T_D$ em 600m')
        plt.plot(x, ydI, ls='solid', lw='1', color='r', label='$T_D$ em 1200m')
        plt.title('Tração em função da velocidade')
        plt.xlabel('V ($m/s$)', fontsize=10)
        plt.ylabel('$T$ ($N$)', fontsize=10)
        plt.legend()
        plt.show()
        x = [i[2] for i in Tracao if i[3] == 1.165]
        ydF = [i[0] for i in Tracao if i[3] == 1.165]
        ydS = [i[0] for i in Tracao if i[3] == 1.081]
        ydI = [i[0] for i in Tracao if i[3] == 0.998]
        yrF = [i[1] for i in Tracao if i[3] == 1.165]
        yrS = [i[1] for i in Tracao if i[3] == 1.081]
        yrI = [i[1] for i in Tracao if i[3] == 0.998]
        if self.rho == 1.165:
            p = np.poly1d(np.polyfit(x,yrF,n)) # Função que expressa a tração requerida na análise acima para 0m
            q = np.poly1d(np.polyfit(x,ydF,n)) # Função que expressa a tração disponível na análise acima para 0m
            print(p) # mostra o resultado da função TrF(v)
            print(q) # mostra o resultado da função TdF(v)
        elif self.rho == 1.081:
            p = np.poly1d(np.polyfit(x,yrS,n)) # Função que expressa a tração requerida na análise acima para 600m
            q = np.poly1d(np.polyfit(x,ydF,n)) # Função que expressa a tração disponível na análise acima para 600m
            print(p) # mostra o resultado da função TrSP(v)
            print(q) # mostra o resultado da função TdF(v)
        elif self.rho == 0.998:
            p = np.poly1d(np.polyfit(x,yrI,n)) # Função que expressa a tração requerida na análise acima para 1200m
            q = np.poly1d(np.polyfit(x,ydF,n)) # Função que expressa a tração disponível na análise acima para 1200m
            print(p) # mostra o resultado da função TrSJC(v)
            print(q) # mostra o resultado da função TdF(v)
        pass

    def curva_PRxPD(self): # Curvas de potências disponível (hélice escolhida) e requerida em diversas altitude-densidades
        n = 2 # Número de grau do polinômio
        rho = 0 # parâmetro de densidade que auxiliará a percorrer a lista
        Potencia = [] # lista vazia para receber os valores de Pd, Pr, v e rho
        while rho < 3:
            v = 1 # velocidade inicial
            if self.rho == 1.165: vmin = 8.5 # velocidade inicial ajustada para análise em 0m
            elif self.rho == 1.081: vmin = 8 # velocidade inicial ajustada para análise em 600m
            elif self.rho == 0.998: vmin = 7 # velocidade inicial ajustada para análise em 1200m
            if rho == 0: rho = 1.165
            elif rho == 1: rho = 1.081
            elif rho == 2: rho = 0.998
            while v < 40:
                Cl = (2*self.W)/(rho*v**2*self.Sw)
                Cd = self.Cdmin + self.K*Cl**2
                Potencia.append([curvas.tracao(self, v, rho=rho)*v, (self.W/(Cl/Cd))*v, v, rho])
                v += 0.01
            if rho == 1.165: rho = 1
            elif rho == 1.081: rho = 2
            else: break
        x = [i[2] for i in Potencia if i[3] == 1.165 and i[2] >= vmin]
        ydF = [i[0] for i in Potencia if i[3] == 1.165 and i[2] >= vmin]
        ydS = [i[0] for i in Potencia if i[3] == 1.081 and i[2] >= vmin]
        ydI = [i[0] for i in Potencia if i[3] == 0.998 and i[2] >= vmin]
        yrF = [i[1] for i in Potencia if i[3] == 1.165 and i[2] >= vmin]
        yrS = [i[1] for i in Potencia if i[3] == 1.081 and i[2] >= vmin]
        yrI = [i[1] for i in Potencia if i[3] == 0.998 and i[2] >= vmin]
        plt.plot(x, yrF, ls='solid', lw='1', color='c', label='$P_R$ em 0m')
        plt.plot(x, yrS, ls='solid', lw='1', color='y', label='$P_R$ em 600m')
        plt.plot(x, yrI, ls='solid', lw='1', color='m', label='$P_R$ em 1200m')
        plt.plot(x, ydF, ls='solid', lw='1', color='g', label='$P_D$ em 0m')
        plt.plot(x, ydS, ls='solid', lw='1', color='b', label='$P_D$ em 600m')
        plt.plot(x, ydI, ls='solid', lw='1', color='r', label='$P_D$ em 1200m')
        plt.title('Potência em função da velocidade - 15x10E')
        plt.xlabel('V ($m/s$)', fontsize=10)
        plt.ylabel('$P$ ($W$)', fontsize=10)
        plt.legend()
        plt.show()
        x = [i[2] for i in Potencia if i[3] == 1.165]
        ydF = [i[0] for i in Potencia if i[3] == 1.165]
        ydS = [i[0] for i in Potencia if i[3] == 1.081]
        ydI = [i[0] for i in Potencia if i[3] == 0.998]
        yrF = [i[1] for i in Potencia if i[3] == 1.165]
        yrS = [i[1] for i in Potencia if i[3] == 1.081]
        yrI = [i[1] for i in Potencia if i[3] == 0.998]
        if self.rho == 1.165:
            p = np.poly1d(np.polyfit(x,yrF,n)) # Função que expressa a potência requerida na análise acima para 0m
            q = np.poly1d(np.polyfit(x,ydF,n)) # Função que expressa a potência disponível na análise acima para 0m
            print(p) # mostra o resultado da função PrF(v)
            print(q) # mostra o resultado da função PdF(v)
        elif self.rho == 1.081:
            p = np.poly1d(np.polyfit(x,yrS,n)) # Função que expressa a potência requerida na análise acima para 600m
            q = np.poly1d(np.polyfit(x,ydF,n)) # Função que expressa a potência disponível na análise acima para 600m
            print(p) # mostra o resultado da função PrSP(v)
            print(q) # mostra o resultado da função PdF(v)
        elif self.rho == 0.998:
            p = np.poly1d(np.polyfit(x,yrI,n)) # Função que expressa a potência requerida na análise acima para 1200m
            q = np.poly1d(np.polyfit(x,ydF,n)) # Função que expressa a potência disponível na análise acima para 1200m
            print(p) # mostra o resultado da função PrSJC(v)
            print(q) # mostra o resultado da função PdF(v)
        pass

    def curva_decolagem(self): # Carga máxima (kg) por comprimento de pista (m) com obstáculo
        y = [self.Mtow for i in self.carga if i[1] == 1.165] # Define os valores de y para o mtow máximo
        xF = [i[8] for i in self.carga if i[1] == 1.165]
        xS = [i[8] for i in self.carga if i[1] == 1.081]
        xI = [i[8] for i in self.carga if i[1] == 0.998]
        yF = [i[0]/self.g for i in self.carga if i[1] == 1.165]
        yS = [i[0]/self.g for i in self.carga if i[1] == 1.081]
        yI = [i[0]/self.g for i in self.carga if i[1] == 0.998]
        plt.plot(xF, y, ls='solid', lw='1', color='k') # Traça uma linha horizontal na carga máxima suportada
        plt.text(35.7, self.Mtow + 0.1, f'Mtow: {round(self.Mtow, 0)}kg', color='black')
        plt.plot(xF, yF, ls='solid', lw='1', color='g', label='Mtow em 0m')
        plt.plot(xS, yS, ls='solid', lw='1', color='b', label='Mtow em 600m')
        plt.plot(xI, yI, ls='solid', lw='1', color='r', label='Mtow em 1200m')
        plt.title('Comprimento de pista em função do MTOW')
        plt.xlabel('Distância de decolagem ($m$)')
        plt.ylabel('Mtow (kg)')
        plt.legend()
        plt.show()
        pass

        