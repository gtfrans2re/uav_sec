"""
Interface CLI principale
------------------------
Permet de lancer les attaques et les défenses via un menu texte en ligne de commande.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logger import setup_logger
from utils.config import GPS_BASE_LAT, GPS_BASE_LON, SIMULATED_GPS_POINTS, GPS_SPOOF_FREQ

import subprocess
from utils.logger import setup_logger
from utils.config import *

logger = setup_logger()

# Commandes associées aux scripts d’attaque et de défense
ATTACK_COMMANDS = {
    "1": "python attacks/gps_spoofing.py",
    "2": "python attacks/dos_attack.py",
    "3": "python attacks/firmware_hack.py"
}

DEFENSE_COMMANDS = {
    "4": "python defenses/anomaly_detector.py",
    "5": "python defenses/encryption_module.py",
    "6": "python defenses/secure_comm.py"
}

def print_menu():
    print("\n" + "="*40)
    print("   SYSTÈME DE SÉCURITÉ UAV – MENU CLI")
    print("="*40)
    print("1. Lancer attaque GPS Spoofing")
    print("2. Lancer attaque DoS (UDP Flood)")
    print("3. Lancer modification Firmware")
    print("4. Activer détection d’anomalies GPS")
    print("5. Tester chiffrement/déchiffrement AES")
    print("6. Établir une communication TLS sécurisée")
    print("0. Quitter")
    print("="*40)

def execute_script(command):
    try:
        logger.info(f"Exécution de la commande : {command}")
        subprocess.run(command, shell=True)
    except Exception as e:
        logger.error(f"Erreur pendant l'exécution : {e}")

def main():
    while True:
        print_menu()
        choice = input("Sélectionnez une option : ").strip()
        if choice == "0":
            print("Fermeture du programme. À bientôt !")
            break
        elif choice in ATTACK_COMMANDS:
            execute_script(ATTACK_COMMANDS[choice])
        elif choice in DEFENSE_COMMANDS:
            execute_script(DEFENSE_COMMANDS[choice])
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()