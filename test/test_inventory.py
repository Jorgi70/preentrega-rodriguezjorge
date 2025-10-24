from selenium.webdriver.common.by import By
from selenium import webdriver


def test_inventory(login_in_driver):
    try:
        
        driver = login_in_driver;
        
        assert driver.title == "Swag Labs";
        
        # Aca treamos todos los elementos inventory de la pagina
        products = driver.find_elements(By.CLASS_NAME, "inventory_item");
        
        # Verificamos que haya productos
        assert len(products) > 0, "No hay Productos Visibles en la Pagina";
        
        # Eligo el del Primer Producto y lo paso a texto
        titulo_producto1 = products[0].text;
        
        # Creo otra Variable para comprobar el Primer Producto
        titulo_primer = "Sauce Labs Backpack";
        
        # Verificamos que sea el titulo 1 con el starts para validar la cadena de texto
        assert titulo_producto1.startswith(titulo_primer),f"Fallo la verificacion, el titulo es: {titulo_producto1}";
        
        # Busco el boton del menu 
        boton_menu = driver.find_element(By.ID,"react-burger-menu-btn");
        
        #Verificamos el boton exista con displayed
        assert boton_menu.is_displayed(),"Fallo la verificacion. El boton no esta visible";
    
        
    except Exception as e:
        print(f"El error fue: {e}");
        raise;
    finally:
        driver.quit();