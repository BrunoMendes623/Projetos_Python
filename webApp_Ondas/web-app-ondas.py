import streamlit as st 
import matplotlib.pyplot as plt 

# Função para tratamento das cores
def cores_onda(comprimento):
    if comprimento > 675:
        cor = ('#d8020b', 'w')
    elif 650 < comprimento <= 675:
        cor = ('#e65907', 'w')
    elif 625 < comprimento <= 650:
        cor = ('#ea8100', 'w')
    elif 600 < comprimento <= 625:
        cor = ('#f2b600', 'w')
    elif 575 < comprimento <= 600:
        cor = ('#f7eb18', 'w')
    elif 550 < comprimento <= 575:
        cor = ('#86b81a', 'w')
    elif 525 < comprimento <= 550:
        cor = ('#008e3a', 'w')
    elif 500 < comprimento <= 525:
        cor = ('#159c96', 'w')
    elif 475 < comprimento <= 500:
        cor = ('#4793cd', 'w')
    elif 450 < comprimento <= 475:
        cor = ('#0153a0', 'w')
    elif 425 < comprimento <= 450:
        cor = ('#0d1b81', 'w')
    elif 400 <= comprimento <= 425:
        cor = ('#5d117d', 'w')
    return cor


# Constantes
MOL = 6.02e23
PLANCK = 6.6207e-34 # m²Kg/s
LUZ = 2.99792458e8 # m/s
MASSA_ELÉTRON = 9.10938e-31 # Kg
NANO = 1e-9 
KILO = 1e3
MEGA = 1e6 
TERA = 1e12 

# Menu principal
st.sidebar.image('https://cdn.pixabay.com/photo/2016/11/11/20/05/wave-1817646_960_720.png', use_column_width=True)
st.sidebar.title('Escolha uma opção')
opção_menuprincipal = ('Sobre', 'Usar o app')
selecionar_menuprincipal = st.sidebar.selectbox('', opção_menuprincipal)

# Menu "Sobre"
if selecionar_menuprincipal == opção_menuprincipal[0]:
    st.sidebar.success('P/ continuar selecione "Usar o app".')
    st.markdown(
    '''
    # Auxiliar de estudos - Ondas
    ---
    ## Descrição
    O intuito do WebApp é facilitar a compreensão do estudante frente 
    aos assuntos "Ondas Eletromagnéticas" e "Compostos de Coordenação".

    ## Funcionamento
    👈 Selecione a opção _**Usar o App**_ no menu ao lado e selecione uma das opções abaixo.
    - **Frequência e Energia de uma onda** -
    Você encontrará um display dinâmico. Basta selecionar um comprimento de onda qualquer clicando e arrastando o mouse ao longo da barra horizontal. O programa irá calcular as propriedades automaticamente e também mostrará um círculo colorido, que representa a cor correspondente ao comprimento de onda selecionado.
    - ** Comprimento de onda de um elétron** - 
    Basta digitar a velocidade do elétron em m/s sem a notação 10^6. O programa mostrará uma lista de propriedades calculadas.
    ---
    **Criador:**
    [Bruno Henrique de Medeiros](https://www.linkedin.com/in/brunohenriquemendes/) 
    '''
    )

# Menu "Usar APP"
elif selecionar_menuprincipal == opção_menuprincipal[1]:

    opção_app = ('Frequência e Energia de uma onda', 'Comprimento de onda de um elétron')
    selecionar_app = st.sidebar.radio('O que deseja calcular?', opção_app)

    # Corpo da opção "Frequência e Energia de uma onda"
    if selecionar_app == opção_app[0]:
        st.markdown('# Comprimento de onda:')
        comprimento = st.slider('', 400, 700)  # slider p/ selecionar os comprimentos de forma dinâmica

        # Cálculo das grandezas
        comprimento_nano = comprimento * NANO 
        frequência = LUZ / comprimento_nano 
        frequência_tera = frequência / TERA
        energia_j = PLANCK * frequência
        energia_kjmol = (energia_j * MOL) / KILO
         
        # Apresentação dos dados
        coluna_esquerda, coluna_direita = st.beta_columns(2) # Separa o layout em 2 colunas
        with coluna_esquerda:
            st.markdown(
            f'''
            #
            ## Dados:
            ### - Comprimento de Onda: **{comprimento} nm**
            ### - Frequência: **{frequência_tera:.2f} THz**
            ### - Energia: **{energia_j:.2e} J**
            ### - Energia por mol: **{energia_kjmol:.2f} KJ/mol**
            '''
            )
        # Cores
        with coluna_direita:
            st.markdown('#')
            circulo = (1, 0)
            fig1, ax1 = plt.subplots()
            paramentro = cores_onda(comprimento)
            plt.pie(circulo, colors=paramentro , radius=0.8)
            st.pyplot(fig1)

    # Corpo da opção "Comprimento de onda de um elétron"
    elif selecionar_app == opção_app[1]:
        st.markdown('# Insira a velocidade do elétron em m/s:')
        v_elétron = st.number_input('', help="Digite o número sem o exponencial (10^6)")
        v_elétron *= MEGA
        if  v_elétron: # para evitar o erro de divisão por zero
            comprimento_elétron = PLANCK / (MASSA_ELÉTRON * v_elétron)  / NANO # converte metros p/ nanometros
            frequência_elétron = v_elétron / comprimento_elétron / MEGA
            energia_j_elétron = PLANCK * frequência_elétron 
            energia_kjmol_elétron = (energia_j_elétron * MOL) / KILO
            st.markdown(
            f'''
            #
            ## Dados:
            ### - Comprimento de Onda: **{comprimento_elétron:.3f} nm**
            ### - Frequência: **{frequência_elétron:.2f} MHz**
            ### - Energia: **{energia_j_elétron:.2e} J**
            ### - Energia por mol: **{energia_kjmol_elétron:.2e} KJ/mol**
            '''
            )