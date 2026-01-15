import os, threading, asyncio, time
from flask import Flask
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update

app = Flask(__name__)
@app.route('/')
def home(): return "SISTEMA AUTOMATICO ATIVO", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# CONFIGURAÇÕES
TOKEN = "7287694923:AAGkz7SV5oQGKQ65NTleSeq_xVhuglutWL8"
VIDEO = "https://drive.google.com/uc?export=download&id=1g2HaGHeJaL3k_n5rHc61q3wlHOpqFp-N"
GRUPO_ID = "-1002167637171"
MEU_ID_DONO = 5918744817
LINK_PAGAR = "https://pay.infinitepay.io/vippagamentos25/25,00"
LINK_PORTAL = "https://Vipproibidao.short.gy/jfneGR"

TEXTO_VENDA = (
    "🔞 *ACESSO VITALÍCIO - VIP PROIBIDÃO* 🔞\n\n"
    f"🔗 *PORTAL:* {LINK_PORTAL}\n"
    "💳 *VALOR:* R$ 25,00\n\n"
    "📸 *APÓS PAGAR, ENVIE O PRINT DO COMPROVANTE AQUI!*"
)

async def iniciar_bot():
    bot = Bot(token=TOKEN)
    offset = 0
    ultima_postagem = 0

    while True:
        try:
            # 1. POSTAGEM AUTOMÁTICA (90 MIN)
            if time.time() - ultima_postagem > 5400:
                await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO_VENDA, 
                                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR AGORA", url=LINK_PAGAR)]]), 
                                     parse_mode='Markdown')
                ultima_postagem = time.time()

            # 2. ESCUTA DE MENSAGENS, FOTOS E BOTÕES
            updates = await bot.get_updates(offset=offset, timeout=10)
            for update in updates:
                # SE FOR CLIQUE NO BOTÃO DE APROVAR
                if update.callback_query:
                    query = update.callback_query
                    data = query.data
                    if data.startswith("aprovar_"):
                        cliente_id = data.split("_")[1]
                        # Manda o link para o cliente
                        texto_vip = f"✅ *PAGAMENTO CONFIRMADO!*\n\nSeu acesso vitalício está liberado. Clique no link abaixo para entrar no Portal:\n\n🔗 {LINK_PORTAL}"
                        await bot.send_message(chat_id=cliente_id, text=texto_vip, parse_mode='Markdown')
                        # Avisa você que deu certo
                        await query.edit_message_caption(caption="✅ **USUÁRIO APROVADO COM SUCESSO!**", parse_mode='Markdown')
                    await query.answer()

                # SE FOR MENSAGEM (FOTO OU TEXTO)
                elif update.message:
                    chat_id = update.message.chat_id
                    user_id = update.message.from_user.id

                    # CLIENTE ENVIOU COMPROVANTE (FOTO)
                    if update.message.photo:
                        await bot.send_message(chat_id=chat_id, text="⏳ *Recebido!* Estamos conferindo seu comprovante...")
                        # Botão que só aparece para VOCÊ aprovar
                        botao_aprovar = InlineKeyboardMarkup([[InlineKeyboardButton("✅ APROVAR E ENVIAR LINK", callback_data=f"aprovar_{user_id}")]])
                        await bot.send_message(chat_id=MEU_ID_DONO, text=f"📥 *NOVO COMPROVANTE*\nDe: {update.message.from_user.first_name}\nID: `{user_id}`")
                        await bot.send_photo(chat_id=MEU_ID_DONO, photo=update.message.photo[-1].file_id, reply_markup=botao_aprovar)

                    # COMANDOS DE TEXTO
                    elif update.message.text:
                        msg = update.message.text
                        if "/start" in msg:
                            await bot.send_video(chat_id=chat_id, video=VIDEO, caption=TEXTO_VENDA, 
                                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR R$ 25,00", url=LINK_PAGAR)]]), 
                                                 parse_mode='Markdown')
                        elif "/postar" in msg and user_id == MEU_ID_DONO:
                            await bot.send_video(chat_id=GRUPO_ID, video=VIDEO, caption=TEXTO_VENDA, 
                                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 PAGAR AGORA", url=LINK_PAGAR)]]), 
                                                 parse_mode='Markdown')

                offset = update.update_id + 1
        except Exception as e:
            print(f"Erro: {e}")
            await asyncio.sleep(2)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(iniciar_bot())
    
