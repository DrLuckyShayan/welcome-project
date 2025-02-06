from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 🔹 جایگزین کن با توکن رباتت
TOKEN = "7834155788:AAFToNhIee9iKCAld_NCHbPZBNhVXBJszjg"

# 🔸 پیام خوش‌آمدگویی
def start(update: Update, context: CallbackContext) -> None:
    welcome_message = (
        "✨ **-این کلاغ سایه‌ای از آینده است-** ✨\n\n"
        "🌪 **-زمزمه‌های بازار را پیش از آنکه طوفان آغاز شود، شنیده است…-** 🌪\n\n"
        "📩 **برای دسترسی به ربات، با آیدی زیر هماهنگ کنید:**\n"
        "@ShraderSupport"
    )
    update.message.reply_text(welcome_message, parse_mode="Markdown")

# 🔸 اجرای ربات
def main():
    # تنظیم Webhook
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # اضافه کردن دستور /start
    dp.add_handler(CommandHandler("start", start))

    # 🔥 تنظیم Webhook
    PORT = 8443
    APP_NAME = "نام سایت نتلیفای (بدون https و /)"
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://{APP_NAME}.netlify.app/{TOKEN}"
    )

    updater.idle()

# اجرای کد
if __name__ == "__main__":
    main()
