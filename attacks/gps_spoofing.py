"""
GPS Spoofing Attack Simulator
-----------------------------
Ce script simule une attaque de spoofing GPS en envoyant de fausses coordonnées à un drone.
L’objectif est de perturber la navigation du drone en le redirigeant vers des zones non prévues.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logger import setup_logger
from utils.config import GPS_BASE_LAT, GPS_BASE_LON, SIMULATED_GPS_POINTS, GPS_SPOOF_FREQ

import time
import random
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Début de l'attaque GPS Spoofing...")

def fake_gps_coordinates():
    """
    Génère une fausse série de coordonnées GPS simulées.
    """
    latitude = random.uniform(48.8, 49.0)
    longitude = random.uniform(2.2, 2.5)
    altitude = random.uniform(20.0, 30.0)
    return latitude, longitude, altitude

def send_fake_gps():
    """
    Simule l’envoi de coordonnées GPS à une interface drone fictive.
    En réalité, dans un environnement matériel, cela nécessiterait un
    émetteur SDR configuré pour injecter ces signaux.
    """
    for i in range(20):  # Boucle pour 20 paquets fictifs
        lat, lon, alt = fake_gps_coordinates()
        logger.info(f"Injection GPS Spoof #{i+1} : Latitude={lat}, Longitude={lon}, Altitude={alt}")
        time.sleep(1.5)  # Simule le temps entre les paquets

if __name__ == "__main__":
    send_fake_gps()
    logger.info("Fin de l’attaque GPS Spoofing.")