import sys
import math
import numpy as np
from scipy import special

# classe das gaussianas primitivas
class gaussiana_primitiva():
    def __init__(self, alfa, coeff, coordenadas, l1, l2, l3):
        self.alfa = alfa
        self.coeff = coeff
        self.coordenadas = np.array(coordenadas)
        self.A = ( 2.0 * alfa / math.pi) ** 0.75 # + alguns termos p/ l1, l2 e l3 > 0

# Matriz de Sobreposição (S)
def sobreposição(molécula):
    num_bases = len(molécula)
    S = np.zeros([num_bases, num_bases])    

    for i in range(num_bases):
        for j in range(num_bases):
            num_primitivas_i = len(molécula[i])
            num_primitivas_j = len(molécula[j])

            for k in range(num_primitivas_i):
                for l in range(num_primitivas_j):

                    N = molécula[i][k].A * molécula[j][l].A
                    p = molécula[i][k].alfa + molécula[j][l].alfa
                    q = molécula[i][k].alfa * molécula[j][l].alfa / p
                    Q = molécula[i][k].coordenadas - molécula[j][l].coordenadas
                    Q2 = np.dot(Q,Q)

                    S[i,j] += N * molécula[i][k].coeff * molécula[j][l].coeff * math.exp(-q * Q2) * (math.pi / p)**(3/2)
    return S

# Energia cinética (T)
def cinética(molécula):
    num_bases = len(molécula)
    T = np.zeros([num_bases, num_bases])    

    for i in range(num_bases):
        for j in range(num_bases):
            num_primitivas_i = len(molécula[i])
            num_primitivas_j = len(molécula[j])

            for k in range(num_primitivas_i):
                for l in range(num_primitivas_j):
                    
                    c1c2 = molécula[i][k].coeff * molécula[j][l].coeff

                    N = molécula[i][k].A * molécula[j][l].A
                    p = molécula[i][k].alfa + molécula[j][l].alfa
                    q = molécula[i][k].alfa * molécula[j][l].alfa / p
                    Q = molécula[i][k].coordenadas - molécula[j][l].coordenadas
                    Q2 = np.dot(Q,Q)

                    P = molécula[i][k].alfa * molécula[i][k].coordenadas + molécula[j][l].alfa * molécula[j][l].coordenadas
                    Pp = P/p
                    PG = Pp - molécula[j][l].coordenadas
                    PGx2 = PG[0] * PG[0]
                    PGy2 = PG[1] * PG[1]
                    PGz2 = PG[2] * PG[2]


                    s = N * c1c2 * math.exp(-q*Q2) * (math.pi/p)**(3/2)

                    T[i,j] += 3*molécula[j][l].alfa*s
                    T[i,j] -= 2*molécula[j][l].alfa*molécula[j][l].alfa*s * (PGx2 + 0.5/p)
                    T[i,j] -= 2*molécula[j][l].alfa*molécula[j][l].alfa*s * (PGy2 + 0.5/p)
                    T[i,j] -= 2*molécula[j][l].alfa*molécula[j][l].alfa*s * (PGz2 + 0.5/p)
    return T

# definição da função "boys" (caso especial para a função confluente hipergeométrica de Kummer)
def boys (x, n):
    if x == 0:
        return 1.0/(2*n+1)
    else:
        return special.gammainc(n+0.5,x) * special.gamma(n+0.5) * (1.0/(2*x**(n+0.5)))
# Energia cinética (T)
def atração_elétron_núcleo(molécula, coordenadas_atômicas, z):
    num_átomos = len(z)
    num_bases = len(molécula)
    V_ne = np.zeros([num_bases, num_bases])    

    for átomo in range(num_átomos):
        for i in range(num_bases):
            for j in range(num_bases):
                num_primitivas_i = len(molécula[i])
                num_primitivas_j = len(molécula[j])

                for k in range(num_primitivas_i):
                    for l in range(num_primitivas_j):
                        
                        c1c2 = molécula[i][k].coeff * molécula[j][l].coeff

                        N = molécula[i][k].A * molécula[j][l].A
                        p = molécula[i][k].alfa + molécula[j][l].alfa
                        q = molécula[i][k].alfa * molécula[j][l].alfa / p
                        Q = molécula[i][k].coordenadas - molécula[j][l].coordenadas
                        Q2 = np.dot(Q,Q)

                        P = molécula[i][k].alfa * molécula[i][k].coordenadas + molécula[j][l].alfa * molécula[j][l].coordenadas
                        Pp = P/p
                        PG = Pp - coordenadas_atômicas[átomo]
                        PG2 = np.dot(PG,PG)

                        V_ne[i,j] += -z[átomo] * N * c1c2 * math.exp(-q*Q2) * (2.0 * math.pi/p) * boys(p*PG2, 0)
    return V_ne




