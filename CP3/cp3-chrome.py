import time
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver 

d = webdriver.Chrome(executable_path='C:\Descargas\chromedriver.exe')
d.get("https://tucan.toolsincloud.net/")

with open("publicaciones.txt", "r") as f:
    contenido = f.readlines()

accepted=0
rejected=0

d.find_element(By.NAME, "email").click()
d.find_element(By.NAME, "email").send_keys("username1@prueba.com")
d.find_element(By.NAME, "password").click()
d.find_element(By.NAME, "password").send_keys("12345")
d.find_element(By.NAME, "login").click()

for i in range(0, len(contenido), 1):
    msj = contenido[i].strip()
    try:
        usr = d.find_element(By.NAME, "status").click()
        usr = d.find_element(By.ID, "tweet-input").click()
        usr = d.find_element(By.CSS_SELECTOR, ".item2-pair").text
        if usr == "status or image are required":
            accepted+=1
    except Exception as e:
        rejected+=1

with open("reportecp3-chrome.txt", "w") as file:
    file.write("")

archivo2 = open("reportecp3-chrome.txt", "r+")
contenido_adicional = "Pruebas Exitosas = "+str(accepted)+"\n"+"Pruebas Fallidas = "+str(rejected) # Contenido adicional a agregar
archivo2.write(contenido_adicional)
archivo2.close()