import telegram
 
token = '5553206519:AAGkMePen2tvas28Ra5_tKsPzK6SZjdrGgs'
bot = telegram.Bot(token = token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)