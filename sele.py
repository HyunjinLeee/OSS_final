from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options = chrome_options)
driver.get("http://www.google.com")
screenshot_name = "/home/pi/weather.png"
driver.save_screenshot(screenshot_name)

