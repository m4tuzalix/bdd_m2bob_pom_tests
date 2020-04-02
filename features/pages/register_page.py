from .page_model import basePage

class RegisterPage(basePage):
    def __int__(self):
        basePage.__init__(self)

    def accept_the_rules(self):
        try:
            rules_input = self.browser.find_element_by_css_selector("input[name='accept']")
            rules_input.click()
        except:
            return False
        return True

    def check_if_form_visible(self):
        try:
            h1 = self.browser.find_element_by_css_selector("header.boxHeadline > h1").text
            return h1
        except:
            return False

    def fulfill_the_fields(self, credentials): #/ inputs are doubled so implemented js to retriev the correct ones
        try:
            self.fields = self.browser.execute_script("""
                const fields = document.querySelectorAll("div[class='container containerPadding marginTop'] input")
                const required_fields = []
                fields.forEach((field)=>{
                    const field_autocomplete = field.getAttribute("autocomplete")
                    if(field_autocomplete == null){
                        required_fields.push(field)
                    }
                });
                return required_fields
            """)
            for x in range(len(credentials)):
                try:
                    self.fields[x+1].send_keys(credentials[x]) #/ +1 because I want to skip the login(Already inehrited)
                except:
                    continue
            return True
        except:
            return False

    def validate_data_provided(self): #/ if login/email is already taken or password do not match, the red labels appear
        try:
            possible_errors = self.browser.execute_script("""
                const errors = document.querySelectorAll("small.innerError")
                return errors
            """)
            if len(possible_errors) > 0:
                raise ValueError
        except:
            return False
        return True

    def click_submit_register(self):
        try:
            button = self.browser.execute_script("""
                const button = document.querySelector("input[value='Submit']")
                button.click()
            """)
            script_error = self.browser.execute_script("""
                const script_error = document.querySelector("div.userNotice p.error")
                return script_error
            """)
            if script_error:
                raise Exception
        except:
            return False
        return True

