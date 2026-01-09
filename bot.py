import telebot
from telebot import types

# Seu Token já configurado
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def mensagem_venda(message):
    # Cria o botão de pagamento
    markup = types.InlineKeyboardMarkup()
    botao_pagar = types.InlineKeyboardButton("Pague agora R$25,00", callback_data='ver_pix')
    markup.add(botao_pagar)

    # Seu texto principal (agora será a legenda do vídeo)
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

    # Link do seu vídeo no Google Drive (ajustado para download)
    video_url = "https://drive.google.com/uc?export=download&id=1k9r0J1AzOpJD-oiaQuchQ-k4ogjkAfcI"

    try:
        # Envia o VÍDEO com o TEXTO e o BOTÃO tudo junto
        bot.send_video(
            message.chat.id, 
            video_url, 
            caption=texto_principal, 
            reply_markup=markup
        )
    except Exception as e:
        # Caso o vídeo falhe, envia apenas a mensagem para não parar o bot
        bot.send_message(message.chat.id, texto_principal, reply_markup=markup)
        print(f"Erro ao enviar vídeo: {e}")

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
