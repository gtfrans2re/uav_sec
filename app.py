from flask import Flask, render_template, request, redirect, url_for, flash
from utils.logger import setup_logger
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'uav_secure_key'

# Configuration du logger
logger = setup_logger()

# Chemins vers les scripts d'attaque et de défense
ATTACK_SCRIPTS = {
    'gps_spoofing': 'attacks/gps_spoofing.py',
    'dos_attack': 'attacks/dos_attack.py',
    'firmware_hack': 'attacks/firmware_hack.py'
}

DEFENSE_SCRIPTS = {
    'anomaly_detector': 'defenses/anomaly_detector.py',
    'encryption_module': 'defenses/encryption_module.py',
    'secure_comm': 'defenses/secure_comm.py'
}

def run_script(script_path):
    try:
        logger.info(f"Lancement du script : {script_path}")
        subprocess.Popen(['python', script_path])
        return True
    except Exception as e:
        logger.error(f"Erreur lors du lancement de {script_path} : {e}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/launch_attack', methods=['POST'])
def launch_attack():
    attack_type = request.form.get('attack')
    if attack_type in ATTACK_SCRIPTS:
        success = run_script(ATTACK_SCRIPTS[attack_type])
        flash(f"Attaque '{attack_type}' lancée avec succès !" if success else "Échec du lancement.", 'info')
    return redirect(url_for('index'))

@app.route('/launch_defense', methods=['POST'])
def launch_defense():
    defense_type = request.form.get('defense')
    if defense_type in DEFENSE_SCRIPTS:
        success = run_script(DEFENSE_SCRIPTS[defense_type])
        flash(f"Défense '{defense_type}' activée avec succès !" if success else "Échec de l'activation.", 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)