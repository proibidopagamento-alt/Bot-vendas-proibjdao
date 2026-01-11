# ... (mantenha o restante do código igual)

# TEXTO ATUALIZADO PARA ORIENTAR SOBRE O PIX
texto_venda = (
    "😈 **OII ESTOU ON...** 😈\n\n"
    "VEM SE DIVERTIR NO MEU GRUPINHO VIP VEM...\n"
    "🤤😈⚡🔥🤤🤤\n\n"
    "VÍDEOS COMPLETOS E SEM CENSURA 🤤\n\n"
    "⭐ **PAGAMENTO ÚNICO DE R$ 25 VITALÍCIO**\n\n"
    "✅ **ACEITAMOS PIX E CARTÃO**\n"
    "_(Ao clicar abaixo, selecione a opção de pagamento na tela da InfinitePay)_ \n\n"
    "👇 **CLIQUE NO BOTÃO ABAIXO PARA PAGAR**"
)

# Botão com texto reforçando as opções
def criar_markup():
    markup = types.InlineKeyboardMarkup()
    botao_pagar = types.InlineKeyboardButton("PAGAR R$ 25,00 (PIX OU CARTÃO) 💳", url=LINK_INFINITE_PAY)
    markup.add(botao_pagar)
    return markup

# ... (restante do código)
