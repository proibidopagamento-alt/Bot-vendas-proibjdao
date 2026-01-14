import os
import threading
import asyncio
import time
from flask import Flask
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# 1. Servidor Flask (Mantém o Render 'Live')
app = Flask(__name__)
@app.route('/')
def home(): return "SISTEMA ATIVO", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. Configurações Finais
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
GRUPO_ID = "-1002167637171"
MEU_ID_DONO = 5918744817  # O SEU ID DE DONO
LINK_PAGAR = "https://pay.infinitepay.io/vippagamentos25/25,00"
LINK_PORTAL = "https://Vipproibidao.short.gy/jfneGR"
LINK_SUPORTE = "https://t.me/TetrispagBot" # <-- Pode mudar para o seu @ pessoal se preferir

TEXTO = (
    "🔞 *ACESSO VITALÍCIO - VIP PROIBIDÃO* 🔞\n\n"
    "Pague apenas uma vez e tenha acesso para sempre!\n\n"
    f"🔗 *PORTAL:* {LINK_PORTAL}\n"
    "💎 *BENEFÍCIO:* Pagamento Único (Vitalício)\n"
    "💳 *VALOR:* R$ 25,00\n\n"
    "✅ *APROVAÇÃO IMEDIATA!*"
)

BOTAO = InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR R$ 25,00 AGORA", url=LINK_PAGAR)]])

# 3. Função Principal com Comandos e Segurança
async def iniciar_bot():
    bot = Bot(token=TOKEN)
    offset = 0
    ultima_postagem = 0
    print("Bot Protegido Iniciado...")

    while True:
        try:
            # Postagem Automática (a cada 90 min)
            agora = time.time()
            if agora - ultima_postagem > 5400:
                await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                ultima_postagem = agora

            # Ouvindo comandos
            updates = await bot.get_updates(offset=offset, timeout=5)
            for update in updates:
                if update.message and update.message.text:
                    msg = update.message.text
                    chat_id = update.message.chat_id
                    user_id = update.message.from_user.id

                    # COMANDO /START
                    if "/start" in msg:
                        await bot.send_video(chat_id=chat_id, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                    
                    # COMANDO /POSTAR (COM TRAVA DE SEGURANÇA)
                    elif "/postar" in msg:
                        if user_id == MEU_ID_DONO:
                            await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO, reply_markup=BOTAO, parse_mode='Markdown')
                            await bot.send_message(chat_id=chat_id, text="✅ Postagem manual enviada ao grupo!")
                        else:
                            await bot.send_message(chat_id=chat_id, text="❌ Erro: Apenas o administrador pode usar este comando.")
                    
                    # COMANDO /SUPORTE
                    elif "/suporte" in msg:
                        texto_sup = f"🆘 *PRECISA DE AJUDA?*\n\nFale com o nosso suporte aqui: {LINK_SUPORTE}"
                        await bot.send_message(chat_id=chat_id, text=texto_sup, parse_mode='Markdown')

                offset = update.update_id + 1
        except Exception as e:
            print(f"Erro no loop: {e}")
            await asyncio.sleep(2)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(iniciar_bot())
    
