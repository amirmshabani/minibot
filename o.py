import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
RENDER_URL = os.environ["RENDER_URL"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! به ربات خوش اومدی 👋\nبرای ادامه وارد مینی اپ بشید"
    )


app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 10000)),
    url_path=BOT_TOKEN,
    webhook_url=f"{RENDER_URL}/{BOT_TOKEN}",
)
