import requests,telebot
bot = telebot.TeleBot('5144396245:AAEydB4XI9Lfr38ASbieDlU1lUZlhPGYOjI')
@bot.message_handler(commands=["start"])
def mes(message):
 bot.send_message(message.chat.id,'مرحباً بك في بوت رشق نقاط INSTA-UP \n ارسل المعلومات بهذا الشكل \n 0000:1111 \n حيث 0000 هو ايدي حسابك و 1111 هو ايدي الضحية \n By : @K_K3L')
@bot.message_handler(func=lambda m:True)
def inf(message):
 bot.send_message(message.chat.id,"please wait ...🥱")
 b_4qr= message.text
 baqer= b_4qr.split(':')[0]
 TAK   = b_4qr.split(':')[1]
 url=(f"https://RASHIK-INSTA-UP-BY-ALI-HUSSEIN.alihussain64.repl.co?oid={TAK}&uid={baqer}&submit=submit")
 bar=str(requests.get(url).text)
 if 'DONE : ' in bar:
   BB = bar.split('DONE : ')[1]
   LL = BB.split('<hr>')[0]
   good=(f'✅ DONE SEND FOLLOWERS ==> {LL}\n By : @K_K3L')
   bot.send_message(message.chat.id,good)
 elif ('You have to wait until the previous order is completed.') in bar:
   	bad=(f'YOU HAVE 3 ORDER⏳')
   	bot.send_message(message.chat.id,bad)
 else:
   	MM = bar.split('message":"')[1]
   	DD = MM.split('<hr>')[0]
   	bad2=(f'BAD Followers Send ❌\n {DD}')
   	bot.send_message(message.chat.id,bad2)

bot.polling(True)
