from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        time.sleep(5)
        
        # indicamos el usuario para login
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        # indicamos el pass para el login
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        # hacemos click en el boton
        driver.find_element(By.ID,"login-button").click()

        time.sleep(5)


    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()     

