***Settings***
Metadata    Author       	Inga Gajewska
Library		SeleniumLibrary
Library    	FakerLibrary

Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${InvalidEmail}	ji8989898uii
${EMAIL}        %{EMAIL}
${LOGIN}        %{LOGIN}

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

Rejestracja nowego użytkownika w systemie z zajętym adresem email
	Open main page
	Go to registration page
    Input already in use Email
   	Input Username
   	Input Password
    Input First name
    Input Last name
    Register button
   	Assert Register with email already in use

Rejestracja nowego użytkownika w systemie z zajętą nazwą użytkownika
	Open main page
	Go to registration page
    Input Email
   	Input already in use Login
   	Input Password
    Input First name
    Input Last name
    Register button
   	Assert Register with username already in use

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

Input already in use Email
	Input Text	input-email	${EMAIL}

Input already in use Login
    Input Text	input-username	${LOGIN}

Register button
    Element Should Be Enabled	//button[@type="submit"]
	Click Element       //button[@type="submit"]
	Sleep	1s

Assert Register
	${welcome}=	Get Text	//div[@class="card-body"]//h1
	Should Be Equal	${welcome}	You are successfully registered.

Assert Register With Invalid Email
	Element Should Be Disabled	//button[@type="submit"]

Assert Register with email already in use
	Element Should Be Enabled	//button[@type="submit"]

Assert Register with username already in use
	${message}=	Get Text		//div[@class="text-danger message-col col"]
    Should Be Equal	${message}	Username is already in use.

