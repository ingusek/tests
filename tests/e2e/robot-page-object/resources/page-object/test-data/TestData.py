import os

BROWSER	= "Chrome"
APP_URL	= os.environ['APP_URL']
MAILHOG_URL = os.environ['MAILHOG_URL']
LOGIN =  os.environ['LOGIN']
USERNAME = os.environ['LOGIN']
INVALID_USERNAME = "błedny login"
PASSWORD = os.environ['PASSWORD']
INVALID_PASSWORD = "błędne hasło"
EMAIL = os.environ['EMAIL']   

ExpectedWelcomeAfterRegisterText = 'You are successfully registered.'
InvalidEmail =	'ji8989898uii'

MyAccountExpectedUsername = 'ingusek'
MyAccountExpectedName = 'Jan, Kowalski'
MyAccountExpectedEmail = 'ingus@wp.pl'
