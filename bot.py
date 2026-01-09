import telebot
from telebot import types

API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def mensagem_venda(message):
    markup = types.InlineKeyboardMarkup()
    botao_pagar = types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix')
    markup.add(botao_pagar)

    texto_principal = (
        "🤤😈⚡🔥😈🤤\n"
        "VÍDEOS COMPLETOS E SEM CENSURA 🤤 NO MEU CANAL VIP VEM SER FELIZ VEM\n"
        " 😉🔥😉🔥😉\n"
        "PAGAMENTO ÚNICO DE R$ 25 VITALÍCIO\n"
        "CONTEÚDOS NOVOS TODA SEMANA \n"
        "CHAVE PIX EMAIL \n"
        "proibidopagamento@gmail.com\n"
        "Favor enviar comprovante em https://t.me/feeeproibidao\n"
        " para receber o link de acesso \n"
        "🤤😈⚡🔥😈"
    )
    bot.send_message(message.chat.id, texto_principal, reply_markup=markup)

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
