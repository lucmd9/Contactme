import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot("7487461312:AAH5hmYP0eB_wZLCxJSSfU4upUlCsQHdDGw")

OWNER_ID = 1045489068  
OWNER_NAME = "Angel" 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Developer 🎭", url='https://t.me/V_D_M'),
        InlineKeyboardButton("Channel 🌟", url='https://t.me/ANGTHON'),
        InlineKeyboardButton("Sales 🚀", url='https://t.me/veryiced'),
        InlineKeyboardButton("Music 🎵", url='https://t.me/VerySilentness')        
    )
    
    bot.send_message(
        message.chat.id,
        f"مرحبًا بك في بوت التواصل الخاص بـ [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\nأرسل رسالتك وسيتم الرد بأقرب وقت.",
        reply_markup=markup,
        parse_mode='Markdown'
    )
    bot.send_message(
        OWNER_ID,
        f"قام شخص بالدخول للبوت الخاص بك\n\n{message.from_user.username}\nايديه : {message.from_user.id}"
    )

@bot.message_handler(commands=['رد'])
def reply_to_user(message):
    if message.from_user.id == OWNER_ID:
        args = message.text.split(maxsplit=2)
        if len(args) > 2:
            user_id = args[1]
            reply_text = args[2]
            bot.send_message(user_id, reply_text)
            bot.reply_to(message, "- تم ارسال رسالتك بنجاح ")
        else:
            bot.reply_to(message, "- يرجى استخدام الأمر بشكل صحيح. على سبيل المثال: /رد ايدي_الشخص الرسالة")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def forward_to_owner(message):
    if message.from_user.id != OWNER_ID:
        username = message.from_user.username if message.from_user.username else "بدون معرف"
        bot.send_message(
            OWNER_ID,
            f"- رسالة واردة من {username}\n- معرفه : @{username}\n- ايديه : {message.from_user.id}\n\n{message.text}\n\n- للرد عليه فقط ارسل رسالتك وقم بالرد على رسالتك بالأمر التالي [/رد + يوزر الشخص + الرسالة]"
        )
        bot.send_message(
            message.chat.id,
            "- تم استلام رسالتك بنجاح. سيتم الرد عليك في أقرب وقت ممكن."
        )


print("Working⚡")
bot.polling()
