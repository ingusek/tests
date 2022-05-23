*** Settings ***
Documentation  Registration (Page Object in Robot Framework)
Library  SeleniumLibrary
Variables	../resources/page-object/test-data/TestData.py
Resource  	../resources/page-object/keyword-defination-files/LoginPage.robot
Resource  	../resources/page-object/keyword-defination-files/TodoPage.robot
Resource  	../resources/page-object/keyword-defination-files/Common.robot
Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

*** Test Cases ***
010 Sprawdzanie funkcjonalności Todo-dostęp do zakładki Todo tylko po zalogowaniu
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Username
  Input Password
  Login button
  Assert Login
	Open page Todo

011 Sprawdzanie funkcjonalności Todo-dodanie nowego wpisu do listy Todo
  ${entry}=    FakerLibrary.Name
  Set Suite Variable  ${entry}
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Username
  Input Password
  Login button
  Assert Login
	Open page Todo
  Add a new entry to the list Todo

012 Sprawdzanie funkcjonalności Todo-usunięcie pozycji z listy Pending
  ${entry}=    FakerLibrary.Name
  Set Suite Variable  ${entry}
  Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Username
  Input Password
  Login button
  Assert Login
	Open page Todo
  Add a new entry to the list Todo
  Remove item from list Pending
  Assert removing item from list Pending

013 Przeniesienie wpisu z listy pending do ongoing
  ${entry}=    FakerLibrary.Name
  Set Suite Variable  ${entry}
  Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Username
  Input Password
  Login button
  Assert Login
	Open page Todo
  Add a new entry to the list Todo
	Move entry from pending to ongoing
	Assert move item to the list of ongoing

014 Przeniesienie wpisu z listy ongoing do completed
  ${entry}=    FakerLibrary.Name
  Set Suite Variable  ${entry}
  Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Username
  Input Password
  Login button
  Assert Login
	Open page Todo
  Add a new entry to the list Todo
	Move entry from pending to ongoing
	Move entry from ongiong to completed
	Assert move item to the list of completed

015 Umieszczenie na liście Pending pozycji o tej samej nazwie
  ${entry}=    FakerLibrary.Name
  Set Suite Variable  ${entry}
	Opening Browser  ${APP_URL}  ${BROWSER}
	Go to login page
  Input Username
  Input Password
  Login button
  Assert Login
	Open page Todo
  Add a new entry to the list Todo
	Add a new entry to the list Todo
