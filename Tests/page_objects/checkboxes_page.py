from Tests.helpers.support_functions import *


checkbox_tab = 'checkbox-header'
all_checkboxes = 'checkboxes'
checkbox1 = "//*[@id='checkboxes']/input[1]"
checkbox2 = "//*[@id='checkboxes']/input[2]"


def checkboxes_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, all_checkboxes)
    return elem.is_displayed()


def click_checkboxes_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, checkbox_tab)
    elem = driver_instance.find_element_by_id(checkbox_tab)
    elem.click()


def click_checkboxes(driver_instance):
    elem1 = driver_instance.find_element_by_xpath(checkbox1)
    elem1.click()
    elem2 = driver_instance.find_element_by_xpath(checkbox2)
    elem2.click()
