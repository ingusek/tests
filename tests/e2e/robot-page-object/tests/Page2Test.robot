*** Settings ***
Documentation  Registration (Page Object in Robot Framework)
Library  SeleniumLibrary
Variables	../resources/page-object/test-data/TestData.py
Resource  	../resources/page-object/keyword-defination-files/LoginPage.robot
Resource  	../resources/page-object/keyword-defination-files/Page2Page.robot
Resource  	../resources/page-object/keyword-defination-files/Common.robot
Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

*** Test Cases ***
017 Wyświetlenie informacji z podstrony Page2
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login
	Open Sample Page menu   
	Open Page2 menu
	Assert Page2
