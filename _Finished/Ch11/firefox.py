from selenium import webdriver

def selenium_firefox():
    browser = webdriver.Firefox()
    print(type(browser))

    browser.get("http://google.com")



if __name__ == "__main__":
    selenium_firefox()
