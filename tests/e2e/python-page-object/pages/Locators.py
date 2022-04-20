from selenium.webdriver.common.by import By

class RegisterPageLocators():
    """
    Locators used on Register Page
    """
    RegisterEmailInput = (By.ID, 'input-email')
    RegisterUsernameInput = (By.ID, 'input-username')
    RegisterPasswordInput = (By.ID, 'input-password')
    RegisterFirstNameInput = (By.ID, 'input-first-name')
    RegisterLastNameInput = (By.ID, 'input-last-name')
    RegisterButton = (By.XPATH, '//button[@type="submit"]')
    RegisterDangerMessage = (By.XPATH, '//div[@class="text-danger message-col col"]')
    Title = (By.XPATH, "//div[@class='card-body']//h1")


class RegisterConfirmationPageLocators():
    """
    Locators used on Register Confirmation Page
    """
    WelcomeAfterRegisterText = (By.XPATH, "//div[@class='card-body']//h1")

class HomePageLocators():
    """
    Home page locators
    """
    SingUpButton = (By.XPATH, "//a[contains(text(),'Sign up')]")
    LoginButton = (By.PARTIAL_LINK_TEXT, "Login")
    MyAccountButton = (By.PARTIAL_LINK_TEXT, 'My Account')
    LogoutButton = (By.XPATH, '//a[@href="/frontend-vue/logout"]')
   


class MailHogPageLocators():
    EmailRegistrationConfirmButton = (By.PARTIAL_LINK_TEXT, 'Confirm')
    EmailFirstRow = (By.XPATH, '//div[@class="messages container-fluid ng-scope"]/div[1]')
    PreviewIframe = (By.ID, "preview-html")

class LoginPageLocators:
    PageTitle = (By.XPATH, '//div[@class="card-body"]/h1')
    ConfirmRegistrationInfoBox = (By.XPATH, '//div[@data-cy="login-success-message"]')
    FieldLogin = (By.ID, "input-username")
    FieldPassword = (By.ID, "input-password")
    ButtonLogin = (By.XPATH, '//button[@type="submit"]')
    ErrorLoginMessage = (By.XPATH, '//div[@data-cy="login-error-message"]')

class MyAccountPageLocators:
    FieldUsername = (By.XPATH, "//div[@class='card-body']//div/fieldset/div")
