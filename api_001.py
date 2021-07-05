import flask
import time
import webdriver_manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/url', methods=['GET'])
def post_task():
    #example of http body
    # {
    #     "searchText": "azure devops",
    #     "expectedHeadPage": "Azure DevOps Projects"
    # }  

    if not request.args or not 'searchText' in request.args or not 'expectedHeadPage' in request.args :
       return jsonify(Message = "Parameters searchText and expectedHeadPage are required"), 500

    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    chrome_exe= ChromeDriverManager()
    driver = webdriver.Chrome(executable_path=chrome_exe.install(), options=options)
    driver.implicitly_wait(60) 

    searchText = request.args.get('searchText')
    expectedResult = request.args.get('expectedHeadPage')

    driver.get("https://www.google.com/")
    
    driver.find_element(By.NAME, "q").click()
    driver.find_element(By.NAME, "q").send_keys(searchText)
    driver.find_element(By.NAME, "btnK").click()
    driver.find_element(By.CSS_SELECTOR, ".hlcw0c:nth-child(3) .LC20lb").click()
    result = driver.find_element(By.CSS_SELECTOR, "h1").text 
    driver.quit()
    assert result == expectedResult    

    return jsonify(textSearched = f"{searchText}", headPageFound=result)


app.run()