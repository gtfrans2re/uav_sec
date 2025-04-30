"""
Firmware Injection Simulator
----------------------------
Ce script simule une attaque où un fichier firmware malveillant est injecté dans
le répertoire système d'un drone. Dans un scénario réel, cela viserait à modifier
le comportement du drone de façon persistante.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logger import setup_logger
from utils.config import GPS_BASE_LAT, GPS_BASE_LON, SIMULATED_GPS_POINTS, GPS_SPOOF_FREQ

import os
import shutil
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Début de la simulation de modification du firmware...")

FAKE_FIRMWARE_PATH = "attacks/fake_firmware.bin"
TARGET_DIR = "firmware_upload_simulation/"

def create_fake_firmware():
    with open(FAKE_FIRMWARE_PATH, 'w') as f:
        f.write("!! MALICIOUS FIRMWARE PAYLOAD !!\n")
    logger.info("Fichier firmware malveillant créé.")

def simulate_injection():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    shutil.copy(FAKE_FIRMWARE_PATH, os.path.join(TARGET_DIR, "firmware_v2.bin"))
    logger.info(f"Firmware injecté dans {TARGET_DIR}")

if __name__ == "__main__":
    create_fake_firmware()
    simulate_injection()
    logger.info("Fin de la simulation de modification du firmware.")