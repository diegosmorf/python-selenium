## Python

<a href="https://www.python.org"><img src="https://wiki.python.org/wiki/europython/img/python-logo.gif" alt="Python"/></a>

Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python!

* [Beginner's Guide, Programmers](https://wiki.python.org/moin/BeginnersGuide/Programmers)
* [Beginner's Guide, Non-Programmers](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
* [Beginner's Guide, Download & Installation](https://wiki.python.org/moin/BeginnersGuide/Download)
* [Code sample and snippets for Beginners](https://wiki.python.org/moin/BeginnersGuide/Examples)

## Selenium

<a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>

Selenium is an umbrella project encapsulating a variety of tools and libraries enabling web browser automation. Selenium specifically provides an infrastructure for the [W3C WebDriver specification](https://w3c.github.io/webdriver/) — a platform and language-neutral coding interface compatible with all major web browsers.

Selenium's source code is made available under the [Apache 2.0 license](https://github.com/SeleniumHQ/selenium/blob/trunk/LICENSE).

Selenium IDE Browser Extensions: 
The new Selenium IDE is designed to record your interactions with websites to help you generate and maintain site automation, tests, and remove the need to manually step through repetitive takes. 

Features include:
* Recording and playing back tests on Firefox, Chrome and Edge.
* Organizing tests into suites for easy management.
* Export to your favorite software language (eg.python, java, C# etc)

Download:
- Firefox: [link](https://addons.mozilla.org/pt-BR/firefox/addon/selenium-ide/)
- Chrome: [link](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd)
- Edge: [link](https://microsoftedge.microsoft.com/addons/detail/selenium-ide/ajdpfmkffanmkhejnopjppegokpogffp)

## Documentation

* [User Manual](https://selenium.dev/documentation/)
* [Python](https://seleniumhq.github.io/selenium/docs/api/py/)

## Requirements

* [Python 3.7+](https://www.python.org/downloads/)
* `python` on the PATH
* [Visual Code](https://code.visualstudio.com/download)
* [Insomnia Rest Client](https://insomnia.rest/download)

## Installing required python libraries:

```bash
    python -m pip install --upgrade pip setuptools wheel    
    pip install selenium
    pip install pytest
    pip install pytest-html
    pip install pytest-cov
    pip install flask
    pip install webdriver_manager 
```

## Running Scripts

```bash    
    python .\test_003.py
    
```

## Running Tests

```bash
    #Running tests
    pytest .\test_001.py
    #Running tests + generating coverage report
    pytest --doctest-modules --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html    
```

## Running Tests

```bash    
    #Running Flask API
    python .\api_001.py 

    GET = http://127.0.0.1:5000/api/url?searchText=azure devops&expectedHeadPage=Azure DevOps Projects
    {
        "searchText": "azure devops",
        "expectedHeadPage": "Azure DevOps Projects"
    }  

```
