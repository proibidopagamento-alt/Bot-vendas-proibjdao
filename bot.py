import os
import threading
import asyncio
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- CONFIGURAÇÃO DO SERVIDOR FLASK (PARA O RENDER NÃO DORMIR) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot VIP Online e Ativo!"

def run_flask():
    # Tenta usar a porta 10000, se estiver ocupada pula para a próxima
    port = int(os.environ.get("PORT", 10000))
    while True:
        try:
            app.run(host='0.0.0.0', port=port)
            break
        except Exception:
            port += 1

# --- CONFIGURAÇÕES DO SEU BOT ---
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO_URL = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
ID_GRUPO_FREE = "-1002167637171"
LINK_CURTO = "Https://Vipproibidao.short.gy/jfneGR"
LINK_PAGAMENTO = "https://pay.infinitepay.io/vippagamentos25/25,00"

# Texto formatado com o seu novo link curto
TEXTO_VENDA = (
    "🔞 *ACESSO LIBERADO - VIP PROIBIDÃO* 🔞\n\n"
    "Para garantir sua vaga, acesse nosso portal:\n"
    f"🔗 {LINK_CURTO}\n\n"
    "💳 *VALOR: R$ 25,00* (Pix ou Cartão)\n"
    "✅ *APROVAÇÃO AUTOMÁTICA E IMEDIATA!*"
)

# Botão que vai embaixo do vídeo
BOTAO_COMPRAR = InlineKeyboardMarkup([
    [InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAMENTO)]
])

# --- FUNÇÕES DO BOT ---

# Quando alguém clica em /start no privado
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_video(
            video=VIDEO_URL, 
            caption=TEXTO_VENDA, 
            reply_markup=BOTAO_COMPRAR, 
            parse_mode='Markdown'
        )
    except Exception as e:
        print(f"Erro no privado: {e}")

# Função que envia no grupo automaticamente
async def postagem_automatica(context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_video(
            chat_id=ID_GRUPO_FREE, 
            video=VIDEO_URL, 
            caption=TEXTO_VENDA, 
            reply_markup=BOTAO_COMPRAR, 
            parse_mode
