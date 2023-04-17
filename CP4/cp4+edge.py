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

with open("datalogin.txt", "r") as f:
    contenido = f.readlines()

accepted=0
rejected=0
change="cambiuosuario"
contador=1

for i in range(0, len(contenido), 2):
    usuario = contenido[i].strip()
    contra = contenido[i+1].strip()
    try:
        usr = d.find_element(By.NAME, "email").click()
        usr =d.find_element(By.NAME, "email").send_keys(usuario)
        usr = d.find_element(By.NAME, "password").click()
        usr = d.find_element(By.NAME, "password").send_keys(contra)
        usr = d.find_element(By.NAME, "login").click()
        usr = d.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) img").click()
        usr = d.find_element(By.ID, "exampleInputPassword1").click()
        usr = d.find_element(By.ID, "exampleInputPassword1").clear()
        usr = d.find_element(By.ID, "exampleInputPassword1").send_keys(change+str(contador))
        usr = d.find_element(By.NAME, "submit").click()
        usr = d.find_element(By.CSS_SELECTOR, ".grid-user p.username").text
        if usr == "@"+change+str(contador):
            accepted+=1
        else:
            rejected+=1
        usr = d.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        contador+=1
    except Exception as e:
        print()

with open("reportecp4+edge.txt", "w") as file:
    file.write("")

archivo2 = open("reportecp4+edge.txt", "r+")
contenido_adicional = "Pruebas Exitosas = "+str(accepted)+"\n"+"Pruebas Fallidas = "+str(rejected)+"\n" # Contenido adicional a agregar
archivo2.write(contenido_adicional)
archivo2.close()