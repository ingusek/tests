import os
from faker import Faker

class Settings:
    MAILHOG_URL = os.environ['MAILHOG_URL']

class InvalidTestData:
    """
    Invalid Test Data
    """
    def __init__(self) -> None:
        self.email = 'ji8989898uii'
        self.password = 'abcdefg'
        self.login = 'xyzxyz'

class TestData:
    """
    Test Data generator
    """
    def __init__(self):
        self.fake = Faker()
        self.email = self.fake.email()
        self.last_name = self.fake.last_name()
        self.first_name = self.fake.first_name()
        self.login = self.fake.simple_profile()['username']
        self.password = self.fake.password()
        self.invalid = InvalidTestData()
        self.in_use_login =  os.environ['LOGIN']
        self.in_use_email =  os.environ['EMAIL']
        self.in_use_password = os.environ['PASSWORD']

    def get_item_name(self, prefix):
        return prefix + '_' + self.fake.name()
