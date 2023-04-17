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

with open("dataregisterchrome.txt", "r") as f:
    contenido = f.readlines()

accepted=0
rejected=0

for i in range(0, len(contenido), 4):
    nombre = contenido[i].strip()
    usuario = contenido[i+1].strip()
    correo = contenido[i+2].strip()
    contra = contenido[i+3].strip()
    try:
        usr = d.find_element(By.ID, "auto").click() 
        usr = d.find_element(By.ID, "exampleInputEmail1").click()
        usr = d.find_element(By.ID, "exampleInputEmail1").send_keys(nombre)
        usr = d.find_element(By.NAME, "username").click()
        usr = d.find_element(By.NAME, "username").send_keys(usuario)
        usr = d.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
        usr = d.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys(correo)
        usr = d.find_element(By.ID, "exampleInputPassword1").click()
        usr = d.find_element(By.ID, "exampleInputPassword1").send_keys(contra)
        usr = d.find_element(By.NAME, "signup").click()
        d.refresh()
        usr = d.find_element(By.CSS_SELECTOR, "h2").text
        if usr == "Home":
            accepted+=1
        usr = d.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
    except Exception as e:
        rejected+=1

with open("reportecp1+chrome.txt", "w") as file:
    file.write("")

archivo2 = open("reportecp1+chrome.txt", "r+")
contenido_adicional = "Pruebas Exitosas = "+str(accepted)+"\n"+"Pruebas Fallidas = "+str(rejected) # Contenido adicional a agregar
archivo2.write(contenido_adicional)
archivo2.close()
