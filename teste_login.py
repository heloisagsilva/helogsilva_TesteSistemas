from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

#Configuração do webdrive (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

#Acessa  a pagina de cadastro usando o caminho absoluto com o protocolo file://
#Certifique-se que o caminho esta apontando para o arquivo HTML especifico

driver.get("http://localhost:8080/helogsilva_TesteSistemas/login.html")

#Preencha o campo usuario 
# nome_input = driver.find_element(By.ID,"usuario")
# nome_input.send_keys("admin")

#Preencha o senha
# descricao_input = driver.find_element(By.ID, "senha")
# descricao_input.send_keys("123456")

#Clicar no botão cadastrar 
#botao_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#botao_login.click()

#Aguarda um momento para visualizar o resultado 
#(em uma aplicação real, você verificaria a resposta)

#Preencha o campo usuario 
driver.find_element(By.ID,"usuario").send_keys("admin")

#Preencha o campo usuario 
driver.find_element(By.ID,"senha").send_keys("123456")

#Preencha o campo usuario 
# driver.find_element(By.CSS_SELECTOR, "button ['type'submit']").click()

time.sleep(2)
if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso e redirecionado para a index.html!!")
else :
    print("Falha no login ou redirecionamento")

print("Titulo atual da pagina: ", driver.title)

#Fecha o navegador 
#driver.quit()