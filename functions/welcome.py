from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# توکن ربات خود را وارد کنید
TOKEN = "7834155788:AAFToNhIee9iKCAld_NCHbPZBNhVXBJszjg"

def start(update: Update, context: CallbackContext) -> None:
    welcome_message = (
        "✨ **-این کلاغ سایه‌ای از آینده است-** ✨\n\n"
        "🌪 **-زمزمه‌های بازار را پیش از آنکه طوفان آغاز شود، شنیده است…-** 🌪\n\n"
        "📩 **برای دسترسی به ربات، با آیدی زیر هماهنگ کنید:**\n"
        "@ShraderSupport"
    )
    update.message.reply_text(welcome_message, parse_mode="Markdown")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
