import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. SERVIDOR WEB (TEM QUE SER O PRIMEIRO A LIGAR)
app = Flask('')

@app.route('/')
def home():
    return "Bot Online"

# 2. CONFIGURAÇÕES DO BOT
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
bot = telebot.TeleBot(API_TOKEN)

video_url = "https://drive.google.com/uc?export=download&id=1PTQBpZEEQ6WajLPXpaEN8OU9PHrEZ08j"
texto_venda = (
    "🤤😈⚡🔥🤤🤤\nVÍDEOS COMPLETOS E SEM CENSURA 🤤 NO MEU CANAL VIP VEM SER FELIZ VEM\n 😉🔥😉🔥😉\n"
    "PAGAMENTO ÚNICO DE R$ 25 VITALÍCIO\nCONTEÚDOS NOVOS TODA SEMANA \nCHAVE PIX EMAIL \n"
    "proibidopagamento@gmail.com\nFavor enviar comprovante em https://t.me/feeeproibidao\n"
    " para receber o link de acesso \n🤤😈⚡🔥🤤"
)

def criar_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix'))
    return markup

# 3. FUNÇÃO DE POSTAGEM (30 MINUTOS)
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup())
            print("Postagem feita!")
        except Exception as e:
            print(f"Erro: {e}")
        time.sleep(1800)

# 4. INICIALIZAÇÃO SEGURA
def start_bot():
    # Dá um tempo para o Flask ligar antes de iniciar o bot
    time.sleep(5)
    Thread(target=postagem_automatica).start()
    bot.polling(none_stop=True)

if __name__ == "__main__":
    # LIGA O BOT NO FUNDO
    Thread(target=start_bot).start()
    
    # LIGA O SERVIDOR NA FRENTE (O QUE O RENDER QUER VER)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
