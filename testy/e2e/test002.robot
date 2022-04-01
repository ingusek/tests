***Settings***
Library	SeleniumLibrary
Library    FakerLibrary


Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${EMAIL}       ji8989898uii

***Test Cases***
Rejestracja nowego użytkownika w systemie z niepoprawnym adresem email
	Open main page
	Go to registration page
    Input Invalid Email
   	Input Username
   	Input Password
    Input First name
    Input Last name
   	Assert Register

***Keywords***

Suite shutdown
	Sleep	10s
	Close All Browsers

Open main page
   	Open browser    ${APP_URL}   ${BROWSER}
   	Title Should Be    Home | Frontend

Go to registration page
	Click Element       //a[contains(text(),'Sign up')]

Input Invalid Email
	Input Text	input-email	${Email}

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

Assert Register
	Element Should Be Disabled	//button[@type="submit"]
