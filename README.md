# ESP32-WifiScan-TFT
 A wifi scan programs in CircuitPython using the TFT integred screen .
## Fonctionnalités
- **Scan des réseaux Wi-Fi** : L'ESP32 détecte tous les réseaux Wi-Fi à proximité.
- **Navigation par boutons** :
  - **D0** pour naviguer vers le réseau précédent.
  - **D2** pour naviguer vers le réseau suivant.
- **Affichage cyclique** : Si tu atteins le premier ou dernier réseau, la navigation continue cycliquement.

## Matériel requis

- **ESP32 avec écran intégré** (ou un écran externe connecté à l'ESP32)
- **Boutons connectés aux broches D0 et D2**
- **Environnement de développement CircuitPython ou MicroPython**

## Utilisation

- **Démarrage** : Une fois le programme lancé, l'ESP32 scanne les réseaux Wi-Fi disponibles.
- **Navigation** : Utilise les boutons D0 et D2 pour naviguer entre les réseaux affichés.
- **Affichage** : Le nom du réseau (SSID) et la force du signal en pourcentage sont visibles sur l'écran.
