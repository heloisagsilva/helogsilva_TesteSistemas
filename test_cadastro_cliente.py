from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

#Configuração do webdrive (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

#Acessa  a pagina de cadastro usando o caminho absoluto com o protocolo file://
#Certifique-se que o caminho esta apontando para o arquivo HTML especifico

driver.get("file:///C:/Users/heloisa_silva150/Documents/Testes_Sistemas/produto.html")

#Preencha o campo produto 
nome_input = driver.find_element(By.ID,"produto")
nome_input.send_keys("Bolsa")

#Preencha o descrição
descricao_input = driver.find_element(By.ID, "descricao")
descricao_input.send_keys("Azul com detalhes em preto")

#Preencha o campo marca
marca_input = driver.find_element(By.ID, "marca")
marca_input.send_keys("Gucci")

#Preencha o campo quantidade
quantidade_input = driver.find_element(By.ID, "quantidade")
quantidade_input.send_keys("5")

#Preencha o campo preço
preco_input = driver.find_element(By.ID, "preco")
preco_input.send_keys("3.95000")

#Clicar no botão cadastrar 
#submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#submit_button.click()

#Aguarda um momento para visualizar o resultado 
#(em uma aplicação real, você verificaria a resposta)
time.sleep(8)

#Fecha o navegador 
driver.quit()