import argparse
import socket
import threading
from time import sleep

NODES = {
    8001: 8002,
    8002: 8003,
    8003: 8004,
    8004: 8005,
    8005: 8006,
    8006: 8001
}

received_messages = {}

def receive_messages(sock, host, port):
    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8')
        print(f'Received from Node: {addr[0]}:{addr[1]}', message)
        send_message(sock, host, port, message)

def send_message(sock, host, port, message):
    sleep(3)
    next_port = NODES[port]
    if not has_received_message(port, message):
        sock.sendto(message.encode('utf-8'), (host, next_port))

def has_received_message(port, message):
    if port in received_messages and received_messages[port] == message:
        return True
    else:
        received_messages[port] = message
        return False

def main(port):
    host = 'localhost'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(sock, host, port))
    receive_thread.start()

    while True:
        message = input("Enter the message to send: ")
        send_thread = threading.Thread(target=send_message, args=(sock, host, port, message))
        send_thread.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int, help="Port number for this node")
    args = parser.parse_args()
    main(args.port)