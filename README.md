# 2020-1 Open Source Software Lab Final Project

## What does this project do?
This is a personal assistant telegram bot.

With Raspberry Pi and Python in operation, this assistant bot can be used anytime, anywhere in telegram.


## Why is this project useful?
* The first time you operate the bot, you will see instructions about how to use it.
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
9. If you want to set your own timetable, modify `tableMsg` part in `bot.py`.
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
- Creating new telegrambot using BotFather: https://www.youtube.com/watch?v=eADOMfD90fQ
- Installing chromium-chromedirver: https://yongbeomkim.github.io/python/selenium-tutorial/

Except these references, all the codes are written by myself.

## Where can I get more help, if I need it?
For more help, please send me email. <21400615@handong.edu>


## YouTube Project Description Link
<br><a href = "https://www.youtube.com/">Youtube video link</a></br>

