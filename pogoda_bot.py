from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS

a = requests.get('https://sinoptik.ua/погода-ташкент')
html_a = BS(a.content, 'html.parser')
for el in html_a.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    a_min = min[4:]
    a_max = max[5:]



b = requests.get('https://sinoptik.ua/погода-андижан')
html_b = BS(b.content, 'html.parser')
for el in html_b.select('#content'):
    min_2 = el.select('.temperature .min')[0].text
    max_2 = el.select('.temperature .max')[0].text
    b_min = min_2[4:]
    b_max = max_2[5:]



c = requests.get('https://sinoptik.ua/погода-бухара')
html_c = BS(c.content, 'html.parser')
for el in html_c.select('#content'):
    min_3 = el.select('.temperature .min')[0].text
    max_3 = el.select('.temperature .max')[0].text
    c_min = min_3[4:]
    c_max = max_3[5:]



d = requests.get('https://sinoptik.ua/погода-фергана')
html_d = BS(d.content, 'html.parser')
for el in html_d.select('#content'):
    min_4 = el.select('.temperature .min')[0].text
    max_4 = el.select('.temperature .max')[0].text
    d_min = min_4[4:]
    d_max = max_4[5:]



e = requests.get('https://sinoptik.ua/погода-джизак')
html_e = BS(e.content, 'html.parser')
for el in html_e.select('#content'):
    min_5 = el.select('.temperature .min')[0].text
    max_5 = el.select('.temperature .max')[0].text
    e_min = min_5[4:]
    e_max = max_5[5:]



f = requests.get('https://sinoptik.ua/погода-ургенч')
html_f = BS(f.content, 'html.parser')
for el in html_f.select('#content'):
    min_6 = el.select('.temperature .min')[0].text
    max_6 = el.select('.temperature .max')[0].text
    f_min = min_6[4:]
    f_max = max_6[5:]



g = requests.get('https://sinoptik.ua/погода-наманган')
html_g = BS(g.content, 'html.parser')
for el in html_g.select('#content'):
    min_7 = el.select('.temperature .min')[0].text
    max_7 = el.select('.temperature .max')[0].text
    g_min = min_7[4:]
    g_max = max_7[5:]



h = requests.get('https://sinoptik.ua/погода-навои')
html_h = BS(h.content, 'html.parser')
for el in html_h.select('#content'):
    min_8 = el.select('.temperature .min')[0].text
    max_8 = el.select('.temperature .max')[0].text
    h_min = min_8[4:]
    h_max = max_8[5:]



i = requests.get('https://sinoptik.ua/узбекистан/кашкадарьинская-область')
html_i = BS(c.content, 'html.parser')
for el in html_c.select('#content'):
    min_9 = el.select('.temperature .min')[0].text
    max_9 = el.select('.temperature .max')[0].text
    i_min = min_9[4:]
    i_max = max_9[5:]



j = requests.get('https://sinoptik.ua/погода-нукус')
html_j = BS(j.content, 'html.parser')
for el in html_j.select('#content'):
    min_10 = el.select('.temperature .min')[0].text
    max_10 = el.select('.temperature .max')[0].text
    j_min = min_10[4:]
    j_max = max_10[5:]



k = requests.get('https://sinoptik.ua/погода-самарканд')
html_k = BS(k.content, 'html.parser')
for el in html_k.select('#content'):
    min_11 = el.select('.temperature .min')[0].text
    max_11 = el.select('.temperature .max')[0].text
    k_min = min_11[4:]
    k_max = max_11[5:]



l = requests.get('https://sinoptik.ua/погода-сырдарья')
html_l = BS(l.content, 'html.parser')
for el in html_l.select('#content'):
    min_12 = el.select('.temperature .min')[0].text
    max_12 = el.select('.temperature .max')[0].text
    l_min = min_12[4:]
    l_max = max_12[5:]



m = requests.get('https://sinoptik.ua/погода-термез')
html_m = BS(m.content, 'html.parser')
for el in html_m.select('#content'):
    min_13 = el.select('.temperature .min')[0].text
    max_13 = el.select('.temperature .max')[0].text
    m_min = min_13[4:]
    m_max = max_13[5:]



