import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Servidor Flask para o Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Online"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Configurações
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO_URL = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
ID_GRUPO = "-1002167637171"
LINK_PAGAMENTO = "https://pay.infinitepay.io/vippagamentos25/25,00"
LINK_CURTO = "Https://Vipproibidao.short.gy/jfneGR"

TEXTO = (
    "🔞 *ACESSO LIBERADO - VIP PROIBIDÃO* 🔞\n\n"
    f"🔗 Acesse: {LINK_CURTO}\n\n"
    "💳 *VALOR: R$ 25,00*\n"
    "✅ *APROVAÇÃO IMEDIATA!*"
)

BOTAO = InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAMENTO)]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_video(video=VIDEO_URL, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')

async def postar(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_video(chat_id=ID_GRUPO, video=VIDEO_URL, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.job_queue.run_repeated(postar, interval=5400, first=10)
    application.run_polling()
