from tests.BaseTest import BaseTest
from tests.TestData import Settings
from time import sleep

class RegistrationTest(BaseTest):
    """
    Registration Tests
    """
    def verify_error_messages(self, errors):
        pass

    def test_registration_success(self):
        """
        TC 001 : User does not fill the name field
        """
        home_page = self.home_page
        # 1. Click Sign Up
        registration_page = home_page.click_sign_up()
 
        # 2. Fill registration form
        registration_page.fill_in_registration_form(
            self.test_data.email,
            self.test_data.first_name,
            self.test_data.last_name,
            self.test_data.password,
            self.test_data.login
        )

        # 4. Register
        register_confirmation_page = registration_page.register()
        register_confirmation_page.wait_for_regitration_success()
        # 5. Verify
        self.assertEqual(register_confirmation_page.get_info_box().text, 
            "You are successfully registered.")

        # 6. Confirm registration 
        emial_page = home_page.open_email_box(Settings.MAILHOG_URL)
        
        # 7. Verify confirmation
        login_page = emial_page.confirm_registration()
        login_page.wait_for_login_page()
        
        confirmation_text = login_page.get_confirm_regitration_text()
        self.assertEqual(confirmation_text, 'You are now verified. Please use your username/password to login.')


    def test_registeration_with_invalid_email(self):
        """
        TC 001 : User does not fill the name field
        """
        home_page = self.home_page
        # 1. Click Sign Up
        registration_page = home_page.click_sign_up()
 
        # 2. Fill registration form
        registration_page.fill_in_registration_form(
            self.test_data.invalid.email,
            self.test_data.first_name,
            self.test_data.last_name,
            self.test_data.password,
            self.test_data.login
        )

        # 4. Register
        registration_page.register()
        is_button_enabled = registration_page.is_button_enabled()

        # 5. Verify
        self.assertFalse(is_button_enabled)
