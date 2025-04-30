import logging
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Configuration du logger
logger = logging.getLogger("uav_logger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(levelname)s | %(name)s | %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Taille des blocs AES
BLOCK_SIZE = AES.block_size  # 16 octets

def generate_aes_key():
    """Génère une clé AES de 128 bits (16 octets)."""
    key = get_random_bytes(16)
    logger.info(f"Clé générée : {b64encode(key).decode()}")
    return key

def encrypt_message(message, key):
    """Chiffre un message texte avec AES en mode ECB (avec padding)."""
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(message.encode(), BLOCK_SIZE)
    encrypted = cipher.encrypt(padded)
    logger.info("Message chiffré avec succès.")
    return encrypted

def decrypt_message(ciphertext, key):
    """Déchiffre un message AES ECB et retire le padding."""
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_padded = cipher.decrypt(ciphertext)
    decrypted = unpad(decrypted_padded, BLOCK_SIZE)
    logger.info("Message déchiffré avec succès.")
    return decrypted.decode()

if __name__ == "__main__":
    logger.info("Initialisation du module de chiffrement AES...")

    original = "UAV secure test message"
    logger.info(f"Message original : {original}")

    try:
        key = generate_aes_key()
        encrypted = encrypt_message(original, key)
        encrypted_b64 = b64encode(encrypted).decode()
        logger.info(f"Texte chiffré (base64) : {encrypted_b64}")

        decrypted = decrypt_message(encrypted, key)
        logger.info(f"Texte déchiffré : {decrypted}")
    except Exception as e:
        logger.error(f"Erreur lors du chiffrement/déchiffrement : {e}")
