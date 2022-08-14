import time

from Tests.helpers.support_functions import *

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
button1 = 'simpleButton1'
button2 = 'simpleButton2'
message = 'whichButtonIsClickedMessage'

def click_iframe_tab(driver_instance):
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()

def iframe_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, iframe_content)
    return elem.is_displayed()

def click_button1(driver_instance):
    iframe = driver_instance.find_element_by_tag_name('iframe')
    driver_instance.switch_to.frame(iframe)
    button_1 = wait_for_visibility_of_element(driver_instance, button1)
    button_1.location_once_scrolled_into_view
    button_1.click()
    info = 'Button 1 was clicked!'
    which_button_message = wait_for_visibility_of_element(driver_instance, message)
    if which_button_message.text == info:
        return True
    else:
        return False

def click_button2(driver_instance):
    iframe = driver_instance.find_element_by_tag_name('iframe')
    driver_instance.switch_to.frame(iframe)
    button_2 = wait_for_visibility_of_element(driver_instance, button2)
    button_2.location_once_scrolled_into_view
    button_2.click()
    info = 'Button 2 was clicked!'
    which_button_message = wait_for_visibility_of_element(driver_instance, message)
    if which_button_message.text == info:
        return True
    else:
        return False



