#-*- coding: utf-8 -*-
import time
import sys
import random
from pytz import timezone
import datetime
import telepot
import requests
from telepot.loop import MessageLoop
import urllib
from selenium import webdriver
import configparser
from PIL import Image

"""
[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
"""
symbol = ""
startmessage = "Welcome to HJOSS_bot! \n" \
        "Please input command like followings \n" \
        "1. bit -> bitcoin \n" \
        "2. ethe -> ethereum\n" \
        "3. date -> Date of today\n" \
        "4. time -> Current time\n" \
        "5. If you want to check your timetable, input day of the week like followings\n" \
        " -  today -> Today's timetable\n" \
        " -  monday -> Monday timetable\n" \
        " -  tuesday  -> Tuesday timetable\n" \
        " -  wednesday -> Wednesday timetable\n" \
        " -  thursday -> Thursday timetable\n" \
        " -  friday -> Friday timetable"

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")


WeatherURL = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=날씨'

def gettable(symbol):
    if(symbol == 'monday'):
        table = "\n" \
                "09:30 ~ 11:15 Mobile App Development\n" \
                "11:30 ~ 12:45 Law And Technology\n" \
                "13:00 ~ 14:15 Open Source Software Lab"
    elif(symbol == 'tuesday'):
        table = "\n" \
                "13:00 ~ 14:15 Seminar\n" \
                "16:00 ~ 18:45 Practical Finanace For College Students"
    elif(symbol =='wednesday'):
        table = "\n" \
                "10:00 ~ 12:45 Liberal Arts\n" \
                "13:00 ~ 14:15 Career And Career Design"
    elif(symbol == 'thursday'):
        table = "\n" \
                "09:30 ~ 11:15 Mobile App Development\n" \
                "11:30 ~ 12:45 Law And Technology\n" \
                "13:00 ~ 14:15 Open Source Software Lab"
    elif(symbol == 'friday'):
        table = "\n" \
                "There is no schedule today!"
    else:
        table = "\n" \
                "Today is holiday! There is no schedule today!"

    return table

def getprice(symbol):
    url = "https://api.bithumb.com/public/ticker/%s" % symbol
    response = requests.get(url=url)
    price = response.text.split(':')[5].split('"')[1]
    return price

def gettime(symbol):
    if(symbol == 'date'):
        time = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    elif(symbol == 'time'):
        time = str(datetime.datetime.now(timezone("Asia/Seoul")).strftime('%H:%M:%S'))
    return time

def getday():
    t = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    r = datetime.datetime.today().weekday()
    return t[r]

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print 'Got command: %s' % command

    if command == '/start':
        bot.sendMessage(chat_id, startmessage)
    elif command == 'date':
        time = gettime('date')
        bot.sendMessage(chat_id, 'The date today is %s' %time)
    elif command == 'time':
        time = gettime('time')
        bot.sendMessage(chat_id, 'It is now %s' %time)
    elif command == '/random':
        bot.sendMessage(chat_id, random.randin(1,6))
    elif command == 'bit':
        price = getprice("btc")
        bot.sendMessage(chat_id, 'Bitcoin: %s won' %price)
    elif command == 'ethe':
        price = getprice("eth")
        bot.sendMessage(chat_id, 'Ethereum: %s won' %price)
    elif command == 'monday':
        table = gettable('monday')
        bot.sendMessage(chat_id, "Monday's time table is %s" %table)
    elif command == 'tuesday':
        table = gettable('tuesday')
        bot.sendMessage(chat_id, "Tuesday's time table is %s" %table)
    elif command == 'wednesday':
        table = gettable('wednesday')
        bot.sendMessage(chat_id, "Wednesday's time table is %s" %table)
    elif command == 'thursday':
        table = gettable('thursday')
        bot.sendMessage(chat_id, "Thursday's time table is %s" %table)
    elif command == 'friday':
        table = gettable('friday')
        bot.sendMessage(chat_id, "Friday's time table is %s" %table)
    elif command == 'today':
        day = getday()
        table = gettable(day)
        bot.sendMessage(chat_id, "Today's time table is %s" %table)
    elif command == 'weather':
        driver = webdriver.Chrome('/usr/bin/chromedriver')
        driver.implicitly_wait(3)
        driver.get(WeatherURL)
        screenshot_name = "/home/weather.png"
        driver.save_screenshot(screenshot_name)
        img = Image.open('/home/weather.png')
        cutted_img = img.crop((39,210,622,677))
        cutted_img.save('/home/weather.png')
        bot.sendPhoto(chat_id, 'home/weather.png')


    else:
        bot.sendMessage(chat_id, 'I cannot understand')


bot = telepot.Bot('1185667712:AAFYzUb4Lf2yWMsivGBYWfRloMXlEWZfmqA')

MessageLoop(bot, handle).run_as_thread()

print 'I am listening ...'

while True:
    time.sleep(10)
