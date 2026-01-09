import telebot
from telebot import types
import time
from threading import Thread

API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
bot = telebot.TeleBot(API_TOKEN)

def criar_markup():
    markup = types.InlineKeyboardMarkup()
    botao_pagar = types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix')
    markup.add(botao_pagar)
    return markup

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

video_url = "https://drive.google.com/uc?export=download&id=1PTQBpZEEQ6WajLPXpaEN8OU9PHrEZ08j"

# FUNÇÃO DE POSTAGEM AUTOMÁTICA
def postagem_automatica():
    while True:
        try:
            bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup())
            print("Postagem automática realizada!")
        except Exception as e:
            print(f"Erro na postagem automática: {e}")
        
        # ESPERA 1000 SEGUNDOS
        time.sleep(1000) 

# Inicia o temporizador em segundo plano
Thread(target=postagem_automatica).start()

@bot.message_handler(commands=['postar'])
def postar_manual(message):
    try:
        bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=criar_markup())
        bot.reply_to(message, "✅ Postado manualmente no Canal!")
    except Exception as e:
        bot.reply_to(message, f"❌ Erro: {e}")

@bot.message_handler(commands=['start'])
def mensagem_venda(message):
    bot.send_video(message.chat.id, video_url, caption=texto_venda, reply_markup=criar_markup())

@bot.callback_query_handler(func=lambda call: call.data == 'ver_pix')
def responder_clique_pix(call):
    texto_pix = (
        "✅ *CHAVE PIX LIBERADA!* \n\n"
        "📍 *COPIE O E-MAIL ABAIXO:*\n"
        "`proibidopagamento@gmail.com` \n\n"
        "💰 *VALOR:* R$ 25,00\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📩 *APÓS O PAGAMENTO:* \n"
        "Envie o comprovante agora para o link abaixo:\n"
        "👉 https://t.me/feeeproibidao \n"
        "━━━━━━━━━━━━━━━━━━━━\n"
    )
    bot.send_message(call.message.chat.id, texto_pix, parse_mode='Markdown')
    bot.answer_callback_query(call.id)

print("Bot Iniciado - Postagens a cada 1000 segundos.")
bot.polling()

print("Bot de Vendas Online iniciado...")
bot.polling()
