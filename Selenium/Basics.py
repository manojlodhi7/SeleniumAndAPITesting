from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_setup():
    global driver
    driver = webdriver.Firefox(executable_path=r'C:\Practice_Python_Projects\geckodriver.exe')


def test_search_on_google():
    driver.get("http://www.google.com")
    print(driver.title)
    print("Google" in driver.title)
    assert "Google" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("My First Python Selenium Project")
    elem.send_keys(Keys.RETURN)

    search = driver.find_element_by_xpath(
        '''//div[@class = "FPdoLc tfB0Bf"]/center/input[@value="Google Search" and @type = "submit"][1]''')
    search.click()


def test_close():
    driver.close()
    driver.quit()
