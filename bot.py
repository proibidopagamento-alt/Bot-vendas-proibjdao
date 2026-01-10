import telebot
from telebot import types
import time
from threading import Thread
from flask import Flask
import os

# 1. SERVIDOR PARA MANTER O BOT ATIVO (USADO NO RENDER/REPLIT)
app = Flask('')

@app.route('/')
def home():
    return "BOT ONLINE - LINK INFINITEPAY ATIVO"

# 2. CONFIGURAÇÕES PRINCIPAIS
API_TOKEN = '8104662316:AAGJlNxWeUMUDDB5Zizte3vsBoiOlLqIzHg'
ID_CANAL = -1002167637171
MEU_ID_PESSOAL = 5918744817 
bot = telebot.TeleBot(API_TOKEN)

# SEU NOVO LINK DE PAGAMENTO DA INFINITEPAY (TESTADO E FUNCIONANDO)
LINK_PAGAMENTO = "https://invoice.infinitepay.io/vippagamentos25/2LnWW6CO21"

video_url = "https://drive.google.com/uc?export=download&id=1PTQBpZEEQ6WajLPXpaEN8OU9PHrEZ08j"

# TEXTO DE VENDA OTIMIZADO PARA O NOVO MÉTODO
texto_venda = (
    "😈 *OII ESTOU ON...* 😈\n\n"
    "VEM SE DIVERTIR NO MEU GRUPINHO VIP
    
