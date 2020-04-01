from selenium import webdriver
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from features.pages.register_page import RegisterPage
from features.pages.login_page import Login

def before_tag(context, tag):
    if tag == "register":
        context.model = RegisterPage()
    elif tag == "login":
        context.model = Login()

def after_scenario(context, *args):
    context.model.close_page()