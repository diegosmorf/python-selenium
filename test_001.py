import pytest
import time
import webdriver_manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestWrapper():
  def setup_method(self, method):    
    options = webdriver.ChromeOptions()    
    #options.add_argument('--headless')    
    chrome_exe= ChromeDriverManager()
    self.driver = webdriver.Chrome(executable_path=chrome_exe.install(), options=options)
    self.driver.implicitly_wait(60)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  [pytest]
  def test_run(self):    

    searchText = "azure devops"
    expectedResult = "Azure DevOps Projects"

    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(1540, 845)
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys(searchText)
    self.driver.find_element(By.NAME, "btnK").click()
    self.driver.find_element(By.CSS_SELECTOR, ".hlcw0c:nth-child(3) .LC20lb").click()
    result = self.driver.find_element(By.CSS_SELECTOR, "h1").text 

    assert result == expectedResult
