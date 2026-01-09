import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# Configuração do Servidor Web para o Render
app = Flask('')

@app.route('/')
def home():
    return "Bot Online"

# CONFIGURAÇÕES DO BOT - VERIFIQUE O TOKEN E O ID
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
bot = telebot.TeleBot(API_TOKEN)

video_url = "https://drive.google.com/uc?export=download&id=1PTQBpZEEQ6WajLPXpaEN8OU9PHrEZ08j"
texto_venda = (
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

def criar_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix'))
    return markup

def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup())
            print("Postagem realizada com sucesso!")
        except Exception as e:
            print(f"Erro na postagem: {e}")
        time.sleep(1800) # Posta a cada 30 minutos

if __name__ == "__main__":
    # Inicia a postagem automática em uma tarefa separada
    Thread(target=postagem_automatica).start()
    
    # Inicia o Polling do bot em uma tarefa separada
    Thread(target=lambda: bot.infinity_polling(timeout=10, long_polling_timeout=5)).start()
    
    # Inicia o Flask na porta 10000 (O que o Render precisa)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
