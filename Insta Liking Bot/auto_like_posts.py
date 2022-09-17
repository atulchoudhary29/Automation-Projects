from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        bot=self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(5)
    def search_account(self, account):
        bot=self.bot
        bot.get('https://www.instagram.com/explore/tags/' + account)

    def likes(self, amount):
        bot=self.bot
        bot.find_element_by_class_name('eLAPa').click()
        time.sleep(6)
        for _ in range(amount):
            try:
                bot.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]").click()  
            except:
                bot.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[1]").click()    

            time.sleep(2)

            try:
                bot.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[2]/button/div").click() 
            except:
                bot.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/button/div").click()

            time.sleep(2)
            
        bot.get('https://www.instagram.com/' + self.username)    

insta=InstagramBot('your_username','your_password')
insta.login() 
insta.search_account('filmmaker')
insta.likes(50)           