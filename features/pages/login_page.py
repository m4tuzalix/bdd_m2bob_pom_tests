from .page_model import basePage

class Login(basePage):
    def __init__(self):
        basePage.__init__(self)

    def input_password(self, password):
        try:
            input_password = self.browser.find_element_by_css_selector("dd > input#password")
            input_password.send_keys(password)
        except:
            return False
        return True

    def validate_if_logged(self):
        try:
            succes_div = self.browser.find_element_by_css_selector("div.success p").text
            return succes_div
        except:
            return False

    def account_activated(self):
        try:
            not_activated = self.browser.find_element_by_css_selector("div.userNotice p.warning").text
            return not_activated
        except:
            return False

