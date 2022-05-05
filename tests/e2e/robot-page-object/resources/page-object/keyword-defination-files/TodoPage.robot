*** Settings ***
Library     SeleniumLibrary
Library     FakerLibrary
Variables  ../locators/Locators.py
Variables  ../test-data/TestData.py

*** Keywords ***

Open page Todo
     Click Element       ${OpenPageTodoMenu}

Assert Todo
	${Todo App}=	Get Text	${TodoPageTitle}
	Should Be Equal	${Todo App}	Todo App

Add a new entry to the list Todo
    Input Text	input-name	${entry}
    Click Element       ${ButtonAddTodo}
	Sleep	1s

Assert a new entry to the list Todo
	${new_entry}=	Get Text	${TodoPendingItem}
	Should Be Equal	${new_entry}	${entry}

Remove item from list Pending 
    Click Element       ${RemovePendingItemButton}
	Sleep	1s  

Assert removing item from list Pending
	Page Should Not Contain Element	${RemoveAssertPendingItemButton}

