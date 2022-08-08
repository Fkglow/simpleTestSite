from Tests.helpers.support_functions import *
from time import sleep

form_tab = 'form-header'
form_content = 'form-content'
first_name = 'fname'
last_name = 'lname'
submit_button = 'formSubmitButton'

def click_form_tab(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_tab)
    elem.click()

def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_content)
    return elem.is_displayed()

def form_submitted_succesfully(driver_instance):
    fname = driver_instance.find_element_by_id(first_name)
    lname = driver_instance.find_element_by_id(last_name)
    fname.send_keys('Jacek')
    lname.send_keys('Placek')
    button = driver_instance.find_element_by_id(submit_button)
    button.click()
    driver_instance.switch_to_alert