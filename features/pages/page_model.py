from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class basePage(object):
    def __init__(self):
        self.browser = webdriver.Chrome("D:/netguru/features/chromedriver.exe")
        self.timeout = 10

    def open_page(self, url):
        try:
            def login_or_register(): #/ this button needs to be clicked to either login or register
                button = self.browser.execute_script("""
                    const login = document.querySelector("a.loginLink")
                    return login
                """)
                return button
            self.browser.implicitly_wait(self.timeout)
            self.browser.set_script_timeout(5) #/ timeout for js
            self.browser.maximize_window()
            self.browser.get(url)
            login_or_register().click()
        except:
            return False
        return True

    def close_page(self):
        self.browser.quit()

    def choose_box(self, action): #/ 3 checkboxes in total whilst 2 of them represent login and register
        try:
            actions = self.browser.execute_script("""
                const actions = document.querySelectorAll("dd label")
                return actions
            """)
            if action == "register":
                actions[0].click()
            elif action == "login":
                actions[1].click()
            else:
                raise AttributeError
            return True
        except:
            return False

    def input_login(self, login):
        try:
            input = self.browser.find_element_by_css_selector("dd > input#username")
            input.send_keys(login)
        except:
            return False
        return True

    def click_submit(self):
        try:
            button = self.browser.find_element_by_css_selector("div.formSubmit input#loginSubmitButton")
            button.click()
        except:
            return False
        return True


