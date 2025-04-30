import logging
import os

def setup_logger(log_file='logs/activity.log', name='uav_logger'):
    """
    Initialise et retourne un logger prêt à l'emploi.
    - Écrit les logs dans un fichier.
    - Affiche les logs dans la console.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Évite les doublons si le logger est déjà configuré
    if logger.hasHandlers():
        return logger

    # Création du dossier logs si besoin
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Format des messages de log
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Handler fichier
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # Handler console (optionnel mais pratique pour dev)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    # Ajout des handlers au logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger