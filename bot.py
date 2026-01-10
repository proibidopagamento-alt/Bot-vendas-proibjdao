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
    return "BOT ONLINE"

# 2. CONFIGURAÇÕES
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
MEU_ID_PESSOAL = 5918744817 
bot = telebot.TeleBot(API_TOKEN)

# COLOQUEI O LINK EXATO QUE APARECE NO SEU PRINT QUE FUNCIONOU
LINK_PAGAMENTO = "https://invoice.infinitepay.io/vippagamentos25/2LnWW6CO21"

video_url = "https://drive.google.com/uc?export=download&id=1PTQBpZEEQ6WajLPXpaEN8OU9PHrEZ08j"

texto_venda = (
    "😈 *OII ESTOU ON...* 😈\n\n"
    "VEM SE DIVERTIR NO MEU GRUPINHO VIP VEM...\n"
    "🤤😈⚡🔥🤤🤤\n\n"
    "VÍDEOS COMPLETOS E SEM CENSURA 🤤 NO MEU CANAL VIP VEM SER FELIZ VEM\n"
    "😉🔥😉🔥😉\n\n"
    "✅ *PAGAMENTO ÚNICO DE R$ 25 (VITALÍCIO)*\n\n"
    "💳 Pague no PIX ou CARTÃO pelo botão abaixo!\n\n"
    "⚠️ Após pagar, envie o comprovante em:\n"
    "👉 https://t.me/feeeproibidao"
)

def criar_markup():
    markup = types.InlineKeyboardMarkup()
    # Adicionando o botão com o link que você confirmou que funciona no navegador
    botao_pagar = types.InlineKeyboardButton("🚀 CLIQUE AQUI PARA PAGAR R$ 25", url=LINK_PAGAMENTO)
    markup.add(botao_pagar)
    return markup

# 3. POSTAGEM AUTOMÁTICA
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
            print("Postagem automática ok!")
        except Exception as e:
            print(f"Erro: {e}")
        time.sleep(1800)

# 4. COMANDOS
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_video(message.chat.id, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")

@bot.message_handler(commands=['postar'])
def postar_manual(message):
    if message.from_user.id == MEU_ID_PESSOAL:
        bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
        bot.reply_to(message, "✅ Postado!")

if __name__ == "__main__":
    Thread(target=postagem_automatica, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    Thread(target=lambda: app.run(host='0.0.0.0', port=port, use_reloader=False), daemon=True).start()
    bot.infinity_polling(timeout=20)
    
