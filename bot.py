import os
import threading
import asyncio
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

# 1. Servidor Flask (Para o Render ficar Live)
app = Flask(__name__)

@app.route('/')
def index():
    return "BOT ONLINE"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. Configurações do Bot
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
GRUPO_ID = "-1002167637171"
LINK_PAGAR = "https://pay.infinitepay.io/vippagamentos25/25,00"
LINK_PORTAL = "https://Vipproibidao.short.gy/jfneGR"

TEXTO = (
    "🔞 *ACESSO VITALÍCIO - VIP PROIBIDÃO* 🔞\n\n"
    "Pague apenas uma vez e tenha acesso para sempre!\n\n"
    f"🔗 *PORTAL:* {LINK_PORTAL}\n"
    "💎 *BENEFÍCIO:* Pagamento Único\n"
    "💳 *VALOR:* R$ 25,00\n\n"
    "✅ *APROVAÇÃO IMEDIATA!*"
)

BOTAO = InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAR)]])

# 3. Funções de Resposta
async def start(update, context):
    await update.message.reply_video(video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')

async def postar(context):
    await context.bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')

# 4. Inicialização Segura
if __name__ == '__main__':
    # Inicia o Flask em segundo plano
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()

    # Inicia o Telegram
    app_bot = Application.builder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    
    # Postagem automática (90 min)
    app_bot.job_queue.run_repeated(postar, interval=5400, first=10)

    print("Bot rodando...")
    app_bot.run_polling()
