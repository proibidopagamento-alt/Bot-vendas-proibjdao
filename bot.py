import os
import threading
import time
import asyncio
from flask import Flask
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# 1. SERVIDOR PARA MANTER O RENDER VIVO
app = Flask(__name__)
@app.route('/')
def home(): return "OK", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. CONFIGURAÇÕES
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
GRUPO_ID = "-1002167637171"
LINK_PAGAR = "https://pay.infinitepay.io/vippagamentos25/25,00"
LINK_PORTAL = "https://Vipproibidao.short.gy/jfneGR"

TEXTO = (
    "🔞 *ACESSO VITALÍCIO - VIP PROIBIDÃO* 🔞\n\n"
    f"🔗 *PORTAL:* {LINK_PORTAL}\n"
    "💎 *BENEFÍCIO:* Pagamento Único (Vitalício)\n"
    "💳 *VALOR:* R$ 25,00\n\n"
    "✅ *APROVAÇÃO IMEDIATA!*"
)

BOTAO = InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAR)]])

# 3. FUNÇÃO PRINCIPAL (SEM UPDATER PARA NÃO DAR ERRO)
async def iniciar_bot():
    bot = Bot(token=TOKEN)
    offset = 0
    ultima_postagem = 0
    print("SISTEMA INICIADO")

    while True:
        try:
            # Postagem automática no grupo
            agora = time.time()
            if agora - ultima_postagem > 5400: # 90 minutos
                await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                ultima_postagem = agora

            # Resposta ao /start
            updates = await bot.get_updates(offset=offset, timeout=5)
            for update in updates:
                if update.message and update.message.text == "/start":
                    await bot.send_video(chat_id=update.message.chat_id, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                offset = update.update_id + 1
        except Exception as e:
            print(f"Aguardando conexão... {e}")
            await asyncio.sleep(5)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(iniciar_bot())
    rTrTTrrTrTTrTrTr
