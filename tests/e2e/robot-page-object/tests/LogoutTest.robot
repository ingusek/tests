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
009 Sprawdzanie czy da się wylogować ze strony http://localhost/
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
   	Input Username
   	Input Password
   	Login button
    Logout button
   	Assert Logout

***Keywords***