import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from Tests.page_objects import main_page
from Tests.page_objects import checkboxes_page
from Tests.page_objects import hovers_page
from Tests.page_objects import users_page
from Tests.page_objects import inputs_page
from Tests.page_objects import dropdowns_page
from Tests.page_objects import add_remove_page
# from Tests.page_objects import date_picker_page
from Tests.page_objects import basic_auth_page
from Tests.page_objects import login_page
from Tests.page_objects import form_page
from Tests.page_objects import press_key_page
from Tests.page_objects import drag_and_drop_page

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checbkoxes(self.driver)
    #
    # def test3_date_picker(self):
    #     date_picker_page.click_date_picker_tab(self.driver)
    #     self.assertTrue(date_picker_page.date_picker_is_visible(self.driver))
    #     self.assertTrue(date_picker_page.choose_date(self.driver))


    def test4_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_gentleman_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test5_inputs_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test6_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test7_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys(self.driver))

    def test8_basic_auth_happy_path(self):
        basic_auth_page.click_basic_auth_page(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.basic_auth_correct_credentials(self.driver)
        self.assertTrue(login_page.login_success_message_displayed(self.driver))

    def test9_basic_auth_incorrect_username(self):
        basic_auth_page.click_basic_auth_page(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        self.assertTrue(basic_auth_page.basic_auth_incorrect_username(self.driver))

    def test10_basic_auth_incorrect_password(self):
        basic_auth_page.click_basic_auth_page(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        self.assertTrue(basic_auth_page.basic_auth_incorrect_password(self.driver))

    def test11_basic_auth_return_to_main_page(self):
        basic_auth_page.click_basic_auth_page(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.basic_auth_correct_credentials(self.driver)
        self.assertTrue(login_page.login_success_message_displayed(self.driver))
        self.assertTrue(login_page.return_to_main_page(self.driver))

    def test12_form_success(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        form_page.add_first_name(self.driver)
        form_page.add_last_name(self.driver)
        form_page.submit_form(self.driver)
        self.assertTrue(form_page.success_alert_visible(self.driver))
        self.assertFalse(form_page.close_success_alert(self.driver))

    def test13_dropdown_select(self):
        dropdowns_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdowns_page.dropdown_content_visible(self.driver))
        dropdowns_page.get_first_dropdown_value(self.driver)

    def test14_key_presses(self):
        press_key_page.click_key_presses_tab(self.driver)
        self.assertTrue(press_key_page.key_presses_content_visible(self.driver))
        self.assertTrue(press_key_page.press_key(self.driver))

    def test15_drag_and_drop(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visible(self.driver))
        drag_and_drop_page.drag_and_drop_element_A(self.driver)
        self.assertTrue(drag_and_drop_page.check_result_first_switch(self.driver))
        drag_and_drop_page.drag_and_drop_element_A(self.driver)
        self.assertTrue(drag_and_drop_page.check_result_second_switch(self.driver))

    def test16_add_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test17_delete_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_is_invisible(self.driver))


if __name__ == '__main__':
    unittest.main()