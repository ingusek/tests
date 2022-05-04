*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary
Variables  ../locators/Locators.py
Variables  ../test-data/TestData.py

***Keywords***

Assert Username
	${username}=	Get Text	 ${AccountPageUsername}
	Should Be Equal	${username}	${MyAccountExpectedUsername}

Assert name
    ${name}=	Get Text	${AccountPageName}
	Should Be Equal	${name}	${MyAccountExpectedName}

Assert email
    ${email}=	Get Text	${AccountPageEmail}
	Should Be Equal	${email}	${MyAccountExpectedEmail}

Open page Account
	Click Element       ${GoToAccountPageButton}
	Sleep	1s

`