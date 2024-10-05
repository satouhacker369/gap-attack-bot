import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7392376452:AAFKFiu773qn7hAIBRduBt3G7qqOYGzdeN4'
YOUR_CHAT_ID = '2072129101'

bot = telebot.TeleBot(TOKEN)

inline_Keyboard = InlineKeyboardMarkup(row_width=2)
button = InlineKeyboardButton("چنل اول", url="https://t.me/FastShoVpn")
button2 = InlineKeyboardButton("چنل دوم", url="https://t.me/satoukagenou")
button3 = InlineKeyboardButton("عضو شدم", callback_data="step2")
inline_Keyboard.add(button , button2 , button3)

    
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"سلام! به ربات گپ اتک خوش امدید") 
    bot.send_message(message.chat.id,  "جهت استفاده عضو چنل های سپانسر شوید", reply_markup=inline_Keyboard)


#menu
def main_menu():
    markup = InlineKeyboardMarkup()
    bottun_one = InlineKeyboardButton("🩸 اتک به گپ", callback_data="menu1")
    bottun_two = InlineKeyboardButton("🛒 خریده ویژه", callback_data="menu2")
    markup.add(bottun_one,bottun_two)
    return markup


# Define the submenus for Menu 1
def submenu1():
    markup = types.InlineKeyboardMarkup(row_width=1)
    return_button = types.InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(return_button)
    return markup

@bot.callback_query_handler(func=lambda call: call.data == 'menu1')
def handle_menu1(call):
    bot.send_message(call.message.chat.id, """یدی گپ مورد نظرتو بفرس 💀👇
نکته: بدون(@) بفرست """)
    bot.register_next_step_handler(call.message, receive_first_input)

def receive_first_input(message):
    first_input = message.text
    bot.send_message(message.chat.id, """خب حالا بگو با چی باهاش اتک بزنم 💀✅
نکته؛ فقط متن باشه""")
    bot.register_next_step_handler(message, receive_second_input, first_input)

def receive_second_input(message, first_input):
    markup = InlineKeyboardMarkup(row_width=1)
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(return_button)
    second_input = message.text
    bot.send_message(YOUR_CHAT_ID, f"پیام جدید از کاربر:\nمتن اول: {first_input}\nمتن دوم: {second_input}")
    bot.send_message(message.chat.id, "خب فقط وایسا تا 2 روز اتک بزنم 💀")
    bot.send_message(message.chat.id, "🩸 اگه یه اتک خفن میخوای برات انجام بدیم میتونی اشتراک ویژه ازمون خریداری کنی", reply_markup=markup)

# Define the submenus for Menu 2
def submenu2(message2):
    markup = InlineKeyboardMarkup(row_width=1)
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(return_button)
    bot.send_message(message2.chat.id, """🛒 خریده اشتراک - قیمت اتک ویژه 👇
اتک ویژه 2 ساعته: 30 تومان 💀
اتک ویژه 1 روزه : 50 تومان💀
اتک ویژه 7 روزه : 70 تومان💀
اتک ویژه 1 ماهه : 120 تومان💀

برای خرید 👇
@Thetrueeee""", reply_markup=markup)


@bot.message_handler(commands=['menu'])
def hello(message):
    bot.send_message(message.chat.id,"چی میخوای جیگر؟", reply_markup= main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "step2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="چی میخوای جیگر؟", reply_markup=main_menu())
        
    elif call.data == 'menu1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in menu1", reply_markup=submenu1(call.message))
    
# ta bala ok
    elif call.data == 'menu2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🛒 خریده ویژه", reply_markup=submenu2(call.message))
    
    elif call.data == 'return_to_main':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="به منو برگشتید", reply_markup=main_menu())


# تعریف دستور سفارشی
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id,"سلام! به ربات گپ اتک خوش امدید")
# تعریف پاسخ به پیام‌های متنی
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)
# اجرای ربات
bot.polling(timeout=60)


