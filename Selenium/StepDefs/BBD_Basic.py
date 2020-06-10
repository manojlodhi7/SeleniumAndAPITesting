from selenium import webdriver
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../Features/BDD_Basic.feature', example_converters=dict(phrase=str))

@given("Setup driver")
def setup():
    global driver
    driver = webdriver.Firefox(executable_path=r'C:\Practice_Python_Projects\geckodriver.exe')

