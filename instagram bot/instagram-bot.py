from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import random
from pyfiglet import Figlet
text = Figlet(font="slant")
print(text.renderText("Instagram Bot"))
print("-----You need to have FireFox browser installed-----")
print(" ")
print("====================================================")
print(" ")
print("----------------Log In to Instagram-----------------")

username = input("Username: ")
password = input("Password: ")
hastag = input("hastag: ")
comments = input("comment text: ")

def hand_typed_comment(comment, field):
    for i, v in enumerate(comment):
        field.send_keys(v)
        
binary = FirefoxBinary('c:/program files/mozilla firefox/firefox.exe')
profile = webdriver.FirefoxProfile()
profile.set_preference('intl.accept_languages', 'en-GB')
browser = webdriver.Firefox(firefox_binary=binary, executable_path="geckodriver.exe", firefox_profile=profile)
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

sleep(1)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")


username_input.send_keys(username)
password_input.send_keys(password)


login_btn = browser.find_element_by_xpath("//button[@type='submit']")
login_btn.click()

sleep(0.5)


notnow_btn = browser.find_element_by_xpath("//button[text()='Not now']")
notnow_btn.click()



  
sleep(0.5)

notnow_btn = browser.find_element_by_css_selector(".HoLwm")
notnow_btn.click()

sleep(1)
    
browser.get('https://www.instagram.com/explore/tags/' + hastag + '/')

sleep(0.5)

posts = browser.find_elements_by_css_selector("a[href*='/p/']")
links = [elem.get_attribute('href') for elem in posts]



for link in links:
    random_time_addon = random.random()

    browser.get(link)
    sleep(1)

   
    like_btn = browser.find_element_by_css_selector(".fr66n .wpO6b")
    like_btn.click()
    sleep(1)

    like_btn = browser.find_element_by_css_selector("._15y0l .wpO6b")
    like_btn.click()
    sleep(1)
    
    comment_textarea = browser.find_element_by_css_selector("textarea")
    hand_typed_comment(random.choice(comments), comment_textarea)
    sleep(0.4)

    submit_comment = browser.find_element_by_xpath("//button[@data-testid='post-comment-input-button']")
    submit_comment.click()
    sleep(3)



#browser.close()

