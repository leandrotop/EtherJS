import socket
import hashlib
import json
import requests
from time import time
import random
import threading

# Função para obter o IP local do dispositivo
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

# Função para gerar a chave pública e privada da carteira (de forma simples)
def create_wallet():
    private_key = hashlib.sha256(str(random.random()).encode()).hexdigest()
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    print(f"Wallet created:\nPrivate Key: {private_key}\nPublic Key: {public_key}")
    return private_key, public_key

# Função para minerar um bloco (Proof of Work)
def mine_block(last_proof):
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

# Função para gerar o hash de um bloco
def hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

# Função para conectar a um nó na rede
def connect_to_node(nodes, current_ip):
    print(f"Seu IP atual: {current_ip}")
    connect_choice = input("Deseja se conectar a um IP? (sim/não): ").lower()
    if connect_choice == 'sim':
        ip = input("Digite o IP para se conectar: ")
        nodes.append(ip)
    else:
        # Conectar a um nó aleatório da rede
        ip = random.choice(nodes) if nodes else current_ip
        print(f"Conectando ao nó {ip}")
        nodes.append(ip)
    return nodes

# Função para lidar com as mensagens recebidas de outros nós
def handle_message_from_node(node_ip, nodes):
    # Simula receber uma lista de IPs de um nó
    print(f"Recebendo dados do nó {node_ip}")
    new_ips = [get_local_ip(), '192.168.0.2', '192.168.0.3']
    nodes.extend(new_ips)
    print(f"IPs conhecidos atualizados: {nodes}")

# Função para enviar transações entre nós
def send_transaction(sender, recipient, amount):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount,
    }
    print(f"Enviando transação: {transaction}")
    return transaction

# Função principal para orquestrar tudo
def main():
    nodes = []
    current_ip = get_local_ip()
    nodes = connect_to_node(nodes, current_ip)
    
    # Criação da carteira
    private_key, public_key = create_wallet()

    # Minerando um bloco (exemplo simples)
    last_proof = 100
    proof = mine_block(last_proof)
    print(f"Novo bloco minerado com prova: {proof}")
    
    # Enviando uma transação
    sender = public_key
    recipient = "recipient_public_key"
    amount = 50
    transaction = send_transaction(sender, recipient, amount)

    # Simulando a comunicação entre nós
    for node in nodes:
        threading.Thread(target=handle_message_from_node, args=(node, nodes)).start()

if __name__ == '__main__':
    main()
