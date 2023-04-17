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

d = webdriver.Edge(executable_path='C:\Descargas\msedgedriver.exe')
d.get("https://tucan.toolsincloud.net/")

accepted=0
rejected=0
perfiles = []

d.find_element(By.NAME, "email").click()
d.find_element(By.NAME, "email").send_keys("username1@prueba.com")
d.find_element(By.NAME, "password").click()
d.find_element(By.NAME, "password").send_keys("12345")
d.find_element(By.NAME, "login").click()

for i in range(0, 10, 1):
    try:
        usr = d.find_element(By.CSS_SELECTOR, ".grid-share:nth-child(2) strong").click()
        usr = d.find_element(By.CSS_SELECTOR, ".home-name").text
        accepted+=1
        perfiles.append(usr)
        print(usr)
    except Exception as e:
        rejected+=1

with open("reportecp5+edge.txt", "w") as file:
    file.write("")

with open("reportecp5+edge.txt", "w") as archivo:
    contenido_adicional = "Pruebas Exitosas = "+str(accepted)+"\n"+"Pruebas Fallidas = "+str(rejected)+"\n" 
    archivo.write(contenido_adicional)
    for elemento in perfiles:
        archivo.write(elemento + "\n")