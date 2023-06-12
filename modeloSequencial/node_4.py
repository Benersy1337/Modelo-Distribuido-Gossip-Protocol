import socket
import threading
from time import sleep

def receive_messages(sock, host, next_port):
    data, addr = sock.recvfrom(1024)
    print(f'Received from Node: {addr[0]}:{addr[1]}', data.decode('utf-8'))
    send_message(sock, host, next_port)

def send_message(sock, host, next_port):
    sleep(6)  # Move o atraso para a função send_message
    message = 'ENCAMINHADO POR NODE 4'
    sock.sendto(message.encode('utf-8'), (host, next_port))

def main():
    
    print('NODE 4')

    host = 'localhost'
    port = 8004
    next_port = 8005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(sock, host, next_port))  # Adiciona o argumento 'host'
    receive_thread.start()

    send_thread = threading.Thread(target=send_message, args=(sock, host, next_port))
    send_thread.start()

    send_thread.join()

if __name__ == '__main__':
    main()