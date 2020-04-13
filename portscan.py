#!/usr/bin/python

import socket
ip = raw_input("Digite ip do Alvo = ")
for porta in range (1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((ip, porta)) == 0:
                 print "Porta",porta,"[ABERTA********************************************]"
        if porta == 65534:
                 print ">>>>>>>>ESCANEAMENTO FINALIZADO COM SUCESSO ! <<<<<<<<<<<<<<<<<<<<"
                 s.close()
     


