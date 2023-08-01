# Passo a passo do projeto:
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Login
# Passo 3: Importar a base de produtos pra cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim

# pyautogui - Ferramenta que permite o Python controlar o mouse e o teclado do computador
# import time - tempo de espera

import pyautogui
import time

# pyautogui.write -> Este comando escreve o texto
# pyautogui.press -> Este comando aperta uma tecla do pc
# pyautogui.click -> Este comando clica em algum lugar da tecla
# pyauto.hotkey -> Combinação de teclas
# pyautogui.PAUSE = Segundos de espera
    
        # PASSO 1: ENTRAR NO SISTEMA DA EMPRESA.

#- Abrir o navegador:
# - tecla do windowns - digitar chrome - apertar enter

pyautogui.PAUSE =1
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

#- Entrar no link do sistema:
#- digitar o link - pressionar enter

time.sleep(0.5)
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

        # PASSO 2: FAZER LOGIN.
# - Selecionar o campo de email -> print(pyautogui.position()) <- posicao do click do mouse
# - Escrever email 
# - Selecionar o campo de senha
# - Escrever a senha 
# - Logar

time.sleep(2)
pyautogui.click(x=2010, y=369)
pyautogui.write("david.tostes@hotmail.com")
time.sleep(0.1)
pyautogui.click(x=1983, y=475)
pyautogui.write("123456")
time.sleep(0.1)
pyautogui.click(x=2171, y=536)

        # PASSO 3 - IMPORTAR BASE DE PRODUTOS PARA CADASTRAR 
        
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

        # PASSO 4 - CADASTRAR UM PRODUTO
for linha in tabela.index:
        # Clicar no campo código
        pyautogui.click(1930, y=248)
        # pegar da tabela o valor do campo a ser preenchido
        codigo = tabela.loc[linha, "codigo"]
        #marca = tabela.loc[linha, "marca"]
        # preencher o campo
        pyautogui.write(str(codigo))
        # passar para o proximo campo
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")
        # PD ISNA -> verifica se não está vazio
        # se nao tiver vazio o "obs", entao vou escrever a informacao do obs
        if not pd.isna(tabela.loc[linha, "obs"]):
                pyautogui.write(str(tabela.loc[linha, "obs"]))
        pyautogui.press("tab")
        pyautogui.press("enter")

        #dar scroll de tudo pra cima para recomecar os registros:
        pyautogui.scroll(5000)
