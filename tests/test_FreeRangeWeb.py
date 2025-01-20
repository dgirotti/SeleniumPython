import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
 
 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#@pytest.mark.regresion
def test_navegacion_free_range_web():
    driver.get("https://www.freerangetesters.com")
    driver.find_element(By.XPATH, "//a[normalize-space()='Cursos' and @href]").click()
#con pytest -m regresion corro los tests que usan esa marca.