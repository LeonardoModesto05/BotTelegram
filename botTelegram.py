import spacy
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

nlp = spacy.load("pt_core_news_sm")
##pega dados da mensagem recebida e responde o usuario
async def responder (update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message.text.lower()
    doc = nlp(mensagem)
##verifica se tem alguma mensagem de saudações
    if any(token.text in ["oi", "olá", "eae", "eai", "e ai"] for token in doc):
        await update.message.reply_text("Oi! Como posso te ajudar?")
##verifica se tem algum nome na mensagem  
    elif any(ent.label_ == "PER" for ent in doc.ents):
        nomes = [ent.text for ent in doc.ents if ent.label == "PER"]
        await update.message.reply_text(f"Prazer em conhecer voce{' e '.join(nomes)}!")
    elif any(token.text in ["tchau","xau","falou","flw","até mais"]for token in doc):
        await update.message.reply_text(f"Tchau! Até Mais!")
    elif "bom dia" in mensagem:
        await update.message.reply_text("Bom dia!Tenha um ótimo dia!")
    elif "boa tarde" in mensagem:
        await update.message.reply_text("Boa tarde!")
    elif "boa noite" in mensagem:
        await update.message.reply_text("Boa noite!")
    
    else:
        await update.message.reply_text("Desculpa, não entendi sua mensagem. ")
    
app = ApplicationBuilder().token("7696267489:AAEfUH3ikmP4UllQnhUMOXQWTrp8vysUCs0").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,responder))
print("Bot está rodando...")
app.run_polling()


