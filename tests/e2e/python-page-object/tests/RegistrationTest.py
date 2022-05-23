from tests.BaseTest import BaseTest
from tests.TestData import Settings

class RegistrationTest(BaseTest):

    """
    ID: 001
    """
    def test_registration_success(self):
        home_page = self.home_page

        registration_page = home_page.click_sign_up()
        registration_page.fill_in_registration_form(
            self.test_data.email,
            self.test_data.first_name,
            self.test_data.last_name,
            self.test_data.password,
            self.test_data.login
        )

        register_confirmation_page = registration_page.register()
        register_confirmation_page.wait_for_registration_success()

        self.assertEqual(register_confirmation_page.get_info_box().text, 
            "You are successfully registered.")

        emial_page = home_page.open_email_box(Settings.MAILHOG_URL)

        login_page = emial_page.confirm_registration()
        login_page.wait_for_login_page()
        
        confirmation_text = login_page.get_confirm_regitration_text()
        self.assertEqual(confirmation_text, 'You are now verified. Please use your username/password to login.')

    """
    ID: 002
    """
    def test_registeration_with_invalid_email(self):
        home_page = self.home_page

        registration_page = home_page.click_sign_up()
        registration_page.fill_in_registration_form(
            self.test_data.invalid.email,
            self.test_data.first_name,
            self.test_data.last_name,
            self.test_data.password,
            self.test_data.login
        )
        registration_page.register()

        is_button_enabled = registration_page.is_button_enabled()
        self.assertFalse(is_button_enabled)

    """
    ID: 003
    """
    def test_registeration_with_username_already_use(self):
        home_page = self.home_page

        registration_page = home_page.click_sign_up()
        registration_page.fill_in_registration_form(
            self.test_data.email,
            self.test_data.first_name,
            self.test_data.last_name,
            self.test_data.password,
            self.test_data.in_use_login,
        )
        registration_page.register()

        is_button_enabled = registration_page.is_button_enabled()

        self.assertTrue(is_button_enabled)
        error_text = registration_page.get_danger_message()
        expectedError_text = "Username is already in use."
        self.assertEqual(error_text, expectedError_text)

    """
    ID: 004
    """
    def test_registeration_with_email_already_use(self):
        home_page = self.home_page

        registration_page = home_page.click_sign_up()
        registration_page.fill_in_registration_form(
            self.test_data.in_use_email,
            self.test_data.first_name,
            self.test_data.last_name,
            self.test_data.password,
            self.test_data.login,
        )
        registration_page.register()

        is_button_enabled = registration_page.is_button_enabled()

        self.assertTrue(is_button_enabled)
        error_text = registration_page.get_danger_message()
        self.assertEqual(error_text, "Email is already in use.")
