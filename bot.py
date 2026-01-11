import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. Configuração do Servidor Web (Para o Render e Cron-job)
app = Flask('')

@app.route('/')
def home():
    return "BOT ONLINE - PAGAMENTO INFINITEPAY R$ 25"

# 2. CONFIGURAÇÕES DO BOT
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
MEU_ID_PESSOAL = 5918744817  
bot = telebot.TeleBot(API_TOKEN)

# CONFIGURAÇÕES DE PAGAMENTO E VÍDEO
LINK_INFINITE_PAY = "https://pay.infinitepay.io/vippagamentos25/25,00"
video_url = "https://drive.google.com/uc?export=download&id=1Bc_kJ165I7xW-nTN4709WU_9f2J_JmFP"

# TEXTO ATUALIZADO (SEM PIX E-MAIL)
texto_venda = (
    "😈 **OII ESTOU ON...** 😈\n\n"
    "VEM SE DIVERTIR NO MEU GRUPINHO VIP VEM...\n"
    "🤤😈⚡🔥🤤🤤\n\n"
    "VÍDEOS COMPLETOS E SEM CENSURA 🤤 NO MEU CANAL VIP VEM SER FELIZ VEM\n"
    " 😉🔥😉🔥😉\n\n"
    "⭐ **PAGAMENTO ÚNICO DE R$ 25 VITALÍCIO**\n"
    "CONTEÚDOS NOVOS TODA SEMANA\n\n"
    "✅ Pagamento seguro via PIX ou CARTÃO.\n"
    "👇 **CLIQUE NO BOTÃO ABAIXO PARA ENTRAR AGORA**"
)

# Criar botão que leva direto para o pagamento
def criar_markup():
    markup = types.InlineKeyboardMarkup()
    botao_pagar = types.InlineKeyboardButton("PAGAR R$ 25,00 (PIX/CARTÃO) 💳", url=LINK_INFINITE_PAY)
    markup.add(botao_pagar)
    return markup

# 3. FUNÇÃO DE POSTAGEM AUTOMÁTICA (1 EM 1 HORA)
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
            print("Postagem automática (1h) realizada!")
        except Exception as e:
            print(f"Erro na postagem automática: {e}")
        time.sleep(3600) 

# 4. RESPOSTA NO PRIVADO (Captura qualquer mensagem e o /start)
@bot.message_handler(func=lambda message: True)
def responder_interacao(message):
    try:
        # Se for no privado, ele envia o vídeo e o botão de pagamento
        if message.chat.type == 'private':
            bot.send_video(message.chat.id, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
        
        # Se for o comando /postar no grupo (apenas para você)
        elif message.text == '/postar' and message.from_user.id == MEU_ID_PESSOAL:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
            bot.reply_to(message, "✅ Postado no canal!")
    except Exception as e:
        print(f"Erro na interação: {e}")

# 5. EXECUÇÃO
if __name__ == "__main__":
    # Inicia postagem automática
    Thread(target=postagem_automatica, daemon=True).start()
    
    # Inicia servidor Flask para o Render
    port = int(os.environ.get("PORT", 10000))
    Thread(target=lambda: app.run(host='0.0.0.0', port=port, use_reloader=False), daemon=True).start()
    
    print("Bot rodando com InfinitePay e postagem a cada 1 hora...")
    bot.infinity_polling(timeout=20)
            
