#!/usr/bin/python

import socket,time
ip = raw_input("Digite ip = ")
port = (21, 22,23, 25,53,80,110,115,135,138,139,143,156,389,443,445,465,587,8080)
for porta in port:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2) # limite de tempo suportado

        if s.connect_ex((ip, porta)) == 0:
                 print "Porta",porta,"[ABERTA********************************************]"
                 
        else:
                 print "Porta",porta,"[Fechada]"
                 
                 
        if porta == 8080:
        
                print ">>>>>>>>>>>>>>>> ESCANEAMENTO FINALIZADO <<<<<<<<<<<<<<<<<<<<"
                time.sleep(15)# Demora 15 segundos para fechar a janela
