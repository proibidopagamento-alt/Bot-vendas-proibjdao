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

# Configurações do Bot
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
            print("Postagem automática realizada!")
        except Exception as e:
            print(f"Erro na postagem: {e}")
        time.sleep(1800) # 30 minutos

# Função para rodar o bot e o servidor juntos
def run_everything():
    # Inicia a thread da postagem
    Thread(target=postagem_automatica).start()
    # Inicia o bot
    bot.polling(none_stop=True)

if __name__ == "__main__":
    # O segredo: rodar o bot em background e deixar o Flask no comando principal
    Thread(target=run_everything).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
