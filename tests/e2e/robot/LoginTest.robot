***Settings***
Library	SeleniumLibrary
# Library	/app/library/ChromeConfiguration.py
# Library	XvfbRobot

Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${USERNAME}		%{LOGIN}
${INVALID_USERNAME}		błedny login
${PASSWORD}		%{PASSWORD}
${INVALID_PASSWORD}		błędne hasło
${TASK}			Test

***Test Cases***
Logowanie się na stronie http://todo.local/frontend-vue/login przy użyciu poprawnego loginu i poprawnego hasła
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login

Logowanie się na stronie http://todo.local/frontend-vue/login przy użyciu poprawnego loginu i niepoprawnego hasła.
	Open main page
	Go to login page
   	Input Username
   	Input Invalid Password
   	Login button
   	Assert Login with invalid password

Logowanie się na stronie http://todo.local/frontend-vue/login przy użyciu niepoprawnego loginu i poprawnego hasła.
	Open main page
	Go to login page
   	Input Invalid Username
   	Input Password
   	Login button
   	Assert Login with invalid username
	

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
    
Input Invalid Username
	Input Text	input-username	${INVALID_USERNAME}

Input Password
	Input Text	input-password	${PASSWORD}

Input Invalid Password
	Input Text	input-password	${INVALID_PASSWORD}

Login button
	Click Element       //button[@type="submit"]
	Sleep	1s

Assert Login
	${welcome}=	Get Text	//a[@href="/frontend-vue/account"]
	Should Be Equal	${welcome}	Welcome, Jan

Assert Login with invalid password
	${message}=	Get Text	//div[@data-cy="login-error-message"]
	Should Be Equal	${message}      Your username or password is incorrect. Please try again.

Assert Login with invalid username
	${message}=	Get Text	//div[@data-cy="login-error-message"]
	Should Be Equal	${message}      Your username or password is incorrect.	


