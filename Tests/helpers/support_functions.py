from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element(driver_instance, id):
    element = driver_instance.find_element_by_xpath(id)
    hover = ActionChains(driver_instance).move_to_element(element)
    hover.perform()


def wait_for_visibility_of_element(driver_instance, id, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element(inv_driver_instance, xpath, time_to_wait=8):
    inv_element = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element((By.XPATH, xpath)))
    return inv_element

def wait_for_element_to_be_clickable(click_driver_instance, id, time_to_wait=5):
    clickable_elem = WebDriverWait(click_driver_instance, time_to_wait).until(EC.element_to_be_clickable((By.ID, id)))
    return clickable_elem

def wait_for_alert_to_be_presented(driver_instance, time_to_wait=5):
    alert = WebDriverWait(driver_instance, time_to_wait).until(EC.alert_is_present())
    return alert