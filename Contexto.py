import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#acceder a la pagina de finnegans para iniciar sesion 
driver.get("https://go-qa.finneg.com/login")
driver.maximize_window()
time.sleep(2)


#ingresamos usuario de finneggas 
usuario = driver.find_element(By.XPATH, "//*[@id= 'email']")
time.sleep(2)
usuario.send_keys("amarquina@finnegans.com.ar")
time.sleep(2)

#ingreso de conmtraseña
contraseña = driver.find_element(By.XPATH, "//*[@id='password']")
time.sleep(2)
contraseña.send_keys("amarquina")
time.sleep(2)

#ingreso del espacio de trabajo y hacer click
espacio_trabajo = driver.find_element(By.XPATH, "//*[@id='workspace']")
time.sleep(2)
espacio_trabajo.send_keys("dpcomercializadoratest", Keys.ENTER)
time.sleep(5)

                                            
#Abrir menu hamburguesa
menu_hamburguesa = driver.find_element(By.XPATH, "/html/body/app-root/main/app-default/div/mat-sidenav-container/mat-sidenav-content/eco-toolbar/mat-toolbar/mat-toolbar-row[1]/div[1]/i")
time.sleep(2)
menu_hamburguesa.click()
time.sleep(2)

#Abrir Contextos

contextos = driver.find_element(By.XPATH, "/html/body/app-root/main/app-default/div/mat-sidenav-container/mat-sidenav/div/eco-sidebar/mat-nav-list/mat-list-item[3]")
time.sleep(1)
contextos.click()
time.sleep(2)

#Buscar Contexto

buscar_contexto = driver.find_element(By.XPATH, "//*[@id='searchBarContext']/div/input")
time.sleep(2)
buscar_contexto.send_keys("AUTOMATION")
time.sleep(2)
buscar_contexto.send_keys(Keys.ENTER)
time.sleep(2)

#Administrar Contexto
administrar_contexto = driver.find_element(By.XPATH, "//*[@id='mat-dialog-0']/eco-context-list/div/div[2]/div/div[5]/button")
time.sleep(2)
administrar_contexto.click()
time.sleep(2)

#Editar contexto
#Agregar descripcion

descripcion = driver.find_element(By.XPATH, "//*[@id='context-description']")
time.sleep(2)
descripcion.clear()
time.sleep(2)
descripcion.send_keys("ESTO ES UNA PRUEBA DE AUTOMATION HECHA POR ROSE")
time.sleep(2)

#Guardar cambios

boton_listo = driver.find_element(By.XPATH, "/html/body/app-root/main/app-default/div/mat-sidenav-container/mat-sidenav-content/div/eco-context-users-administration-dialog/div/button")
time.sleep(2)
boton_listo.click()
time.sleep(15)

#Cerrar ventana
driver.close()
