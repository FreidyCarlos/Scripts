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

with open("datacp6.txt", "r") as f:
    contenido = f.readlines()

accepted=0
rejected=0

for i in range(0, len(contenido), 3):
    usuario = contenido[i].strip()
    contra = contenido[i+1].strip()
    change = contenido[i+2].strip()
    try:
        usr = d.find_element(By.NAME, "email").click()
        usr =d.find_element(By.NAME, "email").send_keys(usuario)
        usr = d.find_element(By.NAME, "password").click()
        usr = d.find_element(By.NAME, "password").send_keys(contra)
        usr = d.find_element(By.NAME, "login").click()
        usr = d.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(7) img").click()
        usr = d.find_element(By.CSS_SELECTOR, ".home-edit-button").click()
        usr = d.find_element(By.ID, "exampleInputEmail1").click()
        usr = d.find_element(By.ID, "exampleInputEmail1").clear()
        usr = d.find_element(By.ID, "exampleInputEmail1").send_keys(change)
        usr = d.find_element(By.NAME, "update").click()
        usr = d.find_element(By.CSS_SELECTOR, "h4").text
        if usr == change:
            accepted+=1
        usr = d.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
    except Exception as e:
        rejected+=1

with open("reportecp6+edge.txt", "w") as file:
    file.write("")

archivo2 = open("reportecp6+edge.txt", "r+")
contenido_adicional = "Pruebas Exitosas = "+str(accepted)+"\n"+"Pruebas Fallidas = "+str(rejected) # Contenido adicional a agregar
archivo2.write(contenido_adicional)
archivo2.close()