# Typeracer Bot

## Table of Content

1. [Demo](#Demo)
2. [Description](#Description)
3. [Functionalities](#Functionalities)
4. [Installation Steps](#Installation-Steps)
5. [FAQ](#FAQ)
6. [Build With](#Built-With)
7. [License](#License)
8. [Author](#Author)

## Demo 

![typeracer_bot_video](https://imgur.com/4ELfUT3)

## Description

This is a automated program for the website [typeracer.com](https://play.typeracer.com/) made with the use of Python that automatically plays normal games on the website. It is a simple automating script that uses selenium and pyautogui. 

## Functionalities

* Automatically logs in to a [typeracer.com](https://play.typeracer.com/) account 
* Automatically plays normal games
* Automatically keeps playing the number of times asked by the user

## Installation Steps

1. Go to [Chrome WebDriver](https://chromedriver.chromium.org/downloads) and donwload the correct WebDriver for you version of chrome. **_If you do not know your chrome version, you can find it_** [here](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)
2. During the installation process of Chrome WebDriver, remember the path where the exe file has been installed
3. Open the project with an IDE, inside the IDE built-in terminal write : `pip install -r requirements.txt`
4. Open **setup.py** and follow the instructions
5. You can now run the python code

## FAQ

**Q**: **How do I change the bot typing speed?**

**A**: In line 35 of the **main.py** file, you can play with the number inside interval. _PS : I recommend keeping it at the current speed as it seems to be the optimal one_


**Q**: **Why doesn't the bot type faster?**

**A**: [Typeracer.com](https://play.typeracer.com/) seems to have limitations as to how fast you can type. _PS : I'm looking for a work-around_


**Q**: **What average wpm can I except with the current configuration?**

**A**: You can except an average of around 100wpm to 115 wmp


**Q**: **Why does the bot not get past the login page?**

**A**: Make sure your account is verified and you put in the correct login informations


**Q**: **Why am I having problems running the bot?**

**A**: You probably didn't follow the [Installation Steps](#Installation-Steps) well

## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) - The IDE used
* [Python 3.8](https://www.python.org/) - The programming language used
* [Chrome WebDriver](https://chromedriver.chromium.org/downloads) - The executable that replicates Google Chrome   

## License 

This project is licensed under MIT License - see the [LICENSE.md](https://github.com/ousmanebarry/typeracer-bot/blob/main/LICENSE) file for details

## Author

* This project was made by me. It is one of my first few Python projects and I will add more functionalities to this as time goes on
