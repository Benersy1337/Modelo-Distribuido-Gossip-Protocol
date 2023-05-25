import socket
import threading

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f'Received from Node:{addr[1]}', data.decode('utf-8'))

def send_message(sock, host, send_ports):
    while True:
        message = input('Enter message: ')
        for port in send_ports:
            sock.sendto(message.encode('utf-8'), (host, port))

def main():
    host = 'localhost'
    port = 8002

    send_ports = [8001, 8003, 8004, 8005, 8006]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_message, args=(sock, host, send_ports))
    send_thread.start()
    
    send_thread.join()

if __name__ == '__main__':
    main()