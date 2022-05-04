***Settings***
Library	SeleniumLibrary
# Library	/app/library/ChromeConfiguration.py
# Library	XvfbRobot

Suite Teardown	Run Keyword And Ignore Error  Suite shutdown

***Variables***
${BROWSER}		Chrome
${APP_URL}		%{APP_URL}
${USERNAME}		%{LOGIN}
${PASSWORD}		%{PASSWORD}
${TASK}			Test

***Test Cases***
Status change from Pending to Ongoing
	Open main page
	Go to login page
   	Input Username
   	Input Password
   	Login button
   	Assert Login
	Go to todo list
	Add new task
	Move task to the outgoing list
	Assert Task

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
	${welcome}=	Get Text	//a[@href="/account"]
	Should Be Equal	${welcome}	Welcome, Jan

Go to todo list
	Click Element       //a[@href="/todo"]

Add new task
	Input Text	input-name	${TASK}
	Click Element       //div[@class="todo-add-wrapper"]//button[contains(text(),'Add')]
	Sleep	1s

Move task to the outgoing list
	Drag And Drop	//div[@data-name="todo-pending-list-0"]	//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]

Assert Task
	${source}=	Get Text	//div[@data-name="todo-pending-list-0"]
	${target}=	Get Text	//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]
	Should Be Equal	${source}	${target}
