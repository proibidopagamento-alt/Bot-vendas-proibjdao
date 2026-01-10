import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. SERVIDOR PARA O CRON-JOB ACESSAR
app = Flask('')

@app.route('/')
def home():
    return "BOT ONLINE - CRON-JOB ATIVO"

# 2. CONFIGURAÇÕES
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
MEU_ID_PESSOAL = 5918744817 
bot = telebot.TeleBot(API_TOKEN)

# Link da sua Tag InfinitePay configurado para R$ 25
LINK_PAGAMENTO = "https://pay.infinitepay.io/vippagamentos25/25"

video_url = "https://drive.google.com/uc?export=download&id=1PTQBpZEEQ6WajLPXpaEN8OU9PHrEZ08j"

# SEU TEXTO PERSONALIZADO ATUALIZADO
texto_venda = (
    "😈 OII ESTOU ON... 😈\n\n"
    "VEM SE DIVERTIR NO MEU GRUPINHO VIP VEM... \n"
    "🤤😈⚡🔥🤤🤤\n\n"
    "VÍDEOS COMPLETOS E SEM CENSURA 🤤 NO MEU CANAL VIP VEM SER FELIZ VEM\n"
    "😉🔥😉🔥😉\n\n"
    "✅ PAGAMENTO ÚNICO DE R$ 25 (VITALÍCIO)\n"
    "📸 CONTEÚDOS NOVOS TODA SEMANA\n\n"
    "💳 Pague no PIX ou Cartão de Crédito pelo botão abaixo!\n\n"
    "⚠️ Após o pagamento, envie o comprovante para: https://t.me/feeeproibidao\n"
    "para receber o seu link de acesso imediatamente! 🤤"
)

def criar_markup():
    markup = types.InlineKeyboardMarkup()
    # Agora o botão abre o link externo da InfinitePay
    botao_pagar = types.InlineKeyboardButton("🚀 PAGAR AGORA R$ 25,00", url=LINK_PAGAMENTO)
    markup.add(botao_pagar)
    return markup

# 3. POSTAGEM AUTOMÁTICA (30 MINUTOS)
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
            print("Postagem automática ok!")
        except Exception as e:
            print(f"Erro auto-post: {e}")
        time.sleep(1800)

# 4. COMANDOS
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_video(message.chat.id, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")

@bot.message_handler(commands=['postar'])
def postar_manual(message):
    if message.from_user.id == MEU_ID_PESSOAL:
        bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup(), parse_mode="Markdown")
        bot.reply_to(message, "✅ Postado no canal!")

# 5. RODAR TUDO
if __name__ == "__main__":
    # Inicia a thread de postagem automática
    Thread(target=postagem_automatica, daemon=True).start()
    
    # Inicia o servidor Flask para manter o bot vivo no Render/Replit
    port = int(os.environ.get("PORT", 10000))
    Thread(target=lambda: app.run(host='0.0.0.0', port=port, use_reloader=False), daemon=True).start()
    
    print("Bot rodando com Link InfinitePay...")
    bot.infinity_polling(timeout=20)
                
