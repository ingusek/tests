*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary
Variables  ../locators/Locators.py

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
