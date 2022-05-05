*** Settings ***
Library  SeleniumLibrary
Variables  ../locators/Locators.py

*** Keywords ***
Opening Browser
    [Arguments]  ${site_url}  ${browser}
    Open Browser  ${site_url}  ${browser}
    Wait Until Element Is Visible  ${SingUpButton}  timeout=5
  	Title Should Be    Home | Frontend

Go to login page
	Click Element       ${LoginButton}

Go to registration page
    Click Element       ${SingUpButton}

Logout button
    Click Element       ${LogoutButton}
	Sleep	1s

Assert Logout
	Element Should Be Visible	${LoginButton}

Suite shutdown
	Close All Browsers
