#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import telepot
import re
import os
#api do bot
api = 'seu token do telegram pegar no bot father e por dentro das aspas'
bot = telepot.Bot(api)
# função handle nao mude as linhas abaixo----------------------------------->
def handle(msg):
        uid = msg['from']['id']
        firstname = msg['from']['first_name']
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        try:
                user = '@' + msg['from']['username']
        except:
                print ('')
        msgid = msg['message_id']

        content_type, chat_type, chat_id = telepot.glance(msg)
        if msg.get('text'):
                texto = msg['text'].split()[0]
#final da função handle seus codigos vem abaixo-------------------------------------:                        


                if texto == 'boy das galaxias': #se alguem digitar boy das galaxias ele responde
                        bot.sendMessage(chat_id, 'eu amo ele.' , reply_to_message_id=msgid)#resposta do bot quando alguem digitar boy das galaxias
                
                #crie seus comandos bro é facil        
                if texto == 'bote um comando aqui':
                        bot.sendMessage(chat_id, 'bote a resposta do bot aqui' , reply_to_message_id=msgid)                                

              


#inicia o bot nao mude as linhas abaixo------------------------------------------>
bot.message_loop(handle)
print ('[+] ON')
while 1:
        pass
#final do codigo------------------------------------------------------------------>