import os
import threading
import asyncio
import time
from flask import Flask
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# --- SERVIDOR FLASK ---
app = Flask(__name__)
@app.route('/')
def home(): return "SISTEMA OK", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- CONFIGURAÇÕES ---
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
GRUPO_ID = "-1002167637171"
MEU_ID_DONO = 5918744817
LINK_PAGAR = "https://pay.infinitepay.io/vippagamentos25/25,00"
LINK_PORTAL = "https://Vipproibidao.short.gy/jfneGR"
LINK_SUPORTE = "https://t.me/TetrispagBot"

TEXTO = (
    "🔞 *ACESSO VITALÍCIO - VIP PROIBIDÃO* 🔞\n\n"
    f"🔗 *PORTAL:* {LINK_PORTAL}\n"
    "💎 *BENEFÍCIO:* Pagamento Único (Vitalício)\n"
    "💳 *VALOR:* R$ 25,00\n\n"
    "✅ *APROVAÇÃO IMEDIATA!*"
)
BOTAO = InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAR)]])

# --- FUNÇÃO DE ESCUTA (PRIVADO) ---
async def escutar_mensagens(bot):
    offset = 0
    while True:
        try:
            updates = await bot.get_updates(offset=offset, timeout=10)
            for update in updates:
                if update.message and update.message.text:
                    msg = update.message.text
                    u_id = update.message.from_user.id
                    
                    if "/start" in msg:
                        await bot.send_video(chat_id=u_id, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                    elif "/suporte" in msg:
                        await bot.send_message(chat_id=u_id, text=f"🆘 Suporte aqui: {LINK_SUPORTE}")
                    elif "/postar" in msg and u_id == MEU_ID_DONO:
                        await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                        await bot.send_message(chat_id=u_id, text="✅ Postado no grupo!")
                
                offset = update.update_id + 1
        except Exception:
            await asyncio.sleep(2)

# --- FUNÇÃO DE POSTAGEM (GRUPO) ---
async def postagem_automatica(bot):
    while True:
        try:
            await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
            await asyncio.sleep(5400) # 1 hora e meia
        except Exception:
            await asyncio.sleep(10)

async def main():
    bot = Bot(token=TOKEN)
    # Roda as duas funções ao mesmo tempo
    await asyncio.gather(escutar_mensagens(bot), postagem_automatica(bot))

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(main())
