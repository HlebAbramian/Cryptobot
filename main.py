import asyncio
from telebot.async_telebot import AsyncTeleBot
from config import *

bot = AsyncTeleBot('bot_link')



@bot.message_handler(commands=['start', 'hello'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} {message.from_user.last_name}')
    
@bot.message_handler(commands=['price'])
async def priceMessage(message):
        await bot.send_message(message.chat.id,f'{price_for_print}')

@bot.message_handler(func=lambda message:True)            
async def main(message):
    if message.text.lower() == 'привет':
        await bot.send_message(message.chat.id, f'Glad to see you, {message.from_user.first_name} {message.from_user.last_name}')
        
    elif message.text.lower() == 'id':
        await bot.reply_to(message, f'id {message.from_user.id}')
        
    else:
        await bot.send_message(message.chat.id, message.text)
        
async def run():
    await asyncio.gather(
        bot.infinity_polling(),
    )

asyncio.run(run())
