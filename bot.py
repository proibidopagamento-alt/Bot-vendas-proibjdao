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
    return "BOT ONLINE - VÍDEO ATUALIZADO"

# 2. CONFIGURAÇÕES DO BOT
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
MEU_ID_PESSOAL = 5918744817  # Seu ID de administrador
bot = telebot.TeleBot(API_TOKEN)

# LINK DO VÍDEO NOVO (Já convertido para download direto)
video_url = "https://drive.google.com/uc?export=download&id=1Bc_kJ165I7xW-nTN4709WU_9f2J_JmFP"

# SEU TEXTO PERSONALIZADO
texto_venda = (
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

# Função para criar o botão de pagamento
def criar_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix'))
    return markup

# 3. FUNÇÃO DE POSTAGEM AUTOMÁTICA (30 MINUTOS)
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup())
            print("Postagem automática realizada com sucesso!")
        except Exception as e:
            print(f"Erro na postagem automática: {e}")
        time.sleep(1800) # Espera 30 minutos

# 4. COMANDO /START (Responde para você com o vídeo e o texto novo)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_video(message.chat.id, video_url, caption=texto_venda, reply_markup=criar_markup())
    except Exception as e:
        bot.reply_to(message, "Erro ao carregar o vídeo. Verifique se o link do Drive está público.")

# 5. COMANDO /POSTAR (Só você pode usar para postar no canal agora)
@bot.message_handler(commands=['postar'])
def postar_manual(message):
    if message.from_user.id == MEU_ID_PESSOAL:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup())
            bot.reply_to(message, "✅ Postado no canal com sucesso!")
        except Exception as e:
            bot.reply_to(message, f"❌ Erro ao postar: {e}")
    else:
        bot.reply_to(message, "🚫 Acesso negado. Apenas o dono pode usar este comando.")

# 6. RESPOSTA DO BOTÃO PIX
@bot.callback_query_handler(func=lambda call: call.data == 'ver_pix')
def responder_pix(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "💰 *Chave PIX (E-mail):*\n\n`proibidopagamento@gmail.com`", parse_mode="Markdown")

# 7. EXECUÇÃO DO BOT E SERVIDOR
if __name__ == "__main__":
    # Inicia a postagem automática em segundo plano
    Thread(target=postagem_automatica, daemon=True).start()
    
    # Inicia o servidor Flask para o Cron-job não deixar o bot dormir
    port = int(os.environ.get("PORT", 10000))
    Thread(target=lambda: app.run(host='0.0.0.0', port=port, use_reloader=False), daemon=True).start()
    
    # Faz o bot ficar escutando os comandos
    print("Bot rodando com o novo vídeo...")
    bot.infinity_polling(timeout=20, long_polling_timeout=10)
        
