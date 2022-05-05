*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary
Variables  ../locators/Locators.py
Variables  ../test-data/TestData.py

*** Keywords ***

Input email in field find element
    Input Text	${RequestNewPasswordEmail}	${EMAIL}

Click request new password
    Click Element       ${RequestNewPasswordSendEmailButton}

Assert request new email
    ${title}=	Get Text	${RequestNewPasswordSendEmailAssert}
	Should Be Equal	${title}	We sent you an email.
	Sleep	1s

Check email box
    Open browser    ${MAILHOG_URL}   ${BROWSER}

Open email password reset
    Click Element       ${RequestNewPasswordOpenEmail}

Assert password reset
    
   Select Frame         ${EmailContent}
   Click Element        ${RequestNewPasswordButton}
   Unselect Frame
