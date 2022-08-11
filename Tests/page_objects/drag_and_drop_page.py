import time
from Tests.helpers.support_functions import *
from selenium.webdriver.common.action_chains import ActionChains


drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
columns = 'columns'
drag_elem_A = 'column-a'
drag_elem_B = 'column-b'

def click_drag_and_drop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()

def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, drag_and_drop_content)
    return elem.is_displayed()

def drag_and_drop_element_A(driver_instance):
    source = driver_instance.find_element_by_id(drag_elem_A)
    target = driver_instance.find_element_by_id(drag_elem_B)
    driver_instance.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    js_d_d = open(r'/home/antoni/Pulpit/EWA/simpleTestSite/Tests/helpers/drag_drop.js', 'r').read()
    driver_instance.execute_script(js_d_d, source, target)

def check_result_first_switch(driver_instance):
    source = driver_instance.find_element_by_id(drag_elem_A)
    col_A = source.text
    value = 'B'
    if value == col_A:
        return True
    else:
        return False

def check_result_second_switch(driver_instance):
    source = driver_instance.find_element_by_id(drag_elem_A)
    col_A = source.text
    value = 'A'
    if value == col_A:
        return True
    else:
        return False