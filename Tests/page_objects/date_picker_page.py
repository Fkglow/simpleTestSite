from Tests.helpers.support_functions import *
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_picker = "//*[@id='datepicker-content']/div/input"

def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()

def date_picker_is_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()

def choose_date(driver_instance):

    elem = driver_instance.find_element_by_xpath(date_picker)
    elem.click()
    elem.send_keys('01012020')
    elem.click()
    sleep(4)
    value = '01.01.2020'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False

    #
    # invalid_message = wait_for_visibility_of_element(driver_instance, invalid_credentials_message).text
    # message = 'Invalid credentials'
    # if message == invalid_message:
    #     return True
    # else:
    #     return False

    # driver_instance.switch_to_frame()
    # elem = driver_instance.find_element_by_xpath(date_picker)
    # elem.click()
    # sleep(3)
    # elem.send_keys('102020')
    # sleep(3)
    # value = '10.10.2020'
    # if value == elem.get_attribute("value"):
    #     return True
    # else:
    #     return False


