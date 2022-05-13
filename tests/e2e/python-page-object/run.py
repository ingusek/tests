import unittest
from tests.RegistrationTest import RegistrationTest
from tests.LoginTest import LoginTest
from tests.LogoutTest import LogOutTest
from tests.AccountTest import AccountTest
from tests.Page2Test import Page2Test
from tests.TodoTest import TodoTest

# Pobierz testy, które chcesz uruchomić
registration_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
logout_test = unittest.TestLoader().loadTestsFromTestCase(LogOutTest)
my_account_test = unittest.TestLoader().loadTestsFromTestCase(AccountTest)
page2_test = unittest.TestLoader().loadTestsFromTestCase(Page2Test)
todo_page = unittest.TestLoader().loadTestsFromTestCase(TodoTest);

# Lista testów do uruchomienia
tests_for_run = [
    # registration_test,
    # login_test,
    # logout_test,
    # my_account_test
    # page2_test
    todo_page
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)
unittest.TextTestRunner().run(test_suite)
