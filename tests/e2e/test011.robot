***Settings***
Library	SeleniumLibrary
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
Sprawdzanie funkcjonalności Todo-dostęp do zakładki Todo tylko po zalogowaniu
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login
	Open page Todo

***Keywords***

Suite shutdown
	Sleep	10s
	Close All Browsers

Open main page
   	Open browser    ${APP_URL}   ${BROWSER}
   	Title Should Be    Home | Frontend

Go to login page
	Click Element       //a[contains(text(),'Login')]

Input Username
	Input Text	input-username	${USERNAME}

Input Password
	Input Text	input-password	${PASSWORD}

Login button
	Click Element       //button[@type="submit"]
	Sleep	1s

Assert Login
	${welcome}=	Get Text	//a[@href="/frontend-vue/account"]
	Should Be Equal	${welcome}	Welcome, Jan

Open page Todo
     Click Element       //a[contains(text(),'Todo')]

Assert Todo
	${Todo App}=	Get Text	//h1[@class="page-title"]
	Should Be Equal	${Todo App}	Todo App

