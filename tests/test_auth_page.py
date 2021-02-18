from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)  # задержка 3 сек для учебных целей
    page.enter_email('yelley@ye.qu')
    page.enter_pass('123456')
    page.btn.click()

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() != '/all_pets', 'login error'

    time.sleep(4)  # задержка 3 сек для учебных целей


# python -m pytest -v --driver Chrome --driver-path C:/driver/cromedriver.exe