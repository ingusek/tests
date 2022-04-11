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
${EMAIL}        %{EMAIL}
${MAILHOG_URL}  %{MAILHOG_URL}
                 

***Test Cases***
Otrzymanie emaila z linkiem do resetu hasła
	Open main page
	Go to login page
    Click forgot password
   	Input email in field find element
    Click request new password
    Assert request new email
	Check email box 
    Open email password reset
    Assert password reset

***Keywords***

Suite shutdown
	Sleep	10s
	Close All Browsers

Open main page
   	Open browser    ${APP_URL}   ${BROWSER}
   	Title Should Be    Home | Frontend

Go to login page
	Click Element       //a[contains(text(),'Login')]

Click forgot password
    Click Element       //a[contains(text(),'Forgot password?')]

Input email in field find element
    Input Text	input-email	${EMAIL}

Click request new password
    Click Element       //button[@type="submit"]

Assert request new email
    ${title}=	Get Text	//div[@class="card-body"]/h1
	Should Be Equal	${title}	We sent you an email.
	Sleep	1s

Check email box
    Open browser    ${MAILHOG_URL}   ${BROWSER}

Open email password reset
    Click Element       //div[@class="messages container-fluid ng-scope"]/div[1]

Assert password reset
    
   Select Frame      preview-html
   sleep   3s
   Click Element        //a[contains(text(), 'Reset Your Password')]
   sleep   3s   
   Unselect Frame    
   Sleep	3s
     
