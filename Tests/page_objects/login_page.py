import time

from Tests.helpers.support_functions import *

success_message = 'loggedInMessage'
return_button = 'retrun button'
main_page_header = 'test-header'

def login_success_message_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, success_message)
    return elem.is_displayed()

def return_to_main_page(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, return_button)
    elem.click()
    elem2 = wait_for_visibility_of_element(driver_instance,main_page_header)
    return elem2.is_displayed()
