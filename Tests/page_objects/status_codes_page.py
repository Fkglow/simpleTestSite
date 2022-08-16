import requests
from Tests.helpers.support_functions import *

status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
ok_status = '200siteAnchor'
proxy = '305siteAnchor'
not_found = '404siteAnchor'
internal_server_error = '500siteAnchor'


def click_status_codes_tab(driver_instance):
    elem = driver_instance.find_element_by_id(status_codes_tab)
    elem.click()


def status_codes_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, status_codes_content)
    return elem.is_displayed()


def status_code_200(driver_instance):
    elem = driver_instance.find_element_by_id(ok_status)
    url = elem.get_attribute('href')
    req = requests.get(url)
    code = req.status_code
    try:
        if code == 200:
            return True
        else:
            return False
    except ConnectionError:
        print('Connection Error')


def status_code_305(driver_instance):
    elem = driver_instance.find_element_by_id(proxy)
    url = elem.get_attribute('href')
    req = requests.get(url)
    code = req.status_code
    try:
        if code == 305:
            return True
        else:
            return False
    except ConnectionError:
        print('Connection Error')


def status_code_404(driver_instance):
    elem = driver_instance.find_element_by_id(not_found)
    url = elem.get_attribute('href')
    req = requests.get(url)
    code = req.status_code
    try:
        if code == 404:
            return True
        else:
            return False
    except ConnectionError:
        print('Connection Error')


def status_code_500(driver_instance):
    elem = driver_instance.find_element_by_id(internal_server_error)
    url = elem.get_attribute('href')
    req = requests.get(url)
    code = req.status_code
    try:
        if code == 500:
            return True
        else:
            return False
    except ConnectionError:
        print('Connection Error')
