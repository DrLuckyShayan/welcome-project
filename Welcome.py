from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

# 🔹 جایگزین کن با توکن رباتت
TOKEN = "7834155788:AAFToNhIee9iKCAld_NCHbPZBNhVXBJszjg"
bot = Bot(token=TOKEN)

# 🔸 پیام خوش‌آمدگویی
def start(update: Update, context) -> None:
    welcome_message = (
        "✨ **-این کلاغ سایه‌ای از آینده است-** ✨\n\n"
        "🌪 **-زمزمه‌های بازار را پیش از آنکه طوفان آغاز شود، شنیده است…-** 🌪\n\n"
        "📩 **برای دسترسی به ربات، با آیدی زیر هماهنگ کنید:**\n"
        "@ShraderSupport"
    )
    update.message.reply_text(welcome_message, parse_mode="Markdown")

# 🔸 راه‌اندازی Flask برای Webhook
app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler("start", start))

    # دریافت آپدیت‌های تلگرام
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)

    # پردازش دستور /start
    dispatcher.process_update(update)
    return "OK"

# 🔸 اجرای Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
