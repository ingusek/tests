***Settings***
Library	SeleniumLibrary
# Library	/app/library/ChromeConfiguration.py
# Library	XvfbRobot

Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${USERNAME}		%{LOGIN}
${PASSWORD}		błędne hasło


***Test Cases***
Logowanie się na stronie http://todo.local/frontend-vue/login przy użyciu poprawnego loginu i niepoprawnego hasła.
	Open main page
	Go to login page
   	Input Username
   	Input Invalid Password
   	Login button
   	Assert Login
	

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

Input Invalid Password
	Input Text	input-password	${PASSWORD}

Login button
	Click Element       //button[@type="submit"]
	Sleep	1s

Assert Login
	${message}=	Get Text	//div[@data-cy="login-error-message"]
	Should Be Equal	${message}      Your username or password is incorrect. Please try again.	
