import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://hflabs.github.io/suggestions-demo/"
lastname = 'Иванов'
name = 'Иван'
patronymic = 'Иванович'
email = 'aa@mail.ru'
message = 'abc'
phone = '+79991234567'
postal_code = '422540'
city = 'Kazan'
street = 'Толстого'
building = '15'
appartment = '5'


@pytest.mark.positive_required_fields
def test_positive_required_fields_filled(browser):

    browser.get(link)
    browser.implicitly_wait(5)

    lastname_field = browser.find_element_by_id("fullname-surname")
    lastname_field.send_keys(lastname)

    name_field = browser.find_element_by_id("fullname-name")
    name_field.send_keys(name)

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


@pytest.mark.positive_all_fields
def test_positive_all_fields_filled(browser):

    browser.get(link)
    browser.implicitly_wait(5)

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

    phone_field = browser.find_element_by_id('phone')
    phone_field.send_keys(phone)

    postal_code_field = browser.find_element_by_id('address-postal_code')
    postal_code_field.send_keys(postal_code)

    city_field = browser.find_element_by_id('address-city')
    city_field.send_keys(city)

    street_field = browser.find_element_by_id('address-street')
    street_field.send_keys(street)

    building_field = browser.find_element_by_id('address-house')
    building_field.send_keys(building)

    appartment_field = browser.find_element_by_id('address-flat')
    appartment_field.send_keys(appartment)

    send_button = browser.find_element_by_class_name("btn-primary")
    send_button.click()

    if WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'btn-default'), 'Хорошо, я понял')):
        head_feedback = browser.find_element_by_tag_name('h4').text

    assert 'правительство' in head_feedback, 'У правительства обед, обращение не зарегистрировано'


@pytest.mark.positive_transfer_lines_fio
def test_positive_transfer_lines_fio(browser):

    browser.get(link)
    browser.implicitly_wait(5)

    lastname_field = browser.find_element_by_id("fullname-surname")
    lastname_field.send_keys(lastname)

    name_field = browser.find_element_by_id("fullname-name")
    name_field.send_keys(name)

    patronymic_field = browser.find_element_by_id("fullname-patronymic")
    patronymic_field.send_keys(patronymic)

    fullname_field = browser.find_element_by_id('fullname')
    fullname_text = fullname_field.get_attribute('value')

    assert fullname_text == f'{lastname} {name}', 'Поле полного ФИО не совпадает со строчными полями'


@pytest.mark.positive_transfer_lines_address
def test_positive_transfer_lines_address(browser):

    browser.get(link)
    browser.implicitly_wait(5)
    city_field = browser.find_element_by_id('address-city')
    city_field.send_keys(city)

    street_field = browser.find_element_by_id('address-street')
    street_field.send_keys(street)

    building_field = browser.find_element_by_id('address-house')
    building_field.send_keys(building)

    appartment_field = browser.find_element_by_id('address-flat')
    appartment_field.send_keys(appartment)

    next_field = browser.find_element_by_id("message")
    next_field.send_keys('')

    fulladdress_field = browser.find_element_by_id('address')
    fulladdress_text = fulladdress_field.get_attribute('value')

    assert fulladdress_text == f'{city}, {street}, {building}, {appartment}', 'Поле полного адреса не совпадает со ' \
                                                                              'строчными полями'
