# Home page locators
SingUpButton = "//a[contains(text(),'Sign up')]"
LoginButton = "//a[contains(text(),'Login')]"
LogoutButton = "//a[contains(text(),'Logout')]"

# Locators used on Register Confirmation Page
WelcomeAfterRegisterText = "//div[@class='card-body']//h1"

# Register page locators
RegisterEmailInput = 'input-email'
RegisterUsernameInput = 'input-username'
RegisterPasswordInput = 'input-password'
RegisterFirstNameInput = 'input-first-name'
RegisterLastNameInput = 'input-last-name'
RegisterButton = '//button[@type="submit"]'
RegisterErrorMessage = '//div[@class="text-danger message-col col"]'

# Login page locators
SubmitLoginButton = '//button[@type="submit"]'
GoToAccountPageButton = '//a[@href="/account"]'
LoginErrorMessage = '//div[@data-cy="login-error-message"]'
LoginUsernameInput = 'input-username'
LoginPasswordInput = 'input-password'
ResetPasswordButton = "//a[contains(text(),'Forgot password?')]"

# Account page locators
AccountPageUsername = '//div//fieldset[1]//small[@class="form-text text-muted"]'
AccountPageName ='//div//fieldset[2]//small[@class="form-text text-muted"]'
AccountPageEmail = '//div//fieldset[3]//small[@class="form-text text-muted"]'

# Page2 page locators
OpenSamplePageMenu = "//span[contains(text(),'Sample Page')]"
OpenPage2Menu = '//a[@href="/sample-page/2"]'
Page2Title = '//div[@class="page-page text-center my-5"]/h1'

# Todo page locators
OpenPageTodoMenu = "//a[contains(text(),'Todo')]"
TodoPageTitle = '//h1[@class="page-title"]'
ButtonAddTodo = "//button[contains(text(),'Add')]"
TodoPendingItem = '//div[@data-name="todo-pending-name-0"]//span'
RemovePendingItemButton = '//div[@data-name="todo-pending-list-0"]//button'
RemoveAssertPendingItemButton = '//div[@data-name="todo-pending-name-0"]//span[contains(text(),"${entry}")]'
TodoAddItemInput = 'input-name'
def MoveItemToOngiongButton(entry):
  return '//div[@class="card-deck"]//div[@class="card mb-3"][1]//div[@class="todo-list-group"]/div//span[text()="'+entry+'"]/../../button[2]'
def MoveItemToCompletedButton(entry):
  return '//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]/div//span[text()="'+entry+'"]/../../button[3]'
def FindItemsInTheListCompleted(entry):
  return '//div[@class="card-deck"]//div[@class="card mb-3"][3]//div[@class="todo-list-group"]/div//span[text()="'+entry+'"]'
def FindItemsInTheListOngoing(entry):
  return '//div[@class="card-deck"]//div[@class="card mb-3"][2]//div[@class="todo-list-group"]/div//span[text()="'+entry+'"]'

# Reset password page locators
RequestNewPasswordEmail = "input-email"
RequestNewPasswordSendEmailButton = '//button[@type="submit"]'
RequestNewPasswordSendEmailAssert = '//div[@class="card-body"]/h1'
RequestNewPasswordOpenEmail = '//div[@class="messages container-fluid ng-scope"]/div[1]'
RequestNewPasswordButton = "//a[contains(text(), 'Reset your password')]"
EmailContent = "preview-html"
