import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. SERVIDOR PARA O RENDER NÃO DAR ERRO VERMELHO
app = Flask('')

@app.route('/')
def home():
    return "Bot Online"

def run_web():
    # O Render exige que o bot escute nesta porta
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. CONFIGURAÇÕES DO SEU BOT
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

# 3. FUNÇÃO DE POSTAGEM A CADA 30 MINUTOS (1800 SEGUNDOS)
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup())
            print("Postagem automática de 30 min feita!")
        except Exception as e:
            print(f"Erro na postagem: {e}")
        time.sleep(1800) 

# 4. INICIALIZAÇÃO (O SEGREDO PARA NÃO TRAVAR)
if __name__ == "__main__":
    # Inicia o servidor web primeiro
    Thread(target=run_web).start()
    # Inicia a postagem automática em seguida
    Thread(target=postagem_automatica).start()

    @bot.message_handler(commands=['postar', 'start'])
    def atender_comandos(message):
        bot.send_video(message.chat.id, video_url, caption=texto_venda, reply_markup=criar_markup())

    @bot.callback_query_handler(func=lambda call: call.data == 'ver_pix')
    def responder_pix(call):
        texto_pix = (
            "✅ *CHAVE PIX LIBERADA!* \n\n"
            "📍 *COPIE O E-MAIL ABAIXO:*\n"
            "`proibidopagamento@gmail.com` \n\n"
            "💰 *VALOR:* R$ 25,00\n\n"
            "📩 *APÓS O PAGAMENTO:* \n"
            "Envie o comprovante para: https://t.me/feeeproibidao"
        )
        bot.send_message(call.message.chat.id, texto_pix, parse_mode='Markdown')

    print("Bot rodando com sucesso!")
    bot.polling(none_stop=True)
