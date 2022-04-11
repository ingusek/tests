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
Logowanie się na stronie http://todo.local/frontend-vue/login przy użyciu poprawnego loginu i poprawnego hasła
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
	Sleep	1s

Open Sample Page menu
	Click Element       //span[contains(text(),'Sample Page')]
	Sleep	1s

Open Page2 menu
	Click Element       //a[@href="/frontend-vue/sample-page/2"]
	Sleep	1s

Assert Page2
	${title}=	Get Text       //div[@class="page-page text-center my-5"]/h1
	Should Be Equal	${title}	Sample page 2	
