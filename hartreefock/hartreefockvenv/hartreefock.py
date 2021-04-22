import sys
import math
import numpy as np

# classe das gaussianas primitivas
class gaussiana_primitiva():
    def __init__(self, alfa, coef, coordenadas, l1, l2, l3):
        self.alfa = alfa
        self.coef = coef
        self.coordenadas = coordenadas
        self.A = ( 2.0 * alfa / math.pi) ** 0.75 # + alguns termos p/ l1, l2 e l3 > 0




# Gaussianas primitivas dos Hidrogênios 1 e 2
H1_1s = [H1_pg1a, H1_pg1b, H1_pg1c]
H2_1s = [H2_pg1a, H2_pg1b, H2_pg1c]

molecule - [H1_1s, H2_1s]

