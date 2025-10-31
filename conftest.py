import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()