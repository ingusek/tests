*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary
Variables  ../locators/Locators.py
Variables  ../test-data/TestData.py

*** Keywords ***
Input Email
    ${EMAIL}=    FakerLibrary.Email
    Input Text  ${RegisterEmailInput}  ${EMAIL}

Input Username
    ${FIRST_NAME}=    FakerLibrary.First_Name
    Input Text  ${RegisterUsernameInput}  ${FIRST_NAME}

Input Password
    ${PASSWORD}=    FakerLibrary.Password
    Input Text  ${RegisterPasswordInput}  ${PASSWORD}

Input First name
    ${FIRST_NAME}=    FakerLibrary.First_Name
    Input Text  ${RegisterFirstNameInput}  ${FIRST_NAME}

Input Last name
    ${LAST_NAME}=    FakerLibrary.Last_Name
    Input Text  ${RegisterLastNameInput}  ${LAST_NAME}

Click Register
    Click Element  ${RegisterButton}

Input Invalid Email
	Input Text	${RegisterEmailInput}	${InvalidEmail}

Assert Register With Invalid Email
	Element Should Be Disabled	${RegisterButton}

Input already in use Login
    Input Text	${RegisterUsernameInput}	${LOGIN}

Register button
    Element Should Be Enabled	${RegisterButton}
	Click Element       ${RegisterButton}
	Sleep	1s

Assert Register with username already in use
	${message}=	Get Text		${RegisterErrorMessage}
    Should Be Equal	${message}	Username is already in use.

Assert Register with email already in use
	Element Should Be Enabled	${RegisterButton}
