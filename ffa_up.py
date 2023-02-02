# -*- coding: utf-8 -*-
import json
import telebot
from telebot import types


TOKEN = '5042498723:AAG-Tm7r6X4Rs0zQrtcL7LMo6_D3SUcdFlc'
bot = telebot.TeleBot(TOKEN, parse_mode='Markdown')
admin_id = 948595155

# mana topdim
def show():
    file = open('namoz_vaq.json', 'r', encoding='utf-8').read()
    main_data = json.loads(file)
    return main_data

@bot.message_handler(commands='start')
def start(message):
    f_name = message.from_user.first_name
    u_id = message.from_user.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('⌚️ Namoz vaqtlari')
    markup.add('🌐 Masjid Ijtimoiy tarmoqlardagi sahifalari')

    bot.reply_to(message, f'''
Assalomu alaykum  {f_name}! Qoriqo'rg'on 🕌 jome masjidining namoz vaqtlari telegram-botiga xush kelibsiz!

*"Namozni to'kis ado etinglar.Albatta Namoz mo'minlarga vaqtida farz qilingandir" (Niso surasi 103-oyat).
Ushbu bot orqali siz -
Andijon shahrida joylashgan "Қори Кўрғон" jome masjidining namoz vaqtlari haqida ma'lumot olishingiz mumkin! 
Do'stlaringizni ham namoz vaqtlaridan xabardor eting!

Bosh imom-hatib: Musajonov Zuhriddin
Murojaat uchun telefon: +998914860103
 
https://t.me/masjidga_marhabo*

''', reply_markup=markup)

@bot.message_handler(regexp='bekor qilish')
def back(message):
    return start(message)

@bot.message_handler(regexp='admin')
def admin_panel(message):
    u_id = message.from_user.id
    if u_id == admin_id:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('bekor qilish')

        text = bot.reply_to(message, '*Salom! Admin\n\nVaqtlarni kiriting:*', reply_markup=markup)
        bot.register_next_step_handler(text, write_to_json)
    else:
        pass


def write_to_json(message):
    try:
        arr = []
        if message.text != 'bekor qilish':
            text = message.text.split('|')
            arr.append(
                {
                    'bomdod': 'Bomdod➡️ ' + text[0],
                    'peshin': 'Peshin➡️ ' + text[1],
                    'asr': 'Asr➡️ ' + text[2],
                    'shom': 'Shom➡️ ' + text[3],
                    'xufton': 'Xufton➡️ ' + text[4]

                }
            )

            with open('namoz_vaq.json', 'w', encoding='utf-8') as f:
                json.dump(arr, f, indent=4, ensure_ascii=False)
                bot.reply_to(message, '*Vaqtlar muvaffaqiyatli yuklandi!!!*')
                return back(message)
    except Exception as e:
        bot.reply_to(message, f'Error: `{e}`')

@bot.message_handler(regexp='🌐 Masjid Ijtimoiy tarmoqlardagi sahifalari')
def ijt_tar(message):
	bot.reply_to(message, '🕌 Masjidning ijtimoy tarmoqlardagi sahifalari bilan quyida keltirilgan havola orqali tanishing\n https://heylink.me/Qoriqorgonijtimoytarmoqlar \nYuqoridagi linkni yaqinlaringizga ulashib, masjidning ijtimoiy tarmoqlardagi sahifalaridan xabardor eting! ✅\n@masjidgamarxabo ')

@bot.message_handler(regexp='Namoz vaqtlari') 
def namoz_times(message):
    u_id = message.from_user.id

    key = types.InlineKeyboardMarkup()
    keys = [
        types.InlineKeyboardButton(text='Bomdod', callback_data='bomdod'),
        types.InlineKeyboardButton(text='Peshin', callback_data='peshin'),
        types.InlineKeyboardButton(text='Asr', callback_data='asr'),
        types.InlineKeyboardButton(text='Shom', callback_data='shom'),
        types.InlineKeyboardButton(text='Xufton', callback_data='xufton')
    ]
    key.add(*keys)

    bot.reply_to(message, '''
*Islom.uz saytida chop etilgan foydali maqolalar 📚
(Muallif: islom.uz / saytidan olindi)
Iymon haqida:\nhttps://islom.uz/iymon/1   \nNamoz haqida batafsil:\n https://islom.uz/namoz/1   \nAzon duosi\nhttps://islom.uz/maqola/9841\n \nBotdagi xato va kamchiliklar,taklif va fikr mulohazalar uchun @xatoliklaruchunBot ga yozing\n@qoriqorgon_namoz_vaqtlariBot
⏳Namoz vaqtlarini bilish uchun quyidagilardan birini tanlang 👇*''', reply_markup=key)


@bot.callback_query_handler(func=lambda c: c.data == 'bomdod')
def bomdod(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    call_id = call.from_user.id

    bot.send_message(call_id, f'''
*{show()[0]['bomdod']}*
''')

@bot.callback_query_handler(func=lambda c: c.data == 'peshin')
def peshin(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    call_id = call.from_user.id

    bot.send_message(call_id, f'''
*{show()[0]['peshin']}*
''')

@bot.callback_query_handler(func=lambda c: c.data == 'asr')
def asr(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    call_id = call.from_user.id

    bot.send_message(call_id, f'''
*{show()[0]['asr']}*
''')

@bot.callback_query_handler(func=lambda c: c.data == 'shom')
def shom(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    call_id = call.from_user.id

    bot.send_message(call_id, f'''
*{show()[0]['shom']}*
''')

@bot.callback_query_handler(func=lambda c: c.data == 'xufton')
def xufton(call: types.CallbackQuery):
    bot.answer_callback_query(call.id)
    call_id = call.from_user.id

    bot.send_message(call_id, f'''
*{show()[0]['xufton']}*
''')


if __name__ == '__main__':
    print('started!')
    bot.polling()

