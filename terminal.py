import subprocess

def main():
    # Portas de entrada
    portas = range(8001, 8007)

    # Abrir terminal e executar nodes.py em cada porta
    for porta in portas:
        command = f'start cmd /K python nodes.py {porta}'
        subprocess.Popen(command, shell=True)

if __name__ == '__main__':
    main()