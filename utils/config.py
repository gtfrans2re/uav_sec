"""
Fichier de configuration global
-------------------------------
Contient toutes les constantes et paramètres partagés du projet UAV Secure.
Modifiable en un seul endroit pour adapter le comportement de tous les modules.
"""

# === Réseau ===
TARGET_IP = "192.168.0.100"       # IP cible pour les attaques réseau (DoS)
TARGET_PORT = 14550               # Port UDP cible (ex. MAVLink)

# === Spoofing GPS ===
GPS_BASE_LAT = 48.8566
GPS_BASE_LON = 2.3522
GPS_ANOMALY_THRESHOLD = 0.005     # Seuil de détection d'anomalie GPS

# === DoS ===
DOS_DURATION = 15                 # Durée d'une attaque DoS (secondes)
DOS_PACKET_SIZE = 1024           # Taille des paquets UDP envoyés

# === Firmware Hack ===
FIRMWARE_PATH = "attacks/fake_firmware.bin"
FIRMWARE_TARGET_DIR = "firmware_upload_simulation/"
FIRMWARE_OUTPUT = "firmware_v2.bin"

# === Cryptographie ===
AES_KEY_LENGTH = 32              # AES-256
AES_BLOCK_SIZE = 16              # Bloc AES

# === TLS Communication ===
TLS_HOST = "127.0.0.1"
TLS_PORT = 65432

# === Journalisation ===
LOG_FILE_PATH = "logs/activity.log"

# === Flask App ===
FLASK_SECRET_KEY = "uav_secure_key"

# === UI / Simulation ===
SIMULATED_GPS_POINTS = 30
GPS_SPOOF_FREQ = 0.15
GPS_UPDATE_INTERVAL = 1  # secondes

# === Drone Models (Future Extension) ===
SUPPORTED_DRONES = ["DJI Mavic Mini", "DJI Phantom 4 Pro v2"]
