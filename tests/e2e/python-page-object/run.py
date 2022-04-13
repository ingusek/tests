import unittest
from tests.RegistrationTest import RegistrationTest

# Pobierz testy, które chcesz uruchomić
registration_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)

# Lista testów do uruchomienia
tests_for_run = [
    registration_test,
    # kolejny test
    # ...
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)
unittest.TextTestRunner().run(test_suite)
