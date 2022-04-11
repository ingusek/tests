*** Settings ***
Library  SeleniumLibrary
Variables  ../locators/Locators.py

*** Keywords ***
Opening Browser
    [Arguments]  ${site_url}  ${browser}
    Open Browser  ${site_url}  ${browser}
    Wait Until Element Is Visible  ${SingUpButton}  timeout=5
  	Title Should Be    Home | Frontend

Go to registration page
    Click Element       ${SingUpButton}

Suite shutdown
	Close All Browsers
