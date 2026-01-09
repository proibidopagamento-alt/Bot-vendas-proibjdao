import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. Configuração do Servidor Web (Para o Render ficar Online)
app = Flask('')

@app.route('/')
def home():
    return "Bot Online e Operante"

# 2. CONFIGURAÇÕES DO BOT (Verifique se o Token e o ID estão corretos)
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
bot = telebot.TeleBot(API_TOKEN)

# Dados da Postagem
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

# 3. FUNÇÃO DE POSTAGEM AUTOMÁTICA
def postagem_automatica():
    print("Iniciando loop de postagem automática...")
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup())
            print("Vídeo postado no canal com sucesso!")
        except Exception as e:
            print(f"Erro ao postar vídeo: {e}")
        
        # Espera 30 minutos (1800 segundos) para a próxima postagem
        time.sleep(1800)

# 4. COMANDO /START (Para testar se o bot está respondendo)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu estou online e funcionando corretamente! 🚀")

# 5. EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    # Inicia a postagem automática em uma Thread separada
    t_post = Thread(target=postagem_automatica)
    t_post.daemon = True
    t_post.start()
    
    # Inicia o Servidor Flask na porta 10000 para o Render
    port = int(os.environ.get("PORT", 10000))
    t_flask = Thread(target=lambda: app.run(host='0.0.0.0', port=port, use_reloader=False))
    t_flask.daemon = True
    t_flask.start()
    
    # Faz o bot começar a escutar mensagens (Ocupa a linha principal)
    print("Bot escutando mensagens...")
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
        
