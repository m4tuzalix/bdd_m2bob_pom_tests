# Created by Mateusz at 31.03.2020

Feature: Account managament
  # tags to distinguish the scenarios

  @register
  Scenario Outline: User register the new account
    Given I'm opening the page 'https://m2bob-forum.net/'
    Then I'm checking the 'register' checkbox
    And Providing my login <login>
    And Clicking the submit button
    When The page has reloaded, I should see the rules and accept it by clicking the button
    Then I should see registration form
    And Fulfill the registration form with my credentials <email> <email2> <password> <password2>
    Then I should validate if the data I have just provided is acceptable
    When The data is ok and submit has been clicked, I shouldn't get my account created because I'm selenium bot :)
    #// Page is secured with some sort of JS script what makes me unable to register the account with selenium
    Examples: Register
     |login    |email           |email2          |password   | password2   |
     |xyz345   |xyz@gmail.com   |xyz@gmail.com   |Qazzaq12312| Qazzaq12312 |
     
  @login
  Scenario Outline: User login to his account
    Given I'm opening the page 'https://m2bob-forum.net/'
    Then I'm checking the 'login' checkbox
    And Providing my login <email>
    And Providing my password 'netguru1'
    And Clicking the submit button
    When The previous actions have been performed, I should see the message 'You have been logged in.'
    And If my account has not been activated yet, I should see the message 'Your user account is not activated yet.'

    Examples: Login
    |email              |
    |netguruQA@test.com |

