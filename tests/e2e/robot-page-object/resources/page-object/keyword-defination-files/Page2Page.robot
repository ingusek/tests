*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary
Variables  ../locators/Locators.py
Variables  ../test-data/TestData.py

*** Keywords ***

Open Sample Page menu
	Click Element       ${OpenSamplePageMenu}
	Sleep	1s

Open Page2 menu
	Click Element       ${OpenPage2Menu}

Assert Page2
	${title}=	Get Text       ${Page2Title}
	Should Be Equal	${title}	Sample page 2	

