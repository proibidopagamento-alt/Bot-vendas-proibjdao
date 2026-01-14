import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Servidor Flask para manter o Render ativo
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot VIP Online!"

def run_flask():
    # Tenta usar a porta 10000 ou a próxima disponível
    port = int(os.environ.get("PORT", 10000))
    while True:
        try:
            app.run(host='0.0.0.0', port=port)
            break
        except Exception:
            port += 1

# Configurações do seu Bot
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO_URL = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
ID_GRUPO_FREE = "-1002167637171"
LINK_PAGAMENTO = "https://pay.infinitepay.io/vippagamentos25/25,00"

TEXTO_VENDA = (
    "🔞 *ACESSO LIBERADO - VIP PROIBIDÃO* 🔞\n\n"
    "Clique no botão abaixo para realizar o pagamento seguro via *InfinitePay*.\n\n"
    "💳 *Valor: R$ 25,00* (Pix ou Cartão)\n"
    "✅ *Aprovação automática e imediata!*"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAMENTO)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_video(video=VIDEO_URL, caption=TEXTO_VENDA, reply_markup=reply_markup, parse_mode='Markdown')

async def postagem_automatica(context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAMENTO)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_video(chat_id=ID_GRUPO_FREE, video=VIDEO_URL, caption=TEXTO_VENDA, reply_markup=reply_markup, parse_mode='Markdown')

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    # Postagem automática a cada 90 minutos (5400 segundos)
    job_queue = application.job_queue
    job_queue.run_repeated(postagem_automatica, interval=5400, first=10)

    application.run_polling()
    
