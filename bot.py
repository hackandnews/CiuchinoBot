#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fish
from April import today
from telegram import *

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Happy April Fools' Day!")


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("123456789:abc-qwertyuio9GgXnXXMPCo3rSnrhtuDba00") #CiuchinoBot Token :)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

   # log all errors
    dp.add_error_handler(error)

    print("New updates will be released soon! Stay tuned :) ")
    
    # Start the Bot
    updater.start_polling()
.
    updater.idle()
if __name__ == '__main__':
    main()
    
# H&N team
# 1 April 2017
