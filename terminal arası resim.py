#main kısmı

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1002))
server.listen()
alici, adres = server.accept()
dosya = open('İÇİ.jpg', "wb")
goruntu = alici.recv(2048)
while goruntu:
    dosya.write(goruntu)
    goruntu = alici.recv(2048)
dosya.close()


#alıcı kısmı

import socket


alici = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alici.connect(('localhost', 1002))
dosya = open('3LÜ - Kopya.jpg', 'rb')
alinacakdosya = dosya.read(2048)
while alinacakdosya:
    alici.send(alinacakdosya)
    alinacakdosya = dosya.read(2048)

dosya.close()
alici.close()
