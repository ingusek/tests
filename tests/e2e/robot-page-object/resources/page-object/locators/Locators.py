# Home page locators
SingUpButton = "//a[contains(text(),'Sign up')]"
LoginButton = "//a[contains(text(),'Login')]"

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

# Account page locators
AccountPageUsername = '//div//fieldset[1]//small[@class="form-text text-muted"]'
AccountPageName ='//div//fieldset[2]//small[@class="form-text text-muted"]'
AccountPageEmail = '//div//fieldset[3]//small[@class="form-text text-muted"]'


