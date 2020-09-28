from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	REGISTER_FORM = (By.id, "register_form1")
	LOGIN_FORM = (By.id, "login_form1")
