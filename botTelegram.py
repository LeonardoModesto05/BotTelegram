from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from transformers import pipeline 

gerador = pipeline("text-generation", model= "microsoft/DialoGPT-small")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    entrada = update.message.text.strip()
    resposta = gerador(f"Usuário: {entrada}\nBot:", max_length=50, do_sample=True)[0]['generated_text']
    await update.message.reply_text(resposta.split("Bot:")[-1].strip())
    
app = ApplicationBuilder().token("7696267489:AAEfUH3ikmP4UllQnhUMOXQWTrp8vysUCs0").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,responder))
print("Bot está rodando...")
app.run_polling()


