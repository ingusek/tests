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
008 Sprawdzanie danych użytkownika na stronie http://localhost/ po zalogowaniu się
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
    Open page Account   
	Assert Username
    Assert name
    Assert email

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

Assert Username
	${username}=	Get Text	//div//fieldset[1]//small[@class="form-text text-muted"]
	Should Be Equal	${username}	Ingusek

Assert name
    ${name}=	Get Text	//div//fieldset[2]//small[@class="form-text text-muted"]
	Should Be Equal	${name}	Jan, Kowalski

Assert email
    ${email}=	Get Text	//div//fieldset[3]//small[@class="form-text text-muted"]
	Should Be Equal	${email}	ingus@wp.pl

Open page Account
	Click Element       //a[@href="/account"]
	Sleep	1s
