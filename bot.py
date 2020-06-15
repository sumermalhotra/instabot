""" 

This bot has numerous use cases ranging from marketing to spreading awareness and much 
more on what is currently the worlds most popular social media platform. This bot can
also easily be programmed to hate on people you don't like but I don't recommend that.

This file contains the main code used by the bot.

Use the hashtags.txt file to input hashtags for which to scrape.

A <username>_users.txt file is created which tracks people followed using the bot,
in case you want to manually unfollow them at some point in the future. Don't 
forget to delete entries in this file as you unfollow people.

Manually change the comments in the generateComments(n) function. Currently, it is 
configured for a fitness page based instabot. 

Current functionality is following, liking and commenting (1 out of 10 random comments),
if you don't currently follow the user. Can be edited easily by commenting out unnecessary
portions.

"""

from time import sleep
from random import randint
from credentials import acc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

users = open(f"{acc.username}_users.txt", "r")
lines =  users.readlines()
all_users = [t[:-1] for t in lines]
users.close()

hashtags = open("hashtags.txt", "r")
lines =  hashtags.readlines()
hashtag_list = [t[:-1] for t in lines]
hashtags.close() 

def generateComment(n):
    if n == 1:
        return "Great work!"
    elif n == 2:
        return "I love your profile!"
    elif n == 3:
        return "Follow for follow?"
    elif n == 4:
        return "Winners train. Losers complain."
    elif n == 5:
        return "Excuses don't burn calories.."
    elif n == 6:
        return "Slow progress is still progress.."
    elif n == 7:
        return "Im hitting the gym so I dont have to hit you :P"
    elif n == 8:
        return "Do you even deadlift bro?"
    elif n == 9:
        return "Cardio? I'm out."
    else:
        return "I’ve got 99 problems, but I’m going to the gym and ignoring all of them."

def login(webdriver, acc):
    username = webdriver.find_element_by_name('username')
    password = webdriver.find_element_by_name('password')
    username.send_keys(acc.username)
    sleep(2)
    password.send_keys(acc.password)
    sleep(2)
    button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
    button_login.click()
    sleep(3)
    not_now = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    not_now.click()
    sleep(2)
    not_now_2 = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div:nth-child(3) > button:nth-child(2)')
    not_now_2.click()
    sleep(2)

def activity(webdriver):

    for hashtag in hashtag_list: 

        webdriver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        sleep(5)

        first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        first_thumbnail.click()
        sleep(2)

        try:
            
            for x in range(1000):

                try:

                    username = webdriver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div:nth-child(2) > div > article > header > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)').text
                    if username not in all_users:

                        follow_button = webdriver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div:nth-child(2) > div > article > header > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > button')
                        if follow_button.text == 'Follow':

                            # Follow current user
                            follow_button.click()
                            all_users.append(username)
                            f.write(username)
                            f.write('\n')
                            sleep(randint(3, 5))

                            # Like picture
                            like_button = webdriver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div:nth-child(2) > div > article > div.eo2As > section > span > button')
                            like_button.click()
                            sleep(randint(20, 30))

                            # Comment on picture
                            comment_box = webdriver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div:nth-child(2) > div > article > div.eo2As > section.sH9wk._JgwE > div > form')
                            comment_box.click()
                            comment = generateComment(randint(1, 10))
                            comment_box.find_element_by_css_selector('textarea').send_keys(comment)
                            comment_box.find_element_by_css_selector('button').click()
                            sleep(randint(3, 5))

                            # Next picture
                            webdriver.find_element_by_link_text('Next').click()
                            sleep(randint(5, 9))

                    else:

                        # Next picture
                        webdriver.find_element_by_link_text('Next').click()
                        sleep(randint(5, 9))

                except Exception as e:
                    print(e)
                    
        except Exception as e:
            print(e)

f = open(f"{acc.username}_users.txt", "a+")
webdriver = webdriver.Chrome(ChromeDriverManager().install())
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(5)
login(webdriver, acc)
activity(webdriver)

f.close()