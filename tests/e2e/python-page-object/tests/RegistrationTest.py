from tests.BaseTest import BaseTest
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
        # 5. Verify
        self.assertEqual(register_confirmation_page.get_info_box().text, 
            "You are successfully registered.")
