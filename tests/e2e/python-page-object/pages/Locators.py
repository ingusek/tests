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


