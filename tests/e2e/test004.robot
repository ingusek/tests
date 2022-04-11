***Settings***
Library	SeleniumLibrary
Library    FakerLibrary


Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${LOGIN}        %{LOGIN}
${expectedMessage}   Username is already in use.

***Test Cases***
Rejestracja nowego użytkownika w systemie z zajętą nazwą użytkownika
	Open main page
	Go to registration page
    Input Email
   	Input already in use Login
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

Input Email
    ${EMAIL}=    FakerLibrary.Email
	Input Text	input-email	${EMAIL}

Input already in use Login
    Input Text	input-username	${LOGIN}

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
	${message}=	Get Text		//div[@class="text-danger message-col col"]
    Should Be Equal	${message}  ${expectedMessage}
