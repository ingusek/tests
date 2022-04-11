***Settings***
Library	SeleniumLibrary
Library    FakerLibrary


Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${EMAIL}        %{EMAIL}

***Test Cases***
Rejestracja nowego użytkownika w systemie z zajętym adresem email
	Open main page
	Go to registration page
    Input already in use Email
   	Input Username
   	Input Password
    Input First name
    Input Last name
    Register button
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

Input already in use Email
	Input Text	input-email	${EMAIL}

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
	Element Should Be Enabled	//button[@type="submit"]
