import telegram
import time

my_token = '348728717:AAFo2orhFFIptTaQr2TA-zzycO82Tj46dvs'

bot = telegram.Bot(token = my_token)

updates = bot.getUpdates()

for u in updates :

    print(u.message)

chat_id = bot.getUpdates()[-1].message.chat.id

bot.sendMessage(chat_id = 169495465, text="I'm Jenna.")
