import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Lấy token từ biến môi trường
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Hàm xử lý /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào 👋! Tôi là bot Telegram 🚀 (Render)")

# Hàm xử lý /hello
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋, chúc bạn một ngày tốt lành!")

# Hàm xử lý tin nhắn thường
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bạn vừa nói: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()

    # Gán các command
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))  # 🆕 thêm lệnh mới
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
