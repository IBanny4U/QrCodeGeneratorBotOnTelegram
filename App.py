import qrcode;
import os;
import io;


# load_dotenv read .env file 
from dotenv import load_dotenv 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


load_dotenv()

APIToken = os.getenv("Bot_Token");


# /start command handler
async def start(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a link and I'll generate a QR code!")

# Handle normal text messages
async def generate_qr(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("http"):


        # Generate QR code
        img = qrcode.make(text)
        bio = io.BytesIO()
        bio.name = "qr.png"
        img.save(bio, "PNG")
        bio.seek(0)




        await update.message.reply_photo(photo=bio, caption="Here’s your QR code!")
    else:
        await update.message.reply_text("Please send a valid link starting with https:")

def main():


    # Create the bot application
    app = Application.builder().token(APIToken).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_qr))

    # Run the bot
    app.run_polling()



if __name__ == "__main__":
    main()
