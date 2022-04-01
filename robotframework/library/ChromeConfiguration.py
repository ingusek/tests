from selenium.webdriver.chrome.options import Options

def config():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--log-level=ALL')
    return options

def serviceargs():
    return ["--verbose", "--log-path=/home/developer/chromedriver.log"]
