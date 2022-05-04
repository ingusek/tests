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
018 Otrzymanie emaila z linkiem do resetu hasła
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
    Click forgot password
   	Input email in field find element
    Click request new password
    Assert request new email
	Check email box 
    Open email password reset
    Assert password reset

***Keywords***