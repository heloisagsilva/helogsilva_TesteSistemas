from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

#Configuração do webdrive (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

#Acessa  a pagina de cadastro usando o caminho absoluto com o protocolo file://
#Certifique-se que o caminho esta apontando para o arquivo HTML especifico

driver.get("file:///C:/Users/heloisa_silva150/Documents/Testes_Sistemas/login.html")

#Preencha o campo usuario 
nome_input = driver.find_element(By.ID,"usuario")
nome_input.send_keys("admin")

#Preencha o senha
descricao_input = driver.find_element(By.ID, "senha")
descricao_input.send_keys("123456")

#Clicar no botão cadastrar 
#botao_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#botao_login.click()

#Aguarda um momento para visualizar o resultado 
#(em uma aplicação real, você verificaria a resposta)
#time.sleep(8)
if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso e redirecionado para a index.html!!")
else :
    print("Falha no login ou redirecionamento")

print("Titulo atual da pagina: ", driver.title)

#Fecha o navegador 
#driver.quit()