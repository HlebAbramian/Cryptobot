import telebot
import webbrowser

bot = telebot.TeleBot('6840452025:AAHXohXJHFvXA-1Fj5GlNejtJ6IlfmdBV80')


@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://Bybit.com')


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} {message.from_user.last_name}')



@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Glad to see you, {message.from_user.first_name} {message.from_user.last_name}')
        
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id {message.from_user.id}')
        
    else: bot.send_message(message.chat.id, message.text)



    
bot.infinity_polling()


#Тестирую гит 