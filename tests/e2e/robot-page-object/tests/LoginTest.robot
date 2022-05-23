*** Settings ***
Documentation  Registration (Page Object in Robot Framework)
Library  SeleniumLibrary
Variables	../resources/page-object/test-data/TestData.py
Resource  	../resources/page-object/keyword-defination-files/LoginPage.robot
Resource  	../resources/page-object/keyword-defination-files/Common.robot
Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

*** Test Cases ***
005 Logowanie się na stronie http://localhost/login przy użyciu poprawnego loginu i poprawnego hasła
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Username
  Input Password
  Login button
  Assert Login

006 Logowanie się na stronie http://localhost/login przy użyciu poprawnego loginu i niepoprawnego hasła.
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Username
  Input Invalid Password
  Login button
  Assert Login with invalid password

007 Logowanie się na stronie http://localhost/login przy użyciu niepoprawnego loginu i poprawnego hasła.
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Invalid Username
  Input Password
  Login button
  Assert Login with invalid username
