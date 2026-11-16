import socket as sck
import bwt

HOST = "127.0.0.1"
PORTA = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as sock_server:
    sock_server.bind((HOST,PORTA))
    sock_server.listen()
    print("Server in ascolto...")

    while True:
        client_conn, client_addr = sock_server.accept()
        with client_conn:
            print("Client connesso: ", client_addr)

            payload = client_conn.recv(1024)
            testo_ricevuto = payload.decode("utf-8")
            print("Stringa ricevuta: ", testo_ricevuto)

            output_bwt = alghoritm_BWT.BWT(testo_ricevuto)
            print("Risultato BWT: " , output_bwt)

            client_conn.sendall(output_bwt.encode("utf-8"))
            print("Risultato inviato al client")







