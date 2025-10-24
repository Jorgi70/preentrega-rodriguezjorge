from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login():
    driver = webdriver.Chrome()
    # Se agrega el implicity para validar todas las busquedas
    driver.implicitly_wait(7)

    try:
        driver.get("https://www.saucedemo.com/")


        # indicamos el usuario para login
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        # indicamos el pass para el login
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        # hacemos click en el boton
        driver.find_element(By.ID,"login-button").click()

        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"

        print("Login exitoso y validado correctamente.")


    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()     

