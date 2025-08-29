import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Lấy token từ biến môi trường Heroku
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Hàm xử lý /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào 👋! Tôi là bot Telegram 🚀")

# Hàm xử lý tin nhắn thường
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bạn vừa nói: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()

    # Gán lệnh /start
    app.add_handler(CommandHandler("start", start))
    # Gán xử lý tin nhắn
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot đang chạy trên Heroku...")
    app.run_polling()

if __name__ == "__main__":
    main()
