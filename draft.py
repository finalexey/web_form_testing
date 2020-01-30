import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://hflabs.github.io/suggestions-demo/"
lastname = 'Иванов'
name = 'Иван'
patronymic = 'Иванович'
email = 'aa@mail.ru'
message = 'abc'

browser = webdriver.Chrome()
browser.get(link)

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



# head_feedback = browser.find_element_by_tag_name('h4').text
# if 'обед' in browser.find_element_by_tag_name('h4').text:
#     print('Обращение не принято - обед', head_feedback)
# elif 'правительство' in browser.find_element_by_tag_name('h4').text:
#     print('Обращение отправлено в ненастоящее правительство', head_feedback)

head_feedback1 = browser.find_element_by_tag_name('h4').text

print('len head =', len(head_feedback1), len(head_feedback1) > 0)
# head_feedback_test = WebDriverWait(browser, 5).until(head_feedback)
# print('TITLE', head_feedback_test)


send_button = browser.find_element_by_class_name("btn-primary")
send_button.click()
time.sleep(2)

# head_feedback_wait = browser.find_element(By.TAG_NAME, 'h4').text
# head_feedback = browser.find_element_by_tag_name('h4').text

# if WebDriverWait(browser, 5).until(
#     EC.text_to_be_present_in_element((By.TAG_NAME, 'h4'), 'Это не настоящее правительство :-(')):
#     head_feedback = browser.find_element_by_tag_name('h4').text


time.sleep(3)
head_feedback2 = browser.find_element_by_tag_name('h4').text
print('len head =', len(head_feedback2), len(head_feedback2) > 0)
# browser.implicitly_wait(3)
# confirm_button = browser.find_element_by_class_name("btn-default")
# confirm_button.click()
# time.sleep(3)
browser.quit()
