***Settings***
Library	    SeleniumLibrary
Library     FakerLibrary


Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${USERNAME}		%{LOGIN}
${PASSWORD}		%{PASSWORD}

***Test Cases***
Sprawdzanie funkcjonalności Todo-usunięcie pozycji z listy Pending
    ${entry}=    FakerLibrary.Name
    Set Suite Variable  ${entry}
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login
	Open page Todo
    Add a new entry to the list Todo
    Remove item from list Pending
    Assert removing item from list Pending
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

Assert Login
	${welcome}=	Get Text	//a[@href="/frontend-vue/account"]
	Should Be Equal	${welcome}	Welcome, Jan

Open page Todo
     Click Element       //a[contains(text(),'Todo')]
     Sleep  1s

Assert Todo
	${Todo App}=	Get Text	//h1[@class="page-title"]
	Should Be Equal	${Todo App}	Todo App

Add a new entry to the list Todo
    Input Text	input-name	${entry}
    Click Element       //button[contains(text(),'Add')]
	Sleep	1s

Assert a new entry to the list Todo
    Page Should Contain Element	//div[@data-name="todo-pending-name-0"]//span[contains(text(),'${entry}')]
	${new_entry}=	Get Text	//div[@data-name="todo-pending-name-0"]//span
	Should Be Equal	${new_entry}	${entry}

Remove item from list Pending 
    Click Element       //div[@data-name="todo-pending-list-0"]//button
	Sleep	1s  

Assert removing item from list Pending
	Page Should Not Contain Element	//div[@data-name="todo-pending-name-0"]//span[contains(text(),'${entry}')]
