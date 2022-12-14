from Tests.helpers.support_functions import *

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


def add_first_name(driver_instance):
    fname = driver_instance.find_element_by_id(first_name)
    fname.send_keys('Jacek')


def add_last_name(driver_instance):
    lname = driver_instance.find_element_by_id(last_name)
    lname.send_keys('Placek')


def submit_form(driver_instance):
    button = driver_instance.find_element_by_id(submit_button)
    button.click()


def success_alert_visible(driver_instance):
    try:
        success_alert = wait_for_alert_to_be_presented(driver_instance)
        value = 'success'
        if success_alert.text == value:
            return True
    except NoAlertPresentException:
        return False


def close_success_alert(driver_instance):
        success_alert = wait_for_alert_to_be_presented(driver_instance)
        success_alert.accept()
        try:
            driver_instance.switch_to.alert()
            return True
        except NoAlertPresentException:
            return False


def empty_inputs_validation(driver_instance):
    fname = driver_instance.find_element_by_id(first_name)
    validation_mess = fname.get_attribute('validationMessage')
    value = 'Please fill out this field.'
    if validation_mess == value:
        return True
    else:
        return False



