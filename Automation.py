from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path="/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/selenium/webdriver/chrome/chromedriver")

driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys('{{Your email}}')
searchbutton = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
searchbutton.click()
driver.implicitly_wait(4)
driver.find_element_by_name('password').send_keys('{{Your password}}')
password_next = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
password_next.click()
