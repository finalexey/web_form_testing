import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://hflabs.github.io/suggestions-demo/"


@pytest.mark.required_forms
def test_required_forms_filled(browser):
    browser.get(link)
    browser.implicitly_wait(5)

    lastname = 'Иванов'
    name = 'Иван'
    patronymic = 'Иванович'
    email = 'aa@mail.ru'
    message = 'abc'

    lastname_field = browser.find_element_by_id("fullname-surname")
    lastname_field.send_keys(lastname)

    name_field = browser.find_element_by_id("fullname-name")
    name_field.send_keys(name)

    patronymic_field = browser.find_element_by_id("fullname-patronymic")
    patronymic_field.send_keys(patronymic)

    email_field = browser.find_element_by_id("email")
    email_field.send_keys(email)

    message_field = browser.find_element_by_id("message")
    message_field.send_keys(message)

    send_button = browser.find_element_by_class_name("btn-primary")
    send_button.click()

    if WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'btn-default'), 'Хорошо, я понял')):
        head_feedback = browser.find_element_by_tag_name('h4').text

    assert 'правительство' in head_feedback, 'У правительства обед, обращение не зарегистрировано'
