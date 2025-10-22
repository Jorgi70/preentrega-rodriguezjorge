from selenium import webdriver
# importamos modulo de selenium para los selectores
from selenium.webdriver.common.by import By


def test_nav():
    #inicializamos el navegador Chrome
    driver = webdriver.Chrome()
    # analiza o valida el selenium implicitly_wait(espera elemento de la web)
    driver.implicitly_wait(7)

    try:
        # Ingresamos a la Pagina
        driver.get("https://www.saucedemo.com/")
        # indicamos el usuario para login
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        # indicamos el pass para el login
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        # hacemos click en el boton
        driver.find_element(By.ID,"login-button").click()
        # Validamos que redirecciones a /inventory.html
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"
        
        #  Aca agarramos el titulo con una clase dentro de inventory.html
        titulo = driver.find_element(By.CLASS_NAME,"app_logo")
        
        # Aca validamos el titulo
        assert titulo.text == "Swag Labs",f"Titulo incorrecto: {titulo.text}"

        print("Titulo Validado con EXITO")

    except Exception as e:
        print(f"El error fue: {e}")
        raise

    finally:
        driver.quit()
