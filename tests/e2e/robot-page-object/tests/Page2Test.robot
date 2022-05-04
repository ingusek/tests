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
017 Wyświetlenie informacji z podstrony Page2
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login
	Open Sample Page menu   
	Open Page2 menu
	Assert Page2

***Keywords***