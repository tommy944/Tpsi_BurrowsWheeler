import socket as sck
import alghoritm_BWT

HOST = "127.0.0.1"
PORTA = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as sock_server:
    sock_server.bind((HOST,PORTA))
    sock_server.listen()
    print("Server in ascolto...")


