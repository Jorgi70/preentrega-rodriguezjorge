from selenium import webdriver
import time
# importamos modulo de selenium para los selectores
from selenium.webdriver.common.by import By

#inicializamos el navegador Chrome
driver = webdriver.Chrome()
# analiza o valida el selenium implicitly_wait(espera elemento de la web)
driver.implicitly_wait(7)

try:
    # Ingresamos a la Pagina
    driver.get("https://www.saucedemo.com/")
    #  Validamos el Titulo de la misma
    titulo = driver.find_element(By.CLASS_NAME,"login_logo")
    assert titulo == "Swag Labs"

    print("Titulo Validado con EXITO")

except Exception as e:
    print(f"El error fue: {e}")
    raise

finally:
    driver.quit()
