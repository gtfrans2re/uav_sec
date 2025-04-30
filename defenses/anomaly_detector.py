"""
Détection d’anomalies GPS en temps réel
---------------------------------------
Ce module lit un flux simulé de coordonnées GPS et détecte des écarts brutaux
qui peuvent révéler une attaque de type GPS spoofing.
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
logger.info("Démarrage du module de détection d'anomalies...")

def simulate_gps_stream():
    """
    Simule un flux de données GPS normales avec de rares anomalies.
    """
    base_lat, base_lon = 48.85, 2.35
    for i in range(30):
        # Injecte aléatoirement des anomalies (sauts de coordonnées)
        if random.random() < 0.15:
            lat = base_lat + random.uniform(0.01, 0.05)  # anomalie
            lon = base_lon + random.uniform(0.01, 0.05)
        else:
            lat = base_lat + random.uniform(-0.0002, 0.0002)
            lon = base_lon + random.uniform(-0.0002, 0.0002)

        yield (lat, lon)
        time.sleep(1)

def detect_anomalies():
    prev_lat, prev_lon = None, None
    for lat, lon in simulate_gps_stream():
        if prev_lat is not None:
            delta = ((lat - prev_lat)**2 + (lon - prev_lon)**2)**0.5
            if delta > 0.005:
                logger.warning(f"Anomalie détectée ! Δ={delta:.5f} | GPS: {lat:.5f}, {lon:.5f}")
            else:
                logger.info(f"GPS normal : {lat:.5f}, {lon:.5f}")
        prev_lat, prev_lon = lat, lon

if __name__ == "__main__":
    detect_anomalies()
    logger.info("Fin du module de détection d'anomalies.")
