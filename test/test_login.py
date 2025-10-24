from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time


def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        assert "/inventory.html" in driver.current_url,"No se Redirigio al inventario"
        
    except Exception as e:
        print(f"Error en testa_login: {e}")
        raise
    finally:
        driver.quit()    
