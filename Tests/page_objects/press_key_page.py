from Tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys

pressKey_tab = 'keypresses-header'
pressKey_content = 'keypresses-content'
input_field = 'target'
result = 'keyPressResult'

def click_key_presses_tab(driver_instance):
    elem = driver_instance.find_element_by_id(pressKey_tab)
    elem.click()

def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, pressKey_content)
    return elem.is_displayed()

def press_key(driver_instance):
        input = driver_instance.find_element_by_id(input_field)
        res = driver_instance.find_element_by_id(result)
        input.click()
        input.send_keys(Keys.ENTER)
        elem = wait_for_visibility_of_element(driver_instance, result)
        mess = elem.text
        message_text = 'You entered: ENTER'
        if mess == message_text:
            return True
        else:
            return False
