import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. Configuração do Servidor Web (Para o Render)
app = Flask('')

@app.route('/')
def home():
    return "Bot Online e Personalizado"

# 2. CONFIGURAÇÕES DO BOT
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
MEU_ID_PESSOAL = 5918744817  # Seu ID
bot = telebot.TeleBot(API_TOKEN)

# Dados da Postagem
video_url = "https://drive.google.com/uc?export=download&id=1PTQBpZEEQ6WajLPXpaEN8OU9PHrEZ08j"

# Texto que você pediu para o /START
texto_start = (
    "😈OII ESTOU ON...😈\n"
    " VEM SE DIVERTIR NO KEU GRUPINHO V7P VEM... \n"
    "🤤😈⚡🔥🤤🤤\n"
    "VÍDEOS COMPLETOS E SEM CENSURA 🤤 NO MEU CANAL VIP VEM SER FELIZ VEM\n"
    " 😉🔥😉🔥😉\n"
    "PAGAMENTO ÚNICO DE R$ 25 VITALÍCIO\n"
    "CONTEÚDOS NOVOS TODA SEMANA \n"
    "CHAVE PIX EMAIL \n"
    "proibidopagamento@gmail.com\n"
    "Favor enviar comprovante em https://t.me/feeeproibidao\n"
    " para receber o link de acesso \n"
    "🤤😈⚡🔥🤤"
)

# Texto padrão para o CANAL (se quiser diferente, altere aqui)
texto_venda_canal = texto_start 

def criar_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix'))
    return markup

# 3. FUNÇÃO DE POSTAGEM AUTOMÁTICA
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda_canal, reply_markup=criar_markup())
            print("Postagem automática realizada!")
        except Exception as e:
            print(f"Erro na postagem automática: {e}")
        time.sleep(1800)

# 4. COMANDO /START (TEXTO NOVO QUE VOCÊ PEDIU)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_video(message.chat.id, video_url, caption=texto_start, reply_markup=criar_markup())
    except Exception as e:
        bot.reply_to(message, "Erro ao enviar vídeo no privado.")

# 5. COMANDO /POSTAR (PROTEGIDO)
@bot.message_handler(commands=['postar'])
def postar_manual(message):
    if message.from_user.id == MEU_ID_PESSOAL:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda_canal, reply_markup=criar_markup())
            bot.reply_to(message, "✅ Postado no canal com sucesso!")
        except Exception as e:
            bot.reply_to(message, f"❌ Erro ao postar no canal: {e}")
    else:
        bot.reply_to(message, "🚫 Acesso negado.")

# 6. EXECUÇÃO
if __name__ == "__main__":
    Thread(target=postagem_automatica, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    Thread(target=lambda: app.run(host='0.0.0.0', port=port, use_reloader=False), daemon=True).start()
    print("Bot rodando com novo texto no /start...")
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
                     
