# Hyundai Ioniq 5 (2025) - EU/Austria Features

## 🇪🇺 Europa-spezifische Funktionen / European Features

Diese Integration ist speziell für den europäischen Markt optimiert und bietet alle Funktionen, die für Ioniq 5 2025 Modelle in Österreich und der EU verfügbar sind.

### ✨ Exklusive EU 2023+ Funktionen

Ihr Ioniq 5 2025 (in Europa verkauft) unterstützt diese erweiterten Funktionen:

#### 🪟 Fenstersteuerung (Window Control)
```yaml
service: ioniq5_2025.set_windows
data:
  front_left: open    # oder: close
  front_right: open
  rear_left: open
  rear_right: open
target:
  device_id: YOUR_DEVICE_ID
```

**Anwendungsfälle:**
- Lüften bei heißem Wetter
- Schnelles Abkühlen vor der Fahrt
- Automatisches Schließen bei Regen

#### 🔑 Valet-Modus (Valet Mode)
```yaml
# Aktivieren
service: ioniq5_2025.start_valet_mode
target:
  device_id: YOUR_DEVICE_ID

# Deaktivieren
service: ioniq5_2025.stop_valet_mode
target:
  device_id: YOUR_DEVICE_ID
```

**Funktionen im Valet-Modus:**
- Geschwindigkeitsbegrenzung
- Begrenzter Zugriff auf Fahrzeugfunktionen
- Ideal beim Parken durch Dritte

#### 🔌 Ladeklappe steuern (Charge Port Control)
```yaml
# Öffnen
service: ioniq5_2025.open_charge_port
target:
  device_id: YOUR_DEVICE_ID

# Schließen
service: ioniq5_2025.close_charge_port
target:
  device_id: YOUR_DEVICE_ID
```

**Praktisch für:**
- Automatisches Öffnen vor geplanter Ladezeit
- Fernöffnung wenn Ladekabel vergessen

#### ⚡ V2L - Vehicle to Load (Fahrzeug als Stromquelle)
```yaml
service: number.set_value
data:
  value: 80  # Maximale Entladung bis 80%
target:
  entity_id: number.ioniq5_v2l_limit
```

**V2L Anwendungen:**
- Campingausrüstung betreiben
- Werkzeuge auf Baustellen
- Notstromversorgung zuhause
- Andere EVs laden

**Technische Daten V2L (Ioniq 5):**
- Maximale Leistung: 3.6 kW
- Spannung: 230V (EU)
- Steckdose: Schuko (EU) im Fahrzeug

### 🌍 API-Endpunkt: Europa

**Base URL für Österreich/EU:**
```
https://prd.eu-ccapi.hyundai.com:8080
```

**Verfügbare API-Versionen:**
- `/api/v1/spa/` - Basis-Funktionen
- `/api/v2/spa/` - Erweiterte Funktionen (inkl. Fenster, Valet)
- `/api/v2/spa/vehicles/{id}/ccs2/` - CCS2-spezifische Funktionen

### 📊 Alle verfügbaren Sensoren & Steuerungen

#### Batterieverwaltung
- `sensor.ioniq5_ev_batterie` - Batteriestand (%)
- `sensor.ioniq5_ev_reichweite` - Reichweite (km)
- `sensor.ioniq5_12v_batterie` - 12V Batterie (V)
- `sensor.ioniq5_ladeleistung` - Aktuelle Ladeleistung (kW)
- `sensor.ioniq5_ladezeit` - Zeit bis vollständig geladen
- `binary_sensor.ioniq5_ladevorgang` - Lädt: Ja/Nein
- `binary_sensor.ioniq5_stecker_eingesteckt` - Stecker: Ja/Nein

#### Lade-Steuerung
- `ioniq5_2025.start_charge` - Laden starten
- `ioniq5_2025.stop_charge` - Laden stoppen
- `ioniq5_2025.set_charge_limits` - AC/DC Limits (50-100%)
- `ioniq5_2025.set_charging_current` - Ladestrom (100%, 90%, 60%)
- `ioniq5_2025.open_charge_port` - Ladeklappe öffnen ⭐
- `ioniq5_2025.close_charge_port` - Ladeklappe schließen ⭐

#### Klimatisierung
- `climate.ioniq5_klima` - Klimasteuerung
- `sensor.ioniq5_aussentemperatur` - Außentemperatur (°C)
- `sensor.ioniq5_innentemperatur` - Innentemperatur (°C)
- `ioniq5_2025.start_climate` - Klimatisierung starten
- `ioniq5_2025.stop_climate` - Klimatisierung stoppen

