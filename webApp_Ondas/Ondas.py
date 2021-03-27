# Soluções dos cálculos da lista 1

def regiao(comprimento):
    if comprimento > 740:
        cor = 'Infra Vermelho'
    elif 625 < comprimento <= 740:
        cor = '\033[1;31mVermelho\033[m'
    elif 590 < comprimento <= 625:
        cor = '\033[1;33mLaranja\033[m'
    elif 565 < comprimento <= 590:
        cor = '\033[33mAmarelo\033[m'
    elif 500 < comprimento <= 565:
        cor ='\033[1;32mVerde\033[m'
    elif 485 < comprimento <= 500:
        cor = '\033[1;36mCiano\033[m'
    elif 440 < comprimento <= 485:
        cor = '\033[1;34mAzul\033[m'
    elif 380 < comprimento <= 440:
        cor = '\033[1;35mVioleta\033[m'
    else:
        cor = 'Ultra Violeta'
    return cor

print('-=-' * 15)
print('{:^40}' .format(' Auxiliar de Estudos Quim2 '))
print('-=-' * 15)

# constantes
PLANCK = 6.6207 * (10 ** (-34)) # m²Kg/s
LUZ = 3 * (10 ** 8) # m/s
MASSA_ELETRON = 9.109 * (10 ** -31) # Kg

while True:
    opção = int(
    input(
f'''
----------------------------------------
      O que deseja calcular?
----------------------------------------
[ 1 ] Comprimento de onda de um elétron
[ 2 ] Frequência e Energia de uma onda
----------------------------------------
Sua opção: ''')
)
    print()
    if opção == 1:
        vel = float(input('Insira a velocidade da partícula em m/s e sem o exponencial (x10^6):  '))
        vel *= (10 ** 6)
        comprimento = PLANCK / (MASSA_ELETRON * vel) / (10 ** -9) # converte metros p/ nanometros
        frequencia = vel / comprimento
        energia = PLANCK * frequencia
        energia2 = energia / 1000 * (6.02 * (10 ** 23))
        print(
f'''
Dados:
---------------------
- Comprimento de Onda: {comprimento:.3f}nm
- Frequência: {frequencia:.2e} Hz.
- Energia: {energia:.2e} Joules.
           {energia2:.2e} KJ mol-¹.
----------------------'''
        )
        print()
    elif opção == 2:
        comprimento = int(input('Insira o comprimento de onda em nanômetros: '))
        print('O comprimento de onda {}nm pertence à região do {}'.format(comprimento, regiao(comprimento)))
        comprimento2 = comprimento * (10 ** -9) #converte nanômetros p/ metros
        frequencia = LUZ / comprimento2
        energia = PLANCK * frequencia
        energia2 = energia / 1000 * (6.02 * (10 ** 23))
        print()
        print(
f'''
Dados:
---------------------
- Comprimento de Onda: {comprimento}nm
- Frequência: {frequencia:.2e} Hz.
- Energia: {energia:.2e} Joules.
           {energia2:.2f} KJ mol-¹.
----------------------'''
        )
        print()
    continuar = str(input('Deseja continuar? [s / n] '))
    print()
    if continuar not in 'Ss':
        break
print()
print('-=-' * 15)
print('{:^40}' .format(' FIM DO PROGRAMA!!! '))
print('-=-' * 15)