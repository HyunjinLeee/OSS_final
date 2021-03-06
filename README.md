# 2020-1 Open Source Software Lab Final Project

## What does this project do?
This is a personal assistant telegram bot.

With Raspberry Pi and Python in operation, this assistant bot can be used anytime, anywhere in telegram.


## Why is this project useful?
* At the first time you operate the bot, you will see instructions about how to use it.
* After that, the bot will inform you of the corresponding information by simply entering the command.
* You can get the following informations from this bot.
 1. Date of today
 2. Current time
 3. Current weather of Seoul
 4. Current air quality of Seoul
 5. Current 2020 Worldwide Box Office
 6. Personal timetable
     - Today's timetable
     - Monday timetable
     - Tuesday timetable
     - Wednesday timetable
     - Thursday timetable
     - Friday timetable
 7. Current price of cryptocurrency
     - Bitcoin
     - Ethereum


## How do I get started?
1. Prepare your own Raspberry pi.
2. Clone this repository on your Raspberry pi.
3. Install libraries like followings.
    ```
    $ sudo apt-get install python-pip
    $ sudo pip install telepot
    $ sudo pip install pytz
    $ sudo pip install selenium
    $ sudo pip install Image
    $ sudo pip install datetime
    $ sudo apt-get install chromium-chromedriver
    $ sudo apt-get install xvfb
    $ sudo pip install xvfbwrapper
    ```
4. Create your own telegram account.
5. In telegram, type 'BotFather' in the search bar.
6. Enter followings in BotFather to create your own bot.
   + `/start`
   + `/newbot`
   + bot name
   + username for bot
7. Get your bot's token to access the HTTP API.
8. Insert your own token at `bot.py`'s `YOUR_OWN_TOKEN`.
9. If you want to set your own timetable, modify `gettable` part in `bot.py`.
10. Enter `python` at your Raspberry pi console.
11. Enter the followings. In 'YOUR_OWN_TOKEN', insert your own token.
    ```
    >>> import telepot
    >>> bot = telepot.Bot('Your_OWN_TOKEN')
    >>> bot.getMe()
    >>> exit()
    ```
12. Enter `python bot.py` at your Raspberry pi console. Now the assistant bot is ready.
13. In telegram, type your bot name in the search bar. Click `start` button. It is ready to begin!

## References
- [How to use BotFather, telepot, 'datetime'](https://www.youtube.com/watch?v=eADOMfD90fQ)
- [Installing chromium-chromedirver](https://yongbeomkim.github.io/python/selenium-tutorial/)
- [How to capture screenshot from webpage and cut it](https://codingfull.tistory.com/17?category=842946)
- [How to change timezone](https://technote.kr/202)
- [Get price of cryptocurrency](https://okhee.co.kr/%ED%85%94%EB%A0%88%EA%B7%B8%EB%9E%A8%EB%B4%872-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%A7%8C%EB%93%9C%EB%8A%94-%EC%8B%9C%EC%84%B8%EB%B4%87/)

## New work I added to this project
- Show 'How to use this telegram bot' when starting the bot or entering '/start'.
- Show 'How to get personal timetable' when entering 'timetable'
- Show 'How to get current cryptocurrency price' when entering 'crypto'.
- Get date of today by datetime module and cut it as year-month-date and show it through the telegram bot.
- Get current time by datetime module and cut it as hour-minute-second and show it through the telegram bot.
- Make the 'current time' and 'date of today' to be Korea Standard time(KST).
- Capture weather of Seoul from 'https://www.timeanddate.com/weather/south-korea/seoul' by selenium and chrome driver module then cut the screenshot into appropriate size by Image module and show it through the telegram bot.
- Capture air quality of Seoul from 'https://air-quality.com/place/south-korea/seoul/3a8d31c0?lang=en&standard=aqi_us' by selenium and chrome driver module then cut the screenshot into appropriate size by Image module and show it through the telegram bot.
- Capture 2020 Worldwide Box office from 'https://www.boxofficemojo.com/year/world/2020/?ref_=bo_lnav_hm_shrt' by selenium and chrome driver then cut the screenshot into appropriate size by Image module and show it through the telegram bot.
- Set personal timetable, and when calling it by the telegram bot, show it through the bot.
- When entering 'today', find out what day it is today(day of the week), and then show the proper timetable.
- When entering the day of the week, show the timetable of entered day of the week.

## Where can I get more help, if I need it?
For more help, please send me email. <21400615@handong.edu>


## YouTube Project Description Link
Please watch this video by setting up 1080p HD!!!

https://youtu.be/fcR47MUjXhI
