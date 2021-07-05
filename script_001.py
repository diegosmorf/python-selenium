import webdriver_manager
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

print(f"Test Start")
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
chrome_exe= ChromeDriverManager()
driver = webdriver.Chrome(executable_path=chrome_exe.install(), options=options)
driver.implicitly_wait(60)

searchText = "azure devops"
expectedResult = "Azure DevOps Projects"

driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").click()
driver.find_element(By.NAME, "q").send_keys(searchText)
driver.find_element(By.NAME, "btnK").click()
driver.find_element(By.CSS_SELECTOR, ".hlcw0c:nth-child(3) .LC20lb").click()
result = driver.find_element(By.CSS_SELECTOR, "h1").text
driver.quit()
assert result  == expectedResult
print(f"Test run sucessfully: Head Page = '{result}'")