## Bulls and Cows Telegram Bot

### Overview
This bot allows you to play the game of Bulls and Cows via Telegram.
The rules of the game can be found on Wikipedia:
https://en.wikipedia.org/wiki/Bulls_and_cows 

### Note
**This bot is not hosted on a server.** 
To use the bot, you need to run the application on your local machine.

### Create Token
For security and privacy reasons, I have not included my personal Telegram bot token in this repository. 
Sharing the token publicly could lead to misuse of the bot.

**Getting Your Telegram Bot Token**

1. Go to "BotFather" bot on Telegram.

2. Create a new bot by following the instructions(enter "/newbot" -> choose the name for your bot).

3. Copy the token provided by BotFather.

4. Create .env file in the root directory of the project

5. Add your token to the .env file:
TOKEN = 'your token'

### Running the Bot
**Install Dependencies:**

Make sure you have Python installed. Install the required libraries using pip:
  
pip install python-dotenv 

pip install pyTelegramBotAPI