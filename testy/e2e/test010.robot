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
Sprawdzanie czy da się wylogować ze strony http://todo.local/frontend-vue/
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
    Logout button
   	Assert Logout
	

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

Logout button
    Click Element       //a[contains(text(),'Logout')]
	Sleep	1s

Assert Logout
	Element Should Be Visible	//a[contains(text(),'Login')]




