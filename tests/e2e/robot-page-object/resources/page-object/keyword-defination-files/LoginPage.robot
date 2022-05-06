*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary
Variables  ../locators/Locators.py
Variables  ../test-data/TestData.py

*** Keywords ***
Input Username
	Input Text	${LoginUsernameInput}	${USERNAME}

Input Invalid Username
	Input Text	${LoginUsernameInput}	${INVALID_USERNAME}

Input Password
	Input Text	${LoginPasswordInput}	${PASSWORD}

Input Invalid Password
	Input Text	${LoginPasswordInput}	${INVALID_PASSWORD}

Login button
	Click Element       ${SubmitLoginButton}
	Sleep	1s

Click forgot password
    Click Element       ${ResetPasswordButton}

Assert Login
	${welcome}=	Get Text	${GoToAccountPageButton}
	Should Be Equal	${welcome}	Welcome, Jan

Assert Login with invalid password
	${message}=	Get Text	${LoginErrorMessage}
	Should Be Equal	${message}      Your username or password is incorrect. Please try again.

Assert Login with invalid username
	${message}=	Get Text	${LoginErrorMessage}
	Should Be Equal	${message}      Your username or password is incorrect.	

