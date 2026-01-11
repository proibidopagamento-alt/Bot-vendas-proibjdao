import telebot
import time
from threading import Thread
from flask import Flask

# --- CONFIGURAÇÕES ---
TOKEN = "SEU_TOKEN_AQUI"
ID_CANAL = "SEU_ID_DO_CANAL" 
LINK_INFINITE_PAY = "https://pay.infinitepay.io/SUA_TAG/VALOR" # Seu link da InfinitePay
VIDEO_DRIVE_URL = "SUA_URL_DO_VIDEO_DO_DRIVE" # Link que termina em ...JmFP

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está online e postando!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Função única para enviar o conteúdo (Vídeo + Texto + Botão)
def enviar_conteudo(chat_id):
    texto_venda = (
        "🔥 *ACESSO EXCLUSIVO LIBERADO*\n\n"
        "Para desbloquear todo o conteúdo, realize o pagamento seguro abaixo.\n"
        "Aceitamos PIX e Cartão via InfinitePay.\n\n"
        "👇 *Clique no botão abaixo para pagar*"
    )
    
    markup = telebot.types.InlineKeyboardMarkup()
    botao_pagar = telebot.types.InlineKeyboardButton("PAGAR AGORA 💳", url=LINK_INFINITE_PAY)
    markup.add(botao_pagar)

    try:
        bot.send_video(chat_id, VIDEO_DRIVE_URL, caption=texto_venda, parse_mode="Markdown", reply_markup=markup)
    except Exception as e:
        print(f"Erro ao enviar para {chat_id}: {e}")

# --- RESPOSTA NO PRIVADO ---
# Este comando faz o bot responder automaticamente no privado
@bot.message_handler(func=lambda message: True) 
def responder_interacao(message):
    # Se a mensagem vier de uma conversa privada, o bot responde com o vídeo e o link
    if message.chat.type == 'private':
        enviar_conteudo(message.chat.id)

# --- POSTAGEM AUTOMÁTICA NO GRUPO ---
def postagem_automatica():
    while True:
        try:
            # Envia para o grupo/canal de 1 em 1 hora
            enviar_conteudo(ID_CANAL)
            time.sleep(3600) 
        except Exception as e:
            print(f"Erro na postagem automática: {e}")
            time.sleep(60)

if __name__ == "__main__":
    # Rodar Flask para o Render não derrubar o bot
    t_flask = Thread(target=run_flask)
    t_flask.start()

    # Rodar a postagem automática em paralelo
    t_post = Thread(target=postagem_automatica)
    t_post.start()

    print("Bot iniciado com sucesso!")
    bot.polling(none_stop=True)
    
