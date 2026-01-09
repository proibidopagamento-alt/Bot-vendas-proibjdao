import telebot
from telebot import types

# Seu Token e ID do Canal configurados
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
bot = telebot.TeleBot(API_TOKEN)

# COMANDO PARA POSTAR NO CANAL
@bot.message_handler(commands=['postar'])
def postar_no_canal(message):
    markup = types.InlineKeyboardMarkup()
    botao_pagar = types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix')
    markup.add(botao_pagar)

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

    try:
        bot.send_video(ID_CANAL, video_url, caption=texto_venda, reply_markup=markup)
        bot.reply_to(message, "✅ Postado com sucesso no Canal!")
    except Exception as e:
        bot.reply_to(message, f"❌ Erro ao postar no canal: {e}\n(Verifique se o bot é administrador do canal)")

# COMANDO START (PARA QUEM FALAR NO PRIVADO)
@bot.message_handler(commands=['start'])
def mensagem_venda(message):
    markup = types.InlineKeyboardMarkup()
    botao_pagar = types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix')
    markup.add(botao_pagar)

    texto_principal = (
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

    try:
        bot.send_video(message.chat.id, video_url, caption=texto_principal, reply_markup=markup)
    except Exception:
        bot.send_message(message.chat.id, texto_principal, reply_markup=markup)

# BOTÃO DO PIX
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

print("Bot de Vendas Online iniciado...")
bot.polling()
