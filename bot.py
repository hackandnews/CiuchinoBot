#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fish
from April import today
from telegram import *

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Happy April Fool's day!")


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

#                                  `````````  ````      ````  ````                                   
#                                 /o:::::::o/.y::++    y/:/y `y:::y`                                 
#                                 +:  .////o/.o  .s    h`  s` s   s`                                 
#                                 +:  /o::::`.o  .y::::d`  s` s` `s                                  
#                                 +:  `-...y-.o   ......   s` y. .s                                  
#                                 +:  -+///s..o  `+////o   s` s-`-s                                  
#                                 +:  /s////-.o  .s````h`  s` +hsh+                                  
#                                 +:  `.....s.o  .s    h`  s`.s.``s.                                 
#                                 :+////////+`o///:    +///o  :////                                  
#                                              ````             `                                    
#                                          ``--:://::.`                                              
#                                        .:++oo/---..-:/:`                                           
#                                      `+syho:``      `:o+-`                                         
#                                     `odmy/.``         :so+`                                        
#                                     oNNy--:-.````-::-..yhh+                                        
#                                     mNmyydmmds++sdyosdsdmNm`                                       
#                                     NMNNMMMMMNo/dNNNNMNNNNm`                                       
#                                     yMNdmNmmd/  `oyhhs+/mNd`                                       
#                                     `dNo//--/:..-::.```-hNh`                                       
#                                      :Ns///oooyyo:/+:-.:yNo                                        
#                                      `ydsoooosso/+oo/::+dh`                                        
#                                       -ddysoddhyyhms//+yh-                                         
#                                        .ddysos/////:/oymh/                                         
#                                         oNdy/::::-.:oyoymy/.                                       
#                                   ```-/yNMmhs:-...-+yh-:syymhs+-``                                 
#                          `    ``  .oNNNmmmmmddyyyyhddyyhdmNNNNNmmdhs+-`                            
#                   .:///.  .` `:+/:+yNNNMMNdhdmNNNNmdddmNMMNNNNNNNNmmmddho-                         
#                  -yyyo-.`` .. `-:`.:hMMMMMMNmNNNNNNMMMMMMMMNNNNNNNNNNNmmmdy:                       
#                  /yys.``.-``-/.-+/::sMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNmms`                     
#                  ohhho:.``-:.:osdddmNMMMMMMMMMMMMMMMMMMMMMMMNNNNNNMMMMMMNNNNNy`                    
#                 `yhhhhhho:-+yshmmdNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNy`                   
#                 /yhhhhdmmmmmNNNMMNMMMMMMMNNMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMNm+                   
#               -+shhhhhhddmmmNMMMMMMMMMMNh::+ydNNMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.                  
#              :ssyhhhdhdddmdhNMMMMMMMMMNh`    `-+NNNNMNMMMMMMMMMMMMMMMMMMMMMMMMMNd.                 
#             :yyyhdhdddddddhhNMMMMMMMMN+.``--  `sNmdmNMNMMMMMMMMMMMMMMMMMMMMMMMMMMh.                
#            `yyyyhddddddmdhhdMMMMMMMMMh./syh/  /NNs-odhmdmMMMMMMMMMMMMMMMMMMMMMMMMMy`               
#            -hhhhhddmmmmmddhhNMNMMMMNho+-hyoo-.dNN/.s-:s.oMMMMMMMMMMMMMMMMMMMMMMMMMNs`              
#            -syyyhhhddmmmddhhdyyMMMMms++o/. `.hsyNo+h/os/dMMMMMMMMMMMMMMMMMMMMMMMMMMNo              
#          .``.`....--::///+o+-`oddmmmdyoo+:`:mm-os/hoohysmmMMMMMMMMMMMMMMNMMMMMMMMMNm/              
#         `s::/o`   `/::::   `...---....-..-`:+/.:-`/.-++/ssNNNNNMMMMMMMMmoMMMMMMMNmhs-              
#          o-  +:   +: `/o`-+::---:://.   +///:     `.......---::///+osyyy`odddddhhyyyo`             
#          .s  .s  /+  -o-o-` .-::-` .+/  y``.h     :+--:::/:+y+/++.    `...-.--.-..---`             
#           +:  o:-o  .s.s.  /+.``:o`  +:-o  .o     +-  .---.+ho  .s   `o:-:sos:-// :+::+.           
#           .s  -ys` .s`:o   s     +/  -o+/  :+     y-  o/::/:.s.  o-  o:  /+//  :+ o-  o-           
#            +/  o. .s. :o   s`   `o-  //s.  s:     y`  .-::/o -s  -s +/  :+ s-  +: y.  y`           
#            `y`   `s.   o:  -+/::+:  .s.y   s`    `s   +/::/o  s.  y/o  -o` y   s. h. `s            
#             /+//:s.    `/+-` ``` `./+``h   /////+/s  `y:::-.  .s  -h` -s  `y  `y  y` ++            
#               ```         -/////:/:`  `y::-....`so/  ``..--h.  o-  ` -s`  .y  .y  ysoy`            
#                                        `....-:://.//+///:/+o   .s-..-s`   -o  -s o/.-s:            
#                                                                 `.-::`    .+:/+- /+::o-            
#                                                                                    .`              
#
