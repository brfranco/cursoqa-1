from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Definir a variável de ambiente diretamente no script
os.environ['URL_DO_SITE'] = 'https://www.jogajuntoinstituto.org/#Contato'

# Acessa a variável de ambiente
url = os.getenv('URL_DO_SITE')

@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_entro_na_pagina(context):
    context.driver = webdriver.Firefox()
    context.driver.get(url)

@when(u'Insiro meus dados')
def step_insiro_dados(context):
    context.driver.find_element(By.ID, "nome").send_keys("Fulano")
    context.driver.find_element(By.ID, "email").send_keys("fulano@teste.com")
    context.driver.find_element(By.ID, "assunto").send_keys("Ser facilitador")

@then(u'Envio a mensagen "Teste - Oi Boa Noite!!"')
def step_envio_mensagen(context):
    mensagem_element = context.driver.find_element(By.ID, "mensagem")
    mensagem_element.send_keys("Teste - Oi Boa Noite!!")
    
    botao_enviar = WebDriverWait(context.driver, 6).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/section[9]/div[1]/form/button"))
    )
    context.driver.execute_script("arguments[0].click();", botao_enviar)
    context.driver.quit()