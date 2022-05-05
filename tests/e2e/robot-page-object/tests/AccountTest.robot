*** Settings ***
Documentation  Registration (Page Object in Robot Framework)
Library  SeleniumLibrary
Variables	../resources/page-object/test-data/TestData.py
Resource  	../resources/page-object/keyword-defination-files/LoginPage.robot
Resource  	../resources/page-object/keyword-defination-files/AccountPage.robot
Resource  	../resources/page-object/keyword-defination-files/Common.robot
Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

*** Test Cases ***
008 Sprawdzanie danych użytkownika na stronie http://localhost/ po zalogowaniu się
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
   	Input Username
   	Input Password
   	Login button
    Open page Account   
	Assert Username
    Assert name
    Assert email
