*** Settings ***
Library  SeleniumLibrary
Variables  ../locators/Locators.py
Variables  ../test-data/TestData.py

*** Keywords ***
Verify Welcome Text after register is Visible
    Wait Until Page Contains    ${ExpectedWelcomeAfterRegisterText}  timeout=5
    ${Welcome}=	Get Text	${WelcomeAfterRegisterText}
    Should Be Equal	${Welcome}	${ExpectedWelcomeAfterRegisterText}

