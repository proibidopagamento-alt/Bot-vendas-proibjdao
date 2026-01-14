import os
import threading
import asyncio
import time
import requests
from flask import Flask
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# 1. SERVIDOR FLASK (PARA O RENDER NÃO DORMIR)
app = Flask(__name__)
@app.route('/')
def home(): return "SISTEMA VIP ATIVO", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. CONFIGURAÇÕES GERAIS
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
GRUPO_ID = "-1002167637171"
MEU_ID_DONO = 5918744817  # Seu ID verificado
LINK_PAGAR = "https://pay.infinitepay.io/vippagamentos25/25,00"
LINK_PORTAL = "https://Vipproibidao.short.gy/jfneGR"
LINK_SUPORTE = "https://t.me/TetrispagBot" # Link do Suporte

TEXTO = (
    "🔞 *ACESSO VITALÍCIO - VIP PROIBIDÃO* 🔞\n\n"
    "Pague apenas uma vez e tenha acesso para sempre!\n\n"
    f"🔗 *PORTAL:* {LINK_PORTAL}\n"
    "💎 *BENEFÍCIO:* Pagamento Único (Vitalício)\n"
    "💳 *VALOR:* R$ 25,00\n\n"
    "✅ *APROVAÇÃO IMEDIATA!*"
)

BOTAO = InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAR)]])

# 3. FUNÇÃO DE LOOP (ESCUTA PRIVADO E POSTA NO GRUPO)
async def iniciar_bot():
    bot = Bot(token=TOKEN)
    offset = 0
    # Define a primeira postagem para 10 segundos após ligar
    proxima_postagem = time.time() + 10 
    
    print("=== BOT INICIADO E ESCUTANDO COMANDOS ===")

    while True:
        try:
            # A. POSTAGEM AUTOMÁTICA (A cada 90 minutos)
            agora = time.time()
            if agora >= proxima_postagem:
                try:
                    await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                    print("Postagem automática realizada!")
                except Exception as e:
                    print(f"Erro ao postar no grupo: {e}")
                proxima_postagem = agora + 5400 # Agenda próxima para daqui a 1h30

            # B. VERIFICAR MENSAGENS (START, POSTAR, SUPORTE)
            updates = await bot.get_updates(offset=offset, timeout=10)
            for update in updates:
                if update.message and update.message.text:
                    msg = update.message.text
                    chat_id = update.message.chat_id
                    user_id = update.message.from_user.id

                    # Resposta ao /start
                    if "/start" in msg:
                        await bot.send_video(chat_id=chat_id, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                    
                    # Comando manual /postar (SÓ PARA VOCÊ)
                    elif "/postar" in msg:
                        if user_id == MEU_ID_DONO:
                            await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                            await bot.send_message(chat_id=chat_id, text="✅ Comando recebido! Postado no grupo.")
                        else:
                            await bot.send_message(chat_id=chat_id, text="❌ Acesso negado.")

                    # Comando /suporte
                    elif "/suporte" in msg:
                        await bot.send_message(chat_id=chat_id, text=f"🆘 Suporte: {LINK_SUPORTE}")

                offset = update.update_id + 1
        
        except Exception as e:
            # Se der erro de conexão, aguarda 5 segundos e tenta de novo
            print(f"Erro no loop: {e}")
            await asyncio.sleep(5)

if __name__ == '__main__':
    # Roda o Flask em uma Thread separada
    threading.Thread(target=run_flask, daemon=True).start()
    # Roda o Bot
    asyncio.run(iniciar_bot())
            
