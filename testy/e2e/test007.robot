***Settings***
Library	SeleniumLibrary
# Library	/app/library/ChromeConfiguration.py
# Library	XvfbRobot

Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${USERNAME}		błedny login
${PASSWORD}		%{PASSWORD}


***Test Cases***
Logowanie się na stronie http://todo.local/frontend-vue/login przy użyciu niepoprawnego loginu i poprawnego hasła.
	Open main page
	Go to login page
   	Input Invalid Username
   	Input Password
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

Input Invalid Username
	Input Text	input-username	${USERNAME}

Input Password
	Input Text	input-password	${PASSWORD}

Login button
	Click Element       //button[@type="submit"]
	Sleep	1s

Assert Login
	${message}=	Get Text	//div[@data-cy="login-error-message"]
	Should Be Equal	${message}      Your username or password is incorrect.	
