from selenium import webdriver
import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


# Configura el controlador del navegador
driver = webdriver.Chrome('C:/Users/alber/Desktop/chromedriver.exe')

# Abre una página web
driver.get('https://www.leagueoflegends.com/es-mx/')


# Esperar a que la página cargue completamente
timeout = 10
wait = WebDriverWait(driver, timeout)
driver.implicitly_wait(10)
element = wait.until(EC.presence_of_element_located((By.ID, "my-element")))

# Tomar una captura de pantalla y guardarla en un archivo
filename = 'screenshot_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.png'
driver.save_screenshot(filename)

# Encontrar el elemento que se debe seleccionar para tomar la captura de pantalla
elemento = driver.find_element_by_id('INFORMACION DEL JUEGO')
elemento = driver.find_element_by_id('CAMPEONES')
elemento = driver.find_element_by_id('NOTICIAS')
elemento = driver.find_element_by_id('NOTAS DE VERSION')
elemento = driver.find_element_by_id('DESCUBRE')
elemento = driver.find_element_by_id('Esports')

# Seleccionar la opción
elemento.click()

# Tomar una captura de pantalla y guardarla como un archivo
driver.save_screenshot('captura.png')

# Esperar 5 segundos antes de cerrar el navegador
time.sleep(5)


##input("Presione cualquier tecla para cerrar el navegador...")
driver.quit()


