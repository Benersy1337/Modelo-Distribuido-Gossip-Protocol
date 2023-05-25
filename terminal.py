import subprocess

def main():
    # Comandos a serem executados
    commands = [
        'python node_1.py',
        'python node_2.py',
        'python node_3.py',
        'python node_4.py',
        'python node_5.py',
        'python node_6.py'
    ]

    # Abrir terminal e executar cada comando
    for command in commands:
        subprocess.Popen(['start', 'cmd', '/K', command], shell=True)

if __name__ == '__main__':
    main()