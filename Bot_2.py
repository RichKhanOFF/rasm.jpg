# from telegram import Update
# from telegram.ext import Updater, CommandHandler,CallbackContext, MessageHandler, Filters, ConversationHandler
#
#
# def start(update:Update, context: CallbackContext):
#     update.message.reply_text(f"Assalomu alaykum")
#
# def main():
#     TOKENT = "5229777365:AAE7c4SpNHK1L9Zh4GwxzClq2ZThE-J9BWs"
#
#     updater = Updater(TOKENT)
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states = {
#
#
#         },
#         fallbacks = []
#     )
#     updater.dispatcher.add_handler(all_handler)
#     updater.start_polling()
#     updater.idle()
#
# if __name__=="__main__":
#     main()
#










# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
#
#
# def start(updater:Update, context: CallbackContext):
#     updater.message.reply_text("Assalomu alaykum\n\n Ism yozing ✍️ ")
#     return 1
#
# def name(updater:Update, context: CallbackContext):
#     ism = updater.message.text
#     user = updater.message.from_user
#     with open(f"{user.id}.text", 'w') as f:
#         f.write(f"\nMijozni ismi: {ism}")
#     updater.message.reply_text("Fam yozing! ✍️ ")
#
#     return 2
# def surname(updater:Update, context: CallbackContext):
#     fam = updater.message.text
#     user = updater.message.from_user
#
#     with open(f"{user.id}.text", 'a') as f:
#         f.write(f"\nMijozni Fam: {fam}")
#
#     with open(f"{user.id}.text", "r") as f:
#         info = f.read()
#         updater.message.reply_text(f"ID:{user.id}\n\nKiritilgan ma'lumot tug'rimi!: {info}")
#
#
#     return 3
# def age(updater:Update, context: CallbackContext):
#     yoshi = updater.message.text
#     print("3", yoshi)
#
# def main():
#     TOKENT = "5229777365:AAE7c4SpNHK1L9Zh4GwxzClq2ZThE-J9BWs"
#
#     updater = Updater(TOKENT)
#
#     all_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states = {
#             1 : [MessageHandler(Filters.text, name)],
#             2 : [MessageHandler(Filters.text, surname)],
#             3 : [MessageHandler(Filters.text, age)]
#
#         },
#         fallbacks = []
#     )
#     updater.dispatcher.add_handler(all_handler)
#     updater.start_polling()
#     updater.idle()
#
# if name=="main":
#     main()




from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler


def start(updater:Update, context:CallbackContext):
    info_button = [
        [KeyboardButton("🍴 Menyu")],
        [KeyboardButton("🛍 Mening buyurtmalarim")],
        [KeyboardButton("✍️ Fikr bildirish"), KeyboardButton("⚙️ Sozlamalar") ]
    ]
    updater.message.reply_text("Quydagilardan birini tanlang..", reply_markup=ReplyKeyboardMarkup(info_button, resize_keyboard=True))

    return 1
def post_message(updater:Update, context:CallbackContext):
    msg = updater.message.text
    updater.message.reply_text(f"{msg}ga O'tildi")

    updater.message.reply_text(f"{msg} bo'limiga")






def main():
    TOKENT = "5229777365:AAE7c4SpNHK1L9Zh4GwxzClq2ZThE-J9BWs"

    updater = Updater(TOKENT)


    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states = {
                1: [MessageHandler(Filters.text, post_message)]
        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updaterx.idle()

if __name__ == "main":
    main()