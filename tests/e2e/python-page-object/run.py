import unittest
from tests.RegistrationTest import RegistrationTest
from tests.LoginTest import LoginTest
from tests.LogOutTest import LogOutTest
from tests.AccountTest import AccountTest

# Pobierz testy, które chcesz uruchomić
registration_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
logout_test = unittest.TestLoader().loadTestsFromTestCase(LogOutTest)
my_account_test = unittest.TestLoader().loadTestsFromTestCase(AccountTest)

# Lista testów do uruchomienia
tests_for_run = [
    # registration_test,
    # login_test,
    # logout_test,
    my_account_test
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)
unittest.TextTestRunner().run(test_suite)