**Climate-Optionen (EU):**
```yaml
service: ioniq5_2025.start_climate
data:
  temperature: 21        # 16-30°C
  defrost: true         # Scheibenentfrostung
  heating: true         # Lenkrad- & Heckscheibenheizung
  flseat: heat          # Fahrersitz: heat/cool/off
  frseat: heat          # Beifahrersitz: heat/cool/off
  duration: 30          # Dauer in Minuten
target:
  device_id: YOUR_DEVICE_ID
```

#### Fahrzeugzugang
- `lock.ioniq5_tuerschloss` - Ver-/Entriegeln
- `binary_sensor.ioniq5_tueren` - Türen Status
- `binary_sensor.ioniq5_fenster` - Fenster Status
- `binary_sensor.ioniq5_motorhaube` - Motorhaube Status
- `binary_sensor.ioniq5_kofferraum` - Kofferraum Status
- `ioniq5_2025.set_windows` - Fenster steuern ⭐

#### Standort & Navigation
- `device_tracker.ioniq5_standort` - GPS Position
- `sensor.ioniq5_adresse` - Adresse (OpenStreetMap)
- `sensor.ioniq5_km_stand` - Kilometerstand

#### Sicherheit & Status
- `binary_sensor.ioniq5_motor` - Motor läuft
- `sensor.ioniq5_reifendruck_vl` - Reifendruck vorne links
- `sensor.ioniq5_reifendruck_vr` - Reifendruck vorne rechts
- `sensor.ioniq5_reifendruck_hl` - Reifendruck hinten links
- `sensor.ioniq5_reifendruck_hr` - Reifendruck hinten rechts

#### Erweitert (EU 2023+) ⭐
- `number.ioniq5_v2l_limit` - V2L Entladegrenze
- `ioniq5_2025.start_valet_mode` - Valet-Modus aktivieren
- `ioniq5_2025.stop_valet_mode` - Valet-Modus deaktivieren
- `ioniq5_2025.start_hazard_lights` - Warnblinker
- `ioniq5_2025.start_hazard_lights_and_horn` - Warnblinker + Hupe

⭐ = Exklusiv für EU 2023+ Modelle (inkl. Ioniq 5 2025)

### 🇦🇹 Österreich-spezifische Optimierungen

#### Zeitzone
- Standard: `Europe/Vienna`
- Automatische Sommer-/Winterzeitumstellung

#### Einheiten
- Distanz: Kilometer (km)
- Temperatur: Celsius (°C)
- Energieverbrauch: kWh/100km
- Reifendruck: bar

#### Sprache
- UI: Deutsch/English
- Entitätsnamen: Deutsch konfigurierbar
- Service-Beschreibungen: Deutsch

#### Stromtarife Integration
Kompatibel mit österreichischen Energieversorgern:
- **aWATTar** - Stündliche Strompreise
- **Tibber** - Dynamische Tarife
- **Wien Energie** - Nachtstrom-Tarife
- **EVN** - Niedertarif-Zeiten

**Beispiel: Laden wenn Strom günstig**
```yaml
automation:
  - alias: "Günstig laden mit aWATTar"
    trigger:
      - platform: numeric_state
        entity_id: sensor.awattar_strompreis
        below: 0.15  # Unter 15 Cent/kWh
    condition:
      - condition: numeric_state
        entity_id: sensor.ioniq5_ev_batterie
        below: 80
      - condition: state
        entity_id: binary_sensor.ioniq5_stecker_eingesteckt
        state: 'on'
    action:
      - service: ioniq5_2025.start_charge
        target:
          device_id: YOUR_DEVICE_ID
```

### 🏠 Smart Home Integrationen

#### PV-Überschuss-Laden
```yaml
automation:
  - alias: "PV-Überschuss laden"
    trigger:
      - platform: numeric_state
        entity_id: sensor.pv_ueberschuss_aktuell
        above: 3000  # 3kW Überschuss
        for: "00:05:00"
    condition:
      - condition: state
        entity_id: binary_sensor.ioniq5_stecker_eingesteckt
        state: 'on'
      - condition: numeric_state
        entity_id: sensor.ioniq5_ev_batterie
        below: 90
    action:
      - service: ioniq5_2025.start_charge
        target:
          device_id: YOUR_DEVICE_ID
```

