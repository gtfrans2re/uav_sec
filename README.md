# uav_sec

> Projet de session du cours **INF8750 – Sécurité des systèmes informatiques**  
> Simulation d’attaques et de défenses sur UAVs (drones) en environnement local

## 🛡️ Description

Ce dépôt contient une plateforme de simulation pour la cybersécurité des UAVs (drones), combinant des **modules d’attaque** (GPS Spoofing, DoS, Firmware Hack) et des **mécanismes de défense** (Détection d’anomalies GPS, chiffrement AES, communication TLS), le tout orchestré par une interface en ligne de commande (CLI) et une application web Flask.

---

## 📁 Structure du projet

```
uav_sec/
├── attacks/              # Scripts d’attaque (DoS, GPS spoofing, etc.)
├── defenses/             # Scripts de défense (AES, TLS, etc.)
├── utils/                # Logger, config, outils communs
├── certs/                # Certificats TLS (server.crt, server.key)
├── templates/            # Interface HTML Flask
├── static/               # Styles CSS et fichiers statiques
├── main.py               # Menu CLI principal
├── app.py                # Application web Flask
├── requirements.txt      # Dépendances du projet
└── README.md             # Ce fichier
```

---

## ⚙️ Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/gtfrans2re/uav_sec.git
cd uav_sec
```

2. **Créer un environnement virtuel Python**

```bash
python3 -m venv .uav_env
source .uav_env/bin/activate
```

3. **Installer les dépendances**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **(Facultatif) Générer les certificats TLS auto-signés**

```bash
mkdir -p certs
openssl req -new -x509 -days 365 -nodes -out certs/server.crt -keyout certs/server.key
```

---

## 🚀 Utilisation

### 📟 Mode CLI

```bash
python main.py
```

Menu interactif :
```
1. Lancer attaque GPS Spoofing
2. Lancer attaque DoS (UDP Flood)
3. Lancer modification Firmware
4. Activer détection d’anomalies GPS
5. Tester chiffrement/déchiffrement AES
6. Établir une communication TLS sécurisée
0. Quitter
```

### 🌐 Mode Flask UI

```bash
python app.py
```

Puis ouvrir [http://127.0.0.1:5000](http://127.0.0.1:5000) dans votre navigateur.  
L’interface permet de sélectionner les attaques et défenses via un menu déroulant.

---

## 🧪 Simulation & Reproductibilité

- Toutes les attaques sont simulées en local (`127.0.0.1`) sans danger réel.
- Les logs sont enregistrés avec horodatage via `utils/logger.py`.
- La structure modulaire permet d’ajouter de nouveaux scripts dans `attacks/` ou `defenses/`.

---

## 📜 Licence

Distribué sous licence MIT — voir le fichier `LICENSE` pour plus d’informations.

---

## 👨‍💻 Auteur

Francois Gonothi Toure  
Projet présenté dans le cadre du cours **INF8750 – Sécurité des systèmes informatiques** à l’UQAM (session hiver 2025).
