from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


def start(code: Update, context: CallbackContext):
    # update.message.reply_text(f'Hello {update.effective_user.first_name}')
    user = code.message.from_user
    # print(update.message.message_id)
    print(code.message.video)
    code.message.reply_text(f"Assalomu alaykum {user.first_name}\n@{user.username} ")
    print(user.username)
def exo(update: Update, context: CallbackContext):
    msg = update.message.text
    update.message.reply_text(msg)
    if "Salom" == msg:
        update.message.reply_text(msg)



updater = Updater('5229777365:AAE7c4SpNHK1L9Zh4GwxzClq2ZThE-J9BWs')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, exo))

updater.start_polling()
updater.idle()

