from .pages.main_page import MainPage
from .locators import MainPageLocators
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, MainPageLocators.MAIN_PAGE)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
	
def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, MainPageLocators.MAIN_PAGE)
    page.open()
    page.should_be_login_link()
	
def test_guest_can_go_to_login_page(browser):
	page = MainPage(browser, MainPageLocators.MAIN_PAGE)
	page.open()
	login_page = page.go_to_login_page()
	login_page.should_be_login_url()
