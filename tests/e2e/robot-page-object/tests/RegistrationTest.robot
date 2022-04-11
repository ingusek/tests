*** Settings ***
Documentation  Registration (Page Object in Robot Framework)
Library  SeleniumLibrary
Resource  ../resources/page-object/keyword-defination-files/RegisterPage.robot
Resource  ../resources/page-object/keyword-defination-files/RegisterConfirmationPage.robot
Resource  ../resources/page-object/keyword-defination-files/Common.robot
Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

*** Variables ***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}

*** Test Cases ***
Verify Registration
    [documentation]  This test case verifies that the user is able to successfully register
    [tags]  Smoke
    Opening Browser  ${APP_URL}  ${BROWSER}
    Go to registration page
    Input Email
    Input Username
    Input Password
    Input First name
    Input Last name
    Click Register
    Verify Welcome Text after register is Visible
    Close Browser

*** Keywords ***
