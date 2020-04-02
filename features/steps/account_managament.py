from behave import *

#----------------REGISTER----------------#

@given("I'm opening the page '{link}'")
def open_page(context, link):
    context.page_opened = context.model.open_page(link)
    assert context.page_opened == True

@then("I'm checking the '{box}' checkbox")
def check_box(context, box):
    context.box = context.model.choose_box(box)
    assert context.box == True

@then("Providing my login {login}")
def put_login(context, login):
    context.login = context.model.input_login(login)
    assert context.login == True

@then("Clicking the submit button")
def click_button(context):
    context.button = context.model.click_submit()
    assert context.button == True

@when("The page has reloaded, I should see the rules and accept it by clicking the button")
def accept_the_rules(context):
    context.rules = context.model.accept_the_rules()
    assert context.rules == True

@then("I should see registration form")
def check_registration_form(context):
    context.form_name = context.model.check_if_form_visible()
    assert "Registration" in str(context.form_name)

@then("Fulfill the registration form with my credentials {email} {email2} {password} {password2}")
def fulfill_the_form(context, email, email2, password, password2):
    context.credentials = [email, email2, password, password2]
    context.fields_fulfillment = context.model.fulfill_the_fields(context.credentials)
    assert context.fields_fulfillment == True

@then("I should validate if the data I have just provided is acceptable")
def validate_data(context):
    context.validation = context.model.validate_data_provided()
    assert context.validation == True

@when("The data is ok and submit has been clicked, I shouldn't get my account created because I'm selenium bot :)")
def click_submit_register(context):
    context.submit_button = context.model.click_submit_register()
    assert context.submit_button == True

#----------------LOGIN----------------#

@then("Providing my password '{password}'")
def put_password(context, password):
    context.password_provided = context.model.input_password(password)
    assert context.password_provided == True

@when("The previous actions have been performed, I should see the message '{message}'")
def validate_login(context, message):
    context.login_message = context.model.validate_if_logged()
    assert message == str(context.login_message)

@when("If my account has not been activated yet, I should see the message '{message}'")
def check_if_account_activated(context, message):
    context.account_not_activated = context.model.account_activated()
    assert message in str(context.account_not_activated)

