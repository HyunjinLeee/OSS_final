#-*- coding:utf-8 -*-
import time
import os
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

reload(sys)
sys.setdefaultencoding('utf-8')

symbol = ""
startmessage = "Welcome to HJOSS_bot! \n" \
        "This is a personal assitant telegram bot.\n" \
        "Please enter any of the following commands you want. \n" \
        " -  date -> Date of today\n" \
        " -  time -> Current time\n" \
        " -  weather -> Current weather of Seoul\n" \
        " -  airquality -> Current air quality of Seoul\n" \
        " -  boxoffice -> Current 2020 Worldwide Box Office\n" \
        " -  If you want to check your timetable, enter 'timetable' to know the input commands.\n" \
        " -  To know current price of cryptocurrency, enter 'crypto' to know the input commands."
       
tableMsg = "Enter any of the following commands you want.\n" \
        " -  today -> Today's timetable\n" \
        " -  monday -> Monday timetable\n" \
        " -  tuesday  -> Tuesday timetable\n" \
        " -  wednesday -> Wednesday timetable\n" \
        " -  thursday -> Thursday timetable\n" \
        " -  friday -> Friday timetable"

cryptoMsg = "Enter any of the following commands you want.\n" \
        " -  bit -> Bitcoin\n" \
        " -  ethe -> Ethereun"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


WeatherURL = 'https://www.timeanddate.com/weather/south-korea/seoul'
AirURL = 'https://air-quality.com/place/south-korea/seoul/3a8d31c0?lang=en&standard=aqi_us'
MovieURL = 'https://www.boxofficemojo.com/year/world/2020/?ref_=bo_lnav_hm_shrt'

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
    elif command == 'crypto':
        bot.sendMessage(chat_id, cryptoMsg)
    elif command == 'bit':
        price = getprice("btc")
        bot.sendMessage(chat_id, 'Bitcoin: %s won' %price)
    elif command == 'ethe':
        price = getprice("eth")
        bot.sendMessage(chat_id, 'Ethereum: %s won' %price)
    elif command == 'timetable':
        bot.sendMessage(chat_id, tableMsg)
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
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options = chrome_options)
        driver.implicitly_wait(3)
        driver.get(WeatherURL)
        screenshot_name = "/home/pi/bot/OSS_final/weather.png"
        driver.save_screenshot(screenshot_name)
        img = Image.open('/home/pi/bot/OSS_final/weather.png')
        cutted_img = img.crop((19,215,310,400))
        cutted_img.save('/home/pi/bot/OSS_final/weather.png')
        bot.sendMessage(chat_id, "Let me tell you the current weather in Seoul.")
        bot.sendPhoto(chat_id, (open('/home/pi/bot/OSS_final/weather.png',"rb")))
    elif command == 'airquality':
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options = chrome_options)
        driver.implicitly_wait(3)
        driver.get(AirURL)
        screenshot_name = "/home/pi/bot/OSS_final/airquality.png"
        driver.save_screenshot(screenshot_name)
        img = Image.open('/home/pi/bot/OSS_final/airquality.png')
        cutted_img = img.crop((30,140,750,575))
        cutted_img.save('/home/pi/bot/OSS_final/airquality.png')
        bot.sendMessage(chat_id, "Let me tell you the current air quality in Seoul.")
        bot.sendPhoto(chat_id, (open('/home/pi/bot/OSS_final/airquality.png',"rb")))
    elif command == 'boxoffice':
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options = chrome_options)
        driver.implicitly_wait(3)
        driver.get(MovieURL)
        screenshot_name = "/home/pi/bot/OSS_final/movie.png"
        driver.save_screenshot(screenshot_name)
        img = Image.open('/home/pi/bot/OSS_final/movie.png')
        cutted_img = img.crop((10,180,750,585))
        cutted_img.save('/home/pi/bot/OSS_final/movie.png')
        bot.sendMessage(chat_id, "Let me tell you the current 2020 Worldwide Box Office.")
        bot.sendPhoto(chat_id, (open('/home/pi/bot/OSS_final/movie.png',"rb")))


    else:
        bot.sendMessage(chat_id, 'I cannot understand')


bot = telepot.Bot('1185667712:AAFYzUb4Lf2yWMsivGBYWfRloMXlEWZfmqA')

MessageLoop(bot, handle).run_as_thread()

print 'I am listening ...'

while True:
    time.sleep(10)