# Base STO-3G p/ o orbital 1s dos Hidrogênios A e B 
HA_gp1a = gaussiana_primitiva(0.3425250914e+01, 0.1543289673e+00, [0,0,0], 0 , 0 , 0)
HA_gp1b = gaussiana_primitiva(0.6239137298e+00, 0.5353281423e+00, [0,0,0], 0 , 0 , 0)
HA_gp1c = gaussiana_primitiva(0.1688554040e+00, 0.4446345422e+00, [0,0,0], 0 , 0 , 0)

HB_gp1a = gaussiana_primitiva(0.3425250914e+01, 0.1543289673e+00, [1.4,0,0], 0 , 0 , 0)
HB_gp1b = gaussiana_primitiva(0.6239137298e+00, 0.5353281423e+00, [1.4,0,0], 0 , 0 , 0)
HB_gp1c = gaussiana_primitiva(0.1688554040e+00, 0.4446345422e+00, [1.4,0,0], 0 , 0 , 0)
  
HA_1s = [HA_gp1a, HA_gp1b, HA_gp1c]
HB_1s = [HB_gp1a, HB_gp1b, HB_gp1c]

z = [1.0, 1.0]
coordenadas_atômicas = [np.array([0,0,0]), np.array([1.4,0,0])]
molécula = [HA_1s, HB_1s]

print('-'*50)
print('\nBase STO-3G para a molécula de H2:\n')
print('Matriz Sobreposição:\n',sobreposição(molécula),'\n')
print('Matriz Energia Cinética:\n',cinética(molécula),'\n')
print('Matriz Atração Elétron-Núcleo:\n',atração_elétron_núcleo(molécula, coordenadas_atômicas, z),'\n')

#sys.exit(0)

# Base 6-31G p/ os orbitais 1s e 2s dos Hidrogênios A e B
HA_gp1a = gaussiana_primitiva(0.1873113696E+02, 0.3349460434E-01, [0,0,0], 0 , 0 , 0)
HA_gp1b = gaussiana_primitiva(0.2825394365E+01, 0.2347269535E+00, [0,0,0], 0 , 0 , 0)
HA_gp1c = gaussiana_primitiva(0.6401216923E+00, 0.8137573261E+00, [0,0,0], 0 , 0 , 0)
HA_gp2a = gaussiana_primitiva(0.1612777588E+00, 1.0000000, [0,0,0], 0 , 0 , 0)

HB_gp1a = gaussiana_primitiva(0.1873113696E+02, 0.3349460434E-01, [1.4,0,0], 0 , 0 , 0)
HB_gp1b = gaussiana_primitiva(0.2825394365E+01, 0.2347269535E+00, [1.4,0,0], 0 , 0 , 0)
HB_gp1c = gaussiana_primitiva(0.6401216923E+00, 0.8137573261E+00, [1.4,0,0], 0 , 0 , 0)
HB_gp2a = gaussiana_primitiva(0.1612777588E+00, 1.0000000, [1.4,0,0], 0 , 0 , 0)

HA_1s = [HA_gp1a, HA_gp1b, HA_gp1c]
HA_2s = [HA_gp2a]
HB_1s = [HB_gp1a, HB_gp1b, HB_gp1c]
HB_2s = [HB_gp2a]

molécula = [HA_1s, HA_2s, HB_1s, HB_2s]

print('-'*50)
print('\nBase 6-31G para a molécula de H2:\n')
print('Matriz Sobreposição:\n',sobreposição(molécula),'\n')
print('Matriz Energia Cinética:\n',cinética(molécula),'\n')
print('Matriz Atração Elétron-Núcleo:\n',atração_elétron_núcleo(molécula, coordenadas_atômicas, z),'\n')