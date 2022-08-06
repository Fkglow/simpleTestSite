from Tests.helpers.support_functions import *
from time import sleep

basic_auth_tab = 'basicauth-header'
basic_auth_content = 'basicauth-content'
username_input = 'ba_username'
password_input = 'ba_password'
login_button = "//*[@id='content']/button"
invalid_credentials_message = 'loginFormMessage'


def click_basic_auth_page(driver_instance):
    elem = driver_instance.find_element_by_id(basic_auth_tab)
    elem.click()

def basic_auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, basic_auth_content)
    return elem.is_displayed()

def basic_auth_correct_credentials(driver_instance):
    username = driver_instance.find_element_by_id(username_input)
    username.send_keys('admin')
    password = driver_instance.find_element_by_id(password_input)
    password.send_keys('admin')
    login = driver_instance.find_element_by_xpath(login_button)
    login.click()

def basic_auth_incorrect_username(driver_intance):
    username = driver_instance.find_element_by_id(username_input)
    username.send_keys('tester')
    password = driver_instance.find_element_by_id(password_input)
    password.send_keys('admin')
    login = driver_instance.find_element_by_xpath(login_button)
    login.click()
    elem = wait_for_visibility_of_element(driver_intance, invalid_credentials_message)
    sleep(3)
    return elem.is_displayed()

def basic_auth_incorrect_password(driver_intance):
    username = driver_instance.find_element_by_id(username_input)
    username.send_keys('admin')
    password = driver_instance.find_element_by_id(password_input)
    password.send_keys('testento')
    login = driver_instance.find_element_by_xpath(login_button)
    login.click()
    elem = wait_for_visibility_of_element(driver_intance, invalid_credentials_message)
    sleep(3)
    return elem.is_displayed()


