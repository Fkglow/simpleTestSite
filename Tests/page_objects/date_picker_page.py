from Tests.helpers.support_functions import *


date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_picker = "//*[@id='datepicker-content']/div/input"


def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()


def date_picker_is_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()


def choose_correct_date(driver_instance):
    elem = driver_instance.find_element_by_xpath(date_picker)
    elem.click()
    elem.send_keys('2020-02-02')
    elem.click()
    value = '2020-02-02'
    if value == elem.get_attribute("value"):
        return True
    else:
        return False


def choose_incorrect_date(driver_instance):
    elem = driver_instance.find_element_by_xpath(date_picker)
    elem.send_keys('2044-44-44')
    value = '2044-44-44'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True




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


