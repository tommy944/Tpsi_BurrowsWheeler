import socket as sck

HOST = "127.0.0.1"
PORTA = 5000

testo_input = input("Scrivi una stringa per la BWT: ")

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as sock_client:

    sock_client.connect((HOST,PORTA))
    print("Connessione stabilita")

    sock_client.sendall(testo_input.encode("utf-8"))
    risposta = sock_client.recv(1024)
    risultato = risposta.decode("utf-8")

    print(f"Risposta del server: {risultato}")
    print("La connessione è terminata")


