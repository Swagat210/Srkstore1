from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import *

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Subscribe ₹99 / 30 Days", callback_data="pay")]
    ]
    await update.message.reply_text(
        "Premium Content Unlock 🔓",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def pay(update: Update, context):
    query = update.callback_query
    await query.answer()
    text = f"""
Pay ₹{PLAN_PRICE}

UPI ID:
{UPI_ID}

After payment send your *UTR number*
"""
    await query.message.reply_text(text, parse_mode="Markdown")

async def utr_handler(update: Update, context):
    utr = update.message.text
    if len(utr) < 10:
        await update.message.reply_text("❌ Invalid UTR")
        return

    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"User {update.message.from_user.id} paid\nUTR: {utr}"
    )

    await update.message.reply_text("✅ Payment received\nAccess granted")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(pay, pattern="pay"))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, utr_handler))
app.run_polling()
