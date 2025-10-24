import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
  
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver    