
import pyautogui
import time
import pandas


# pyautogui.click
# pyautogui.write
# pyautogui.press
# pyautogui.hotkey

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: entrar no sistema da empresa

pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

pyautogui.write (link)
pyautogui.press ("enter")
# fazer uma pausa maior para o site carregar
time.sleep (3)


# Passo 2 fazer login

pyautogui.click (740, 509) # clicar no campo de email
pyautogui.write ("seu_email@exemplo.com")
pyautogui.press ("tab") # passar para o proximo campo
pyautogui.write ("sua_senha") 
time.sleep (1)
pyautogui.click (x=947, y=709)# clicar no botao entrar
pyautogui.click (x=947, y=709)# clicar no botao entrar  
# fazer uma pausa maior para o site carregar
time.sleep (3)


# Passo 3 abrir a base de dados
#pip install pandas

tabela = pandas.read_csv ("produtos.csv")
print (tabela)

for linha in tabela.index:

    # Passo 4 cadastrar 1 produto
    
    #codigo
    pyautogui.click (x=785, y=367) #clicar no codigo 
    codigo = str (tabela.loc[linha, "codigo"])
    pyautogui.write (codigo)
    pyautogui.press ("tab") # passar para o proximo campo

    #marca
    marca = str (tabela.loc[linha, "marca"])
    pyautogui.write (marca)
    pyautogui.press ("tab") # passar para o proximo campo

    #tipo
    tipo = str (tabela.loc[linha, "tipo"])
    pyautogui.write (tipo)
    pyautogui.press ("tab") # passar para o proximo campo

    #categoria
    categoria = str (tabela.loc[linha, "categoria"])
    pyautogui.write (categoria)
    pyautogui.press ("tab") # passar para o proximo campo

    #preço
    preco_unitario = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write (preco_unitario)
    pyautogui.press ("tab") # passar para o proximo campo

    #custo
    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write (custo)
    pyautogui.press ("tab") # passar para o proximo campo

    #obs
    obs = str (tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write (obs)
    pyautogui.press ("tab") # passar para o proximo campo

    pyautogui.press ("enter") #clicar no botao salvar
    
    #voltar para o inicio da tela
    pyautogui.scroll (5000)
    



# Passo 5  repetir o passo 4 ate acabar a lista de produtos



