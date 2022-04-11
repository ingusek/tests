***Settings***
Metadata    Author       	Inga Gajewska
Library		SeleniumLibrary
Library    	FakerLibrary

Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${InvalidEmail}	ji8989898uii

***Test Cases***
Rejestracja nowego użytkownika w systemie
	Open main page
	Go to registration page
    Input Email
   	Input Username
   	Input Password
    Input First name
    Input Last name
   	Register button
   	Assert Register

Rejestracja nowego użytkownika w systemie z niepoprawnym adresem email
	Open main page
	Go to registration page
    Input Invalid Email
   	Input Username
   	Input Password
    Input First name
    Input Last name
   	Assert Register With Invalid Email

***Keywords***

Suite shutdown
	Close All Browsers

Open main page
   	Open browser    ${APP_URL}   ${BROWSER}
   	Title Should Be    Home | Frontend

Go to registration page
	Click Element       //a[contains(text(),'Sign up')]

Input Email
    ${EMAIL}=    FakerLibrary.Email
	Input Text	input-email	${Email}

Input Invalid Email
	Input Text	input-email	${InvalidEmail}

Input Username
    ${USERNAME}=    FakerLibrary.First_Name
	Input Text	input-username	${USERNAME}

Input Password
    ${PASSWORD}=    FakerLibrary.Password
	Input Text	input-password	${PASSWORD}

Input First name
    ${FIRST_NAME}=    FakerLibrary.First_Name
	Input Text	input-first-name	${FIRST_NAME}

Input Last name
    ${LAST_NAME}=    FakerLibrary.Last_Name
	Input Text	input-last-name	${LAST_NAME}

Register button
    Element Should Be Enabled	//button[@type="submit"]
	Click Element       //button[@type="submit"]
	Sleep	1s

Assert Register
	${welcome}=	Get Text	//div[@class="card-body"]//h1
	Should Be Equal	${welcome}	You are successfully registered.

Assert Register With Invalid Email
	Element Should Be Disabled	//button[@type="submit"]