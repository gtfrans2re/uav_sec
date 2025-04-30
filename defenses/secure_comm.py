"""
Communication Sécurisée (SSL)
-----------------------------
Ce module simule l’établissement d’une communication sécurisée entre un drone et un poste
de commande via SSL (TLS 1.2+).
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logger import setup_logger
from utils.config import GPS_BASE_LAT, GPS_BASE_LON, SIMULATED_GPS_POINTS, GPS_SPOOF_FREQ

import ssl
import socket
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Initialisation de la communication sécurisée TLS...")

HOST = '127.0.0.1'
PORT = 65432

def secure_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    #context.load_cert_chain(certfile='/certs/server.crt', keyfile='/certs/server.key')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        with context.wrap_socket(sock, server_side=True) as ssock:
            logger.info("Serveur sécurisé en attente de connexion...")
            conn, addr = ssock.accept()

            logger.info(f"Connexion TLS établie avec {addr}")
            with conn:
                logger.info(f"Connexion TLS établie avec {addr}")
                data = conn.recv(1024).decode()
                logger.info(f"Message reçu : {data}")
                conn.sendall(b"Ack secured")
                logger.info("Message de confirmation envoyé.")
                conn.close()
                logger.info("Fermeture de la connexion.")
            with conn:
                logger.info(f"Connexion TLS établie avec {addr}")
                data = conn.recv(1024).decode()
                logger.info(f"Message reçu : {data}")
                conn.sendall(b"Ack secured")

if __name__ == "__main__":
    secure_server()
    logger.info("Fin de la communication sécurisée.")
