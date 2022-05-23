***Settings***
Library	SeleniumLibrary
Library    FakerLibrary
# Library	/app/library/ChromeConfiguration.py
# Library	XvfbRobot

Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${USERNAME}		%{LOGIN}
${PASSWORD}		%{PASSWORD}
${TASK}			Test

***Test Cases***
010 Sprawdzanie funkcjonalności Todo-dostęp do zakładki Todo tylko po zalogowaniu
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login
	Open page Todo

011 Sprawdzanie funkcjonalności Todo-dodanie nowego wpisu do listy Todo
    ${entry}=    FakerLibrary.Name
    Set Suite Variable  ${entry}
	Open main page
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
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login
	Open page Todo
    Add a new entry to the list Todo
    Remove item from list Pending
    Assert removing item from list Pending

016 Umieszczenie na liście Pending pozycji o tej samej nazwie
    ${entry}=    FakerLibrary.Name
    Set Suite Variable  ${entry}
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login
	Open page Todo
    Add a new entry to the list Todo
	Add a new entry to the list Todo


***Keywords***

Suite shutdown
	Sleep	10s
	Close All Browsers

Open main page
   	Open browser    ${APP_URL}   ${BROWSER}
   	Title Should Be    Home | Frontend

Go to login page
	Click Element       //a[contains(text(),'Login')]
	Sleep	1s

Input Username
	Input Text	input-username	${USERNAME}

Input Password
	Input Text	input-password	${PASSWORD}

Login button
	Click Element       //button[@type="submit"]
	Sleep	1s

Assert Login
	${welcome}=	Get Text	//a[@href="/account"]
	Should Be Equal	${welcome}	Welcome, Jan

Open page Todo
     Click Element       //a[contains(text(),'Todo')]

Assert Todo
	${Todo App}=	Get Text	//h1[@class="page-title"]
	Should Be Equal	${Todo App}	Todo App

Add a new entry to the list Todo
    Input Text	input-name	${entry}
    Click Element       //button[contains(text(),'Add')]
	Sleep	1s

Assert a new entry to the list Todo
	${new_entry}=	Get Text	//div[@data-name="todo-pending-name-0"]//span
	Should Be Equal	${new_entry}	${entry}

Remove item from list Pending 
    Click Element       //div[@data-name="todo-pending-list-0"]//button
	Sleep	1s  

Assert removing item from list Pending
	Page Should Not Contain Element	//div[@data-name="todo-pending-name-0"]//span[contains(text(),'${entry}')]

