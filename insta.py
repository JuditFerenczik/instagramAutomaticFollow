from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import EMAIL, PASSWORD, SIMILAR


class InstaFollower():
    def __init__(self, driver):
        self.driver = webdriver.Chrome(service=Service(driver))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        allowcookies = self.driver.find_element(By.CSS_SELECTOR, "button.aOOlW.HoLwm ")
        allowcookies.click()

        sleep(2)
        username = self.driver.find_element(By.CSS_SELECTOR, "input[name=username]")
        username.send_keys(EMAIL)

        sleep(2)
        password = self.driver.find_element(By.CSS_SELECTOR, "input[name=password]")
        password.send_keys(PASSWORD)

        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(5)
        notifications = self.driver.find_elements(By.CSS_SELECTOR, "div._a9-z button")
        if len(notifications) > 1:
            notifications[1].click()

    def find_followers(self):
        sleep(4)
        search = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div[2]/div/a/div/div[1]/div/div")
        print(search)
        search.click()

        sleep(5)
        searchinput = self.driver.find_element(By.CSS_SELECTOR, "main div div input")
        searchinput.send_keys(SIMILAR)

        sleep(2)
        searchinput.send_keys(Keys.ENTER)

        sleep(2)
        searchinput.send_keys(Keys.ENTER)

        sleep(2)
        FOLLOWER_URL = "/" + SIMILAR + "/followers/"
        followers = self.driver.find_element(By.CSS_SELECTOR, f"a[href='{FOLLOWER_URL}'")
        followers.click()

        sleep(2)
        fbody = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2] ')
        scroll = 0
        while scroll < 5:  # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fbody)
            sleep(2)
            scroll += 1

        followbutton = self.driver.find_elements(By.CSS_SELECTOR, "div.f0dnt3l3.qrrecgo5.o69pmk6j.rt5af2x2.iriodytt.hw7435fk.ba4ynyj4.mm05nxu8.l2tm8nht button._acan._acap._acas")
        print(len(followbutton))
        return followbutton

    def follow(self, follow):
        for i in range(len(follow)):
            sleep(2)
            follow[i].click()