#### Wallbox-Steuerung
```yaml
# Wallbox nur aktivieren wenn Ioniq 5 angesteckt
automation:
  - alias: "Wallbox für Ioniq 5"
    trigger:
      - platform: state
        entity_id: binary_sensor.ioniq5_stecker_eingesteckt
        to: 'on'
    action:
      - service: switch.turn_on
        target:
          entity_id: switch.wallbox_laden
      - service: number.set_value
        data:
          value: 11  # 11 kW Ladeleistung
        target:
          entity_id: number.wallbox_ladestrom
```

### 🔋 Batterie-Optimierung für EU-Klima

#### Winter (< 5°C)
- Vorheizen vor Fahrt (bessere Reichweite)
- Ladegrenze 80% (Batteriegesundheit)
- Häufigere Updates vermeiden (12V-Batterie)

```yaml
automation:
  - alias: "Winter-Vorheizen"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: numeric_state
        entity_id: sensor.aussentemperatur
        below: 5
    action:
      - service: ioniq5_2025.start_climate
        data:
          temperature: 21
          defrost: true
          heating: true
          duration: 20
        target:
          device_id: YOUR_DEVICE_ID
```

#### Sommer (> 25°C)
- Belüftung vor Fahrt
- Fenster automatisch öffnen
- AC-Laden bevorzugen (geringere Hitzeentwicklung)

```yaml
automation:
  - alias: "Sommer-Kühlung"
    trigger:
      - platform: numeric_state
        entity_id: sensor.ioniq5_innentemperatur
        above: 30
    action:
      - service: ioniq5_2025.set_windows
        data:
          front_left: open
          front_right: open
        target:
          device_id: YOUR_DEVICE_ID
      - delay: "00:02:00"
      - service: ioniq5_2025.start_climate
        data:
          temperature: 22
          duration: 10
        target:
          device_id: YOUR_DEVICE_ID
```

### 📱 Dashboard-Empfehlung für EU

```yaml
type: vertical-stack
cards:
  - type: entity
    entity: sensor.ioniq5_ev_batterie
    name: Batteriestand
    icon: mdi:battery-charging-80
    
  - type: horizontal-stack
    cards:
      - type: entity
        entity: sensor.ioniq5_reichweite
        name: Reichweite
      - type: entity
        entity: sensor.ioniq5_km_stand
        name: KM-Stand
        
  - type: entities
    title: Ladesteuerung
    entities:
      - entity: binary_sensor.ioniq5_ladevorgang
        name: Ladevorgang aktiv
      - entity: sensor.ioniq5_ladeleistung
        name: Ladeleistung
      - entity: sensor.ioniq5_ladezeit
        name: Zeit bis voll
      - type: button
        name: Laden starten
        action_name: Starten
        tap_action:
          action: call-service
          service: ioniq5_2025.start_charge
      - type: button
        name: Laden stoppen
        action_name: Stoppen
        tap_action:
          action: call-service
          service: ioniq5_2025.stop_charge
          
  - type: thermostat
    entity: climate.ioniq5_klima
    name: Klimatisierung
    
  - type: map
    entities:
      - device_tracker.ioniq5_standort
    hours_to_show: 24
```

### 🛡️ Datenschutz & DSGVO

#### Datenverarbeitung
- **Standortdaten**: Werden über Hyundai Bluelink EU-Server verarbeitet
- **Geocoding**: Optional über OpenStreetMap (EU-konform)
- **Lokale Verarbeitung**: Home Assistant speichert Daten lokal

#### DSGVO-Compliance
✅ Einwilligung erforderlich (bei Hyundai.com)  
✅ Datenminimierung (nur notwendige Daten)  
✅ Speicherung in EU (Hyundai EU-Server)  
✅ Lokale Kontrolle (Home Assistant)  

### 📞 Support für EU-Nutzer

**Probleme mit EU-Login:**
- [EU Login Flow Guide](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api/wiki/Kia-Europe-Login-Flow)
- Hyundai Bluelink Support: +43 (Österreich) oder lokale Nummer

**Community:**
- [Home Assistant Community (Deutsch)](https://community.home-assistant.io/)
- [Ioniq 5 Forum](https://www.ioniqforum.com/)
- [GitHub Issues](https://github.com/your_username/ioniq5_2025/issues)

---

**🇪🇺 Diese Integration ist vollständig für den europäischen Markt optimiert und unterstützt alle verfügbaren Funktionen Ihres Ioniq 5 2025!**
