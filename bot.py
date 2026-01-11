import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. Configuração do Servidor Web (Prioridade para o Render)
app = Flask(__name__)

@app.route('/')
def home():
    return "BOT ONLINE - R$ 25"

# 2. CONFIGURAÇÕES DO BOT
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
MEU_ID_PESSOAL = 5918744817  
bot = telebot.TeleBot(API_TOKEN)

# CONFIGURAÇÕES DE PAGAMENTO E VÍDEO
LINK_INFINITE_PAY = "https://pay.infinitepay.io/vippagamentos25/25,00"
video_url = "https://drive.google.com/uc?export=download&id=1Bc_kJ165I7xW-nTN4709WU_9f2J_JmFP"

texto_venda = (
    "😈 **OII ESTOU ON...** 😈\n"
    " VEM SE DIVERTIR NO MEU GRUPINHO VIP VEM... \n"
    "🤤😈⚡🔥🤤🤤\n"
    "VÍDEOS COMPLETOS E SEM CENSURA 🤤 NO MEU CANAL VIP VEM SER FELIZ VEM\n"
    " 😉🔥😉🔥😉\n"
    "⭐ **PAGAMENTO ÚNICO DE R$ 25 VITALÍCIO**\n"
    "CONTEÚDOS NOVOS TODA SEMANA \n\n"
    "✅ **ACEITAMOS PIX OU CARTÃO**\n"
    "_(O PIX aparece na tela seguinte após clicar em pagar)_\n\n"
    "🤤😈⚡🔥🤤"
)

def criar_markup():
    markup = types.InlineKeyboardMarkup()
    botao_pagar = types.InlineKeyboardButton("PAGAR R$ 25,00 (PIX/CARTÃO) 💳", url=LINK_INFINITE_PAY)
    markup.add(botao_pagar)
    return markup

# 3. FUNÇÃO DE POSTAGEM AUTOMÁTICA
def postagem_automatica():
    time.sleep(10) # Espera o bot estabilizar
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
            print("Postagem automática realizada!")
            time.sleep(3600) 
        except Exception as e:
            print(f"Erro na postagem: {e}")
            time.sleep(60)

# 4. RESPOSTA NO PRIVADO
@bot.message_handler(func=lambda message: True)
def responder_interacao(message):
    try:
        if message.chat.type == 'private':
            bot.send_video(message.chat.id, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
    except Exception as e:
        print(f"Erro no privado: {e}")

# 5. EXECUÇÃO RESTRUTURADA
if __name__ == "__main__":
    # 1º: Inicia o servidor Flask na porta que o Render exige
    port = int(os.environ.get("PORT", 10000))
    
    # Thread para o Flask (Servidor Web)
    Thread(target=lambda: app.run(host='0.0.0.0', port=port, use_reloader=False)).start()
    
    # 2º: Inicia a postagem automática em segundo plano
    Thread(target=postagem_automatica, daemon=True).start()
    
    # 3º: Inicia o polling do bot
    print("Bot rodando...")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)
    
