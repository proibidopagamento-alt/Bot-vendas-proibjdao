import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. SERVIDOR PARA MANTER O BOT ATIVO
app = Flask('')

@app.route('/')
def home():
    return "SISTEMA VIP ONLINE"

# 2. CONFIGURAÇÕES PRINCIPAIS
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
MEU_ID_PESSOAL = 5918744817 

# LINKS ATUALIZADOS
LINK_GRUPO_VIP = "https://t.me/+UQBVUWlCHnBhOGEx"
LINK_PAGAMENTO = "https://invoice.infinitepay.io/vippagamentos25/2LnWW6CO21"
video_url = "https://drive.google.com/uc?export=download&id=1PTQBpZEEQ6WajLPXpaEN8OU9PHrEZ08j"

bot = telebot.TeleBot(API_TOKEN)

# TEXTO DE VENDA
texto_venda = (
    "😈 *OII ESTOU ON...* 😈\n\n"
    "VEM SE DIVERTIR NO MEU GRUPINHO VIP VEM...\n"
    "🤤😈⚡🔥🤤🤤\n\n"
    "VÍDEOS COMPLETOS E SEM CENSURA 🤤 NO MEU CANAL VIP VEM SER FELIZ VEM\n"
    "😉🔥😉🔥😉\n\n"
    "✅ *PAGAMENTO ÚNICO DE R$ 25 (VITALÍCIO)*\n\n"
    "💳 Pague no PIX ou CARTÃO pelo botão abaixo!\n\n"
    "⚠️ Após pagar, envie o comprovante **AQUI NO BOT** para receber seu acesso imediato! 🤤"
)

def criar_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🚀 PAGAR R$ 25,00 AGORA", url=LINK_PAGAMENTO))
    return markup

# --- FUNÇÃO DE RECEBER COMPROVANTE ---
@bot.message_handler(content_types=['photo'])
def receber_comprovante(message):
    bot.reply_to(message, "✅ Comprovante recebido! Estamos analisando. Em instantes você receberá o link de acesso aqui.")
    
    # Envia para você aprovar no seu privado
    markup = types.InlineKeyboardMarkup()
    btn_aprovar = types.InlineKeyboardButton("✅ APROVAR E MANDAR LINK", callback_data=f"liberar_{message.chat.id}")
    btn_recusar = types.InlineKeyboardButton("❌ RECUSAR", callback_data=f"recusar_{message.chat.id}")
    markup.add(btn_aprovar, btn_recusar)
    
    bot.send_photo(MEU_ID_PESSOAL, message.photo[-1].file_id, 
                   caption=f"📩 *NOVO PAGAMENTO*\nUsuário: @{message.from_user.username}\nID: `{message.chat.id}`", 
                   parse_mode="Markdown", reply_markup=markup)

# --- BOTÕES DE APROVAÇÃO (SÓ VOCÊ VÊ) ---
@bot.callback_query_handler(func=lambda call: call.data.startswith('liberar_'))
def aprovar(call):
    cliente_id = call.data.split("_")[1]
    # Envia o link que você me mandou agora
    bot.send_message(cliente_id, f"🥳 *PAGAMENTO APROVADO!*\n\nSeja bem-vindo(a)! Entre no link abaixo para acessar o conteúdo:\n\n👉 {LINK_GRUPO_VIP}", parse_mode="Markdown")
    
    # Atualiza a mensagem para você saber que já foi feito
    bot.edit_message_caption("✅ *MENSAGEM DE ACESSO ENVIADA!*", chat_id=MEU_ID_PESSOAL, message_id=call.message.id)
    bot.answer_callback_query(call.id, "Link enviado ao cliente!")

@bot.callback_query_handler(func=lambda call: call.data.startswith('recusar_'))
def recusar(call):
    cliente_id = call.data.split("_")[1]
    bot.send_message(cliente_id, "❌ Seu comprovante não foi aprovado. Verifique se o valor está correto e tente novamente.")
    bot.edit_message_caption("❌ *PAGAMENTO RECUSADO*", chat_id=MEU_ID_PESSOAL, message_id=call.message.id)

# --- POSTAGEM AUTOMÁTICA NO CANAL ---
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
        except: pass
        time.sleep(1800)

# --- COMANDO START ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_video(message.chat.id, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")

if __name__ == "__main__":
    Thread(target=postagem_automatica, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    Thread(target=lambda: app.run(host='0.0.0.0', port=port, use_reloader=False), daemon=True).start()
    bot.infinity_polling(timeout=20)
    
