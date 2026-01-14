import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- SERVIDOR FLASK ---
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot Online", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- CONFIGURAÇÕES ---
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

# --- FUNÇÕES ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_video(chat_id=update.effective_chat.id, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')

async def postar_no_grupo(context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
    except Exception as e:
        print(f"Erro no grupo: {e}")

# --- EXECUÇÃO ---
if __name__ == '__main__':
    # Inicia o Flask
    threading.Thread(target=run_flask, daemon=True).start()

    # Inicia o Bot (Forma recomendada para evitar AttributeError)
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    # Postagem automática (90 minutos)
    job_queue = application.job_queue
    job_queue.run_repeated(postar_no_grupo, interval=5400, first=10)

    print("Iniciando Polling...")
    application.run_polling(drop_pending_updates=True)
    
