*** Settings ***
Documentation  Registration (Page Object in Robot Framework)
Library  SeleniumLibrary
Variables	../resources/page-object/test-data/TestData.py
Resource  ../resources/page-object/keyword-defination-files/RegisterPage.robot
Resource  ../resources/page-object/keyword-defination-files/RegisterConfirmationPage.robot
Resource  ../resources/page-object/keyword-defination-files/Common.robot
Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

*** Test Cases ***
001 Rejestracja nowego użytkownika w systemie
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


002 Rejestracja nowego użytkownika w systemie z niepoprawnym adresem email
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to registration page
    Input Invalid Email
   	Input Username
   	Input Password
    Input First name
    Input Last name
   	Assert Register With Invalid Email


003 Rejestracja nowego użytkownika w systemie z zajętą nazwą użytkownika
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to registration page
    Input Email
   	Input already in use Login
   	Input Password
    Input First name
    Input Last name
    Register button
   	Assert Register with username already in use

004 Rejestracja nowego użytkownika w systemie z zajętym adresem email
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to registration page
    Input already in use Email
   	Input Username
   	Input Password
    Input First name
    Input Last name
    Register button
   	Assert Register with email already in use

