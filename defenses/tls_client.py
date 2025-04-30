import socket
import ssl
import logging

# Configuration du logger
logger = logging.getLogger("uav_logger")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(levelname)s | uav_logger | %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def start_tls_client():
    server_address = '127.0.0.1'  # ou l'IP du serveur
    server_port = 65432

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

    # Charger le certificat du serveur pour la vérification
    #context.load_verify_locations('/certs/server.crt')
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    #context.load_cert_chain(certfile='/certs/client.crt', keyfile='/certs/client.key')
    context.set_ciphers('ECDHE-RSA-AES256-GCM-SHA384')  # Exemple de suite de chiffrement   
    try:
        with socket.create_connection((server_address, server_port)) as sock:
            with context.wrap_socket(sock, server_hostname=server_address) as ssock:
                logger.info("Connexion TLS établie avec le serveur.")

                message = "Bonjour depuis le client TLS UAV"
                ssock.sendall(message.encode())
                logger.info(f"Message envoyé : {message}")

                data = ssock.recv(1024)
                logger.info(f"Réponse du serveur : {data.decode()}")

    except Exception as e:
        logger.error(f"Erreur de connexion TLS : {e}")

if __name__ == "__main__":
    logger.info("Client TLS initialisé...")
    start_tls_client()