n = requests.get('https://sinoptik.ua/погода-ташкент')
html_n = BS(n.content, 'html.parser')
for el in html_n.select('#content'):
    min_14 = el.select('.temperature .min')[0].text
    max_14 = el.select('.temperature .max')[0].text
    n_min = min_14[4:]
    n_max = max_14[5:]



def city():
    return [
        [InlineKeyboardButton("Toshkent shaxri", callback_data=f"01")],
        [InlineKeyboardButton("Andijon viloyati", callback_data=f"02")],
        [InlineKeyboardButton("Buxoro viloyati", callback_data=f"03")],
        [InlineKeyboardButton("Fargʻona viloyati", callback_data=f"04")],
        [InlineKeyboardButton("Jizzax viloyati", callback_data=f"05")],
        [InlineKeyboardButton("Xorazm viloyati", callback_data=f"06")],
        [InlineKeyboardButton("Namangan viloyati", callback_data=f"07")],
        [InlineKeyboardButton("Navoiy viloyati", callback_data=f"08")],
        [InlineKeyboardButton("Qashqadaryo viloyati", callback_data=f"09")],
        [InlineKeyboardButton("Qoraqalpogʻiston respublikasi", callback_data=f"10")],
        [InlineKeyboardButton("Samarqand viloyati", callback_data=f"11")],
        [InlineKeyboardButton("Sirdaryo viloyati", callback_data=f"12")],
        [InlineKeyboardButton("Surxondaryo viloyati", callback_data=f"13")],
        [InlineKeyboardButton("Toshkent viloyati", callback_data=f"14")]
    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"Bugun Toshkent shaxrida havo o`zgarib turadi\nmin {a_min}\nmax "
                                f"{a_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "02":
        query.message.edit_text(f"Bugun Andijon viloyatida havo o`zgarib turadi\nmin {b_min}\nmax "
                                f"{b_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "03":
        query.message.edit_text(f"Bugun Buxoro viloyatida havo o`zgarib turadi\nmin {c_min}\nmax "
                                f"{c_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "04":
        query.message.edit_text(f"Bugun Fargʻona viloyatida havo o`zgarib turadi\nmin {d_min}\nmax "
                                f"{d_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "05":
        query.message.edit_text(f"Bugun Jizzax viloyatida havo o`zgarib turadi\nmin {e_min}\nmax "
                                f"{e_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "06":
        query.message.edit_text(f"Bugun Xorazm viloyatida havo o`zgarib turadi\nmin {f_min}\nmax "
                                f"{f_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "07":
        query.message.edit_text(f"Bugun Namangan viloyatida havo o`zgarib turadi\nmin {g_min}\nmax "
                                f"{g_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "08":
        query.message.edit_text(f"Bugun Navoiy viloyatida havo o`zgarib turadi\nmin {h_min}\nmax "
                                f"{h_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "09":
        query.message.edit_text(f"Bugun Qashqadaryo viloyatida havo o`zgarib turadi\nmin {i_min}\nmax "
                                f"{i_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "10":
        query.message.edit_text(f"Bugun Qoraqalpogʻiston Respublikasida havo o`zgarib turadi\nmin {j_min}\nmax "
                                f"{j_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "11":
        query.message.edit_text(f"Bugun Samarqand viloyatida havo o`zgarib turadi\nmin {k_min}\nmax "
                                f"{k_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "12":
        query.message.edit_text(f"Bugun Sirdaryo viloyatida havo o`zgarib turadi\nmin {l_min}\nmax "
                                f"{l_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "13":
        query.message.edit_text(f"Bugun Surxondaryo viloyatida havo o`zgarib turadi\nmin {m_min}\nmax "
                                f"{m_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "14":
        query.message.edit_text(f"Bugun Toshkent viloyatida havo o`zgarib turadi\nmin {n_min}\nmax "
                                f"{n_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))


    elif data[0] == 'back1':
        query.message.edit_text(
            f"Bu yerdan Shahar yoki viloyatni tanlang 👇",
            reply_markup=InlineKeyboardMarkup(city()))


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Assalomu alaykum {user.first_name} 🖐🏼\nBu yerdan Shahar yoki viloyatni tanlang 👇""",
                              reply_markup=InlineKeyboardMarkup(city()))


def main():
    Token = "5256988312:AAHyO3pF-vEySzAjXlpjwTJmvAZUGNRYUTQ"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()