# Hyundai Ioniq 5 (2025) - Europa / Österreich Installationsanleitung

Willkommen! Diese Anleitung ist speziell für österreichische und europäische Ioniq 5 2025 Besitzer optimiert.

## 🇦🇹 Für österreichische Benutzer

Diese Integration wurde speziell für den europäischen Markt konfiguriert und funktioniert einwandfrei in Österreich mit:
- ✅ Hyundai Bluelink Europa
- ✅ Deutsche/Österreichische Benutzeroberfläche
- ✅ Metrische Einheiten (km, °C)
- ✅ Europäische Zeitzone
- ✅ Alle EU 2023+ Funktionen

## ⚠️ WICHTIG: EU Einwilligung erforderlich

**Bevor Sie beginnen**, müssen Sie die Datenverarbeitung bei Hyundai akzeptieren:

1. Besuchen Sie **https://www.hyundai.com/de** (oder .at für Österreich)
2. Melden Sie sich mit Ihren Bluelink-Zugangsdaten an
3. Akzeptieren Sie die **Einwilligung zur Datenverarbeitung**
4. Warten Sie 5-10 Minuten
5. Dann erst mit Home Assistant fortfahren

**Warum?** Ohne diese Einwilligung schlägt die Authentifizierung fehl. Dies ist eine EU-DSGVO Anforderung.

## 📋 Voraussetzungen

### Was Sie benötigen:
- ✅ Home Assistant 2024.1.0 oder neuer
- ✅ Hyundai Ioniq 5 2025 (in Österreich/EU gekauft)
- ✅ Aktives **Hyundai Bluelink** Konto
- ✅ Ioniq 5 in der Bluelink App registriert
- ✅ Ihre Bluelink E-Mail und Passwort
- ✅ Internetverbindung

### Nicht benötigt:
- ❌ PIN (optional in EU, nur bei Bedarf)
- ❌ API-Schlüssel (verwendet OpenStreetMap kostenlos)

## 🚀 Installation

### Methode 1: HACS (Empfohlen) 🌟

1. **HACS öffnen** in Home Assistant
2. Gehen Sie zu **Integrationen**
3. Klicken Sie auf **⋮** (drei Punkte) oben rechts
4. Wählen Sie **Benutzerdefinierte Repositories**
5. Repository hinzufügen:
   - **Repository**: `https://github.com/your_username/ioniq5_2025`
   - **Kategorie**: `Integration`
6. Suchen Sie nach "**Hyundai Ioniq 5**"
7. Klicken Sie auf **Herunterladen**
8. **Home Assistant neu starten**

### Methode 2: Manuell 📦

1. Laden Sie dieses Repository herunter
2. Kopieren Sie `custom_components/ioniq5_2025/` nach:
   ```
   <HA-Verzeichnis>/custom_components/ioniq5_2025/
   ```
3. **Home Assistant neu starten**

## ⚙️ Konfiguration

### Schritt 1: Integration hinzufügen

1. **Einstellungen** → **Geräte & Dienste**
2. Klicken Sie auf **+ Integration hinzufügen**
3. Suchen Sie nach "**Hyundai Ioniq 5**"

### Schritt 2: Zugangsdaten eingeben

| Feld | Wert für Österreich/EU |
|------|------------------------|
| **E-Mail** | Ihre Bluelink E-Mail-Adresse |
| **Passwort** | Ihr Bluelink Passwort |
| **Region** | **Europa** (vorausgewählt) |
| **Marke** | **Hyundai** (vorausgewählt) |
| **PIN** | Leer lassen (außer Sie haben einen gesetzt) |

### Schritt 3: Auf Erkennung warten

- Die Integration verbindet sich mit Hyundai Bluelink Europa
- Ihr Ioniq 5 wird automatisch erkannt
- Dies dauert 30-60 Sekunden

### Schritt 4: Fertig! 🎉

Sie sehen jetzt:
- Gerät: **Hyundai Ioniq 5**
- Viele Sensoren und Steuerungen
- Verfügbare Dienste

## 🔧 Erweiterte Einstellungen (Optional)

Nach der Einrichtung klicken Sie auf **Konfigurieren** für:

### Empfohlene Einstellungen für Österreich:

| Einstellung | Empfohlener Wert | Erklärung |
|-------------|------------------|-----------|
| **Aktualisierungs-Intervall** | 30 Minuten | Wie oft gecachte Daten abgerufen werden |
| **Force-Refresh-Intervall** | 240 Minuten (4 Std) | Wie oft das Auto geweckt wird |
| **Ruhezeit Beginn** | 23 Uhr | Keine Updates ab dieser Zeit |
| **Ruhezeit Ende** | 6 Uhr | Updates ab dieser Zeit wieder |
| **Geolokalisierung** | ✅ Aktiviert | Zeigt Adresse statt nur GPS |
| **E-Mail bei Geocode** | ❌ Deaktiviert | Nicht nötig für OpenStreetMap |

**Warum diese Einstellungen?**
- **4-Stunden Force-Refresh**: Schont die 12V-Batterie, reicht für die meisten Anwendungen
- **Ruhezeit 23-6 Uhr**: Verhindert nächtliches Wecken des Fahrzeugs
- **Geolokalisierung**: OpenStreetMap ist kostenlos und funktioniert gut in Österreich

## 📊 Verfügbare Entitäten

Nach der Einrichtung haben Sie Zugriff auf:

### 🔋 Batterie & Laden
- `sensor.ioniq5_ev_batterie` - Batteriestand in %
- `sensor.ioniq5_reichweite` - Restreichweite in km
- `sensor.ioniq5_ladeleistung` - Aktuelle Ladeleistung in kW
- `binary_sensor.ioniq5_ladevorgang` - Lädt ja/nein
- `binary_sensor.ioniq5_stecker` - Stecker eingesteckt ja/nein

### 📍 Standort
- `device_tracker.ioniq5_standort` - GPS Position
- `sensor.ioniq5_adresse` - Adresse (wenn Geolokalisierung aktiv)
- `sensor.ioniq5_km_stand` - Kilometerstand

### 🚪 Fahrzeugstatus
- `lock.ioniq5_tuerschloss` - Türen ver-/entriegeln
- `binary_sensor.ioniq5_tueren` - Türen offen/zu
- `binary_sensor.ioniq5_fenster` - Fenster offen/zu
- `binary_sensor.ioniq5_kofferraum` - Kofferraum offen/zu
- `binary_sensor.ioniq5_motorhaube` - Motorhaube offen/zu

### 🌡️ Klimatisierung
- `climate.ioniq5_klima` - Klimasteuerung
- `sensor.ioniq5_innentemperatur` - Innenraumtemperatur

### 🔧 Weitere
- `sensor.ioniq5_12v_batterie` - 12V Batterie
- `sensor.ioniq5_reifendruck` - Reifendruckwarnungen
- `number.ioniq5_v2l_limit` - V2L Entladegrenze

## 🎯 Verfügbare Dienste (Actions)

### Wichtigste Dienste für EU-Modelle:

| Dienst | Beschreibung | Verfügbarkeit |
|--------|--------------|---------------|
| `update` | Gecachte Daten abrufen | ✅ Alle |
| `force_update` | Fahrzeug wecken für frische Daten | ✅ Alle |
| `start_climate` | Klimatisierung starten | ✅ Alle |
| `stop_climate` | Klimatisierung stoppen | ✅ Alle |
| `start_charge` | Laden starten | ✅ Alle |
| `stop_charge` | Laden stoppen | ✅ Alle |
| `set_charge_limits` | Ladegrenzen einstellen | ✅ Alle |
| `lock` / `unlock` | Ver-/Entriegeln | ✅ Alle |
| `open_charge_port` | Ladeklappe öffnen | ✅ EU 2023+ |
| `close_charge_port` | Ladeklappe schließen | ✅ EU 2023+ |
| `set_windows` | Fenster steuern | ✅ EU 2023+ |
| `start_valet_mode` | Valet-Modus aktivieren | ✅ EU 2023+ |
| `stop_valet_mode` | Valet-Modus deaktivieren | ✅ EU 2023+ |

**EU 2023+** = Alle ab 2023 in Europa verkauften Ioniq 5 (inkl. 2025er Modell)

## 🤖 Beispiel-Automatisierungen

### 1. Nachtladung (günstiger Strom)
```yaml
automation:
  - alias: "Ioniq 5 nachts laden"
    trigger:
      - platform: time
        at: "23:00:00"
    condition:
      - condition: numeric_state
        entity_id: sensor.ioniq5_ev_batterie
        below: 80
      - condition: state
        entity_id: binary_sensor.ioniq5_stecker
        state: 'on'
    action:
      - service: ioniq5_2025.start_charge
        target:
          device_id: IHR_GERAETE_ID
```

### 2. Vorheizen vor Arbeitsweg
```yaml
automation:
  - alias: "Ioniq 5 vorheizen"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: state
        entity_id: binary_sensor.workday_sensor
        state: 'on'
      - condition: numeric_state
        entity_id: sensor.aussentemperatur
        below: 10
    action:
      - service: ioniq5_2025.start_climate
        data:
          temperature: 21
          defrost: true
          heating: true
        target:
          device_id: IHR_GERAETE_ID
```

### 3. Benachrichtigung bei niedrigem Batteriestand
```yaml
automation:
  - alias: "Ioniq 5 Batterie niedrig"
    trigger:
      - platform: numeric_state
        entity_id: sensor.ioniq5_ev_batterie
        below: 20
    action:
      - service: notify.mobile_app
        data:
          title: "⚠️ Ioniq 5 Batterie niedrig"
          message: "Batteriestand: {{ states('sensor.ioniq5_ev_batterie') }}%"
```

### 4. Automatisches Verriegeln beim Verlassen
```yaml
automation:
  - alias: "Ioniq 5 verriegeln beim Verlassen"
    trigger:
      - platform: state
        entity_id: person.ihr_name
        from: 'home'
        to: 'not_home'
    condition:
      - condition: state
        entity_id: lock.ioniq5_tuerschloss
        state: 'unlocked'
    action:
      - service: lock.lock
        target:
          entity_id: lock.ioniq5_tuerschloss
      - service: notify.mobile_app
        data:
          message: "Ioniq 5 wurde automatisch verriegelt"
```

### 5. Ladevorgang bei 80% stoppen
```yaml
automation:
  - alias: "Ioniq 5 Laden bei 80% stoppen"
    trigger:
      - platform: numeric_state
        entity_id: sensor.ioniq5_ev_batterie
        above: 79
    condition:
      - condition: state
        entity_id: binary_sensor.ioniq5_ladevorgang
        state: 'on'
    action:
      - service: ioniq5_2025.stop_charge
        target:
          device_id: IHR_GERAETE_ID
      - service: notify.mobile_app
        data:
          message: "Ioniq 5 Ladevorgang bei {{ states('sensor.ioniq5_ev_batterie') }}% gestoppt"
```

## 🔍 Fehlerbehebung

### ❌ "Ungültige Anmeldedaten"

**Lösung**:
1. Bei www.hyundai.com/de anmelden
2. Einwilligung zur Datenverarbeitung akzeptieren
3. 10 Minuten warten
4. Nochmal in Home Assistant versuchen
5. Falls weiterhin Fehler: Passwort in Bluelink App zurücksetzen

### ❌ Integration wird nicht gefunden

**Lösung**:
1. Home Assistant neu starten
2. Browser-Cache leeren (Strg+F5)
3. Prüfen ob `custom_components/ioniq5_2025/` existiert
4. Logs in **Einstellungen** → **System** → **Protokolle** prüfen

### ❌ Keine Entitäten erstellt

**Lösung**:
1. 2-3 Minuten warten
2. Dienst `ioniq5_2025.force_update` aufrufen
3. Prüfen ob Ioniq 5 in Bluelink App sichtbar ist
4. Debug-Logging aktivieren (siehe unten)

### ❌ "Config Not Ready" Fehler

**Lösung**:
1. Internetverbindung prüfen
2. Bluelink-Dienst Status prüfen (Bluelink App testen)
3. Home Assistant neu starten
4. Integration entfernen und neu hinzufügen

### 🔧 Debug-Logging aktivieren

Für detaillierte Fehlersuche:

**Variante 1** (einfach):
1. Zu Integration gehen
2. **Debug-Logging aktivieren** klicken
3. Problem reproduzieren
4. **Diagnose herunterladen** klicken

**Variante 2** (dauerhaft):
In `configuration.yaml` hinzufügen:
```yaml
logger:
  default: info
  logs:
    custom_components.ioniq5_2025: debug
    hyundai_kia_connect_api: debug
```
Dann Home Assistant neu starten.

## 🌍 Österreich-spezifische Hinweise

### Stromtarife & Laden
Viele österreichische Energieversorger bieten günstigere Nachttarife:
- **Wien Energie**: Nachtstrom 22:00-06:00
- **EVN**: Niedertarif 20:00-06:00
- **Energie Steiermark**: Nachtstrom 20:00-07:00

→ Passen Sie die Lade-Automatisierungen entsprechend an!

### Wallbox-Integration
Die Integration funktioniert perfekt mit:
- go-eCharger (österreichisches Produkt)
- Fronius Wattpilot
- KEBA KeContact P30

### Photovoltaik
Kombinieren Sie mit Ihrer PV-Anlage:
```yaml
# Laden nur wenn PV-Überschuss vorhanden
automation:
  - alias: "PV-Überschuss Laden"
    trigger:
      - platform: numeric_state
        entity_id: sensor.pv_ueberschuss
        above: 3000  # 3kW Überschuss
        for: "00:05:00"
    action:
      - service: ioniq5_2025.start_charge
```

## 📱 Dashboard-Karten

### Ioniq 5 Status-Karte (Lovelace)
```yaml
type: entities
title: Hyundai Ioniq 5
entities:
  - entity: sensor.ioniq5_ev_batterie
    name: Batteriestand
  - entity: sensor.ioniq5_reichweite
    name: Reichweite
  - entity: binary_sensor.ioniq5_ladevorgang
    name: Ladevorgang
  - entity: sensor.ioniq5_ladeleistung
    name: Ladeleistung
  - entity: lock.ioniq5_tuerschloss
    name: Türschloss
  - entity: sensor.ioniq5_km_stand
    name: Kilometerstand
  - entity: device_tracker.ioniq5_standort
    name: Standort
```

## 💡 Tipps & Tricks

### API-Limits beachten
- ❌ Nicht jede Minute force_update aufrufen
- ✅ Force-Update max. alle 4 Stunden
- ✅ Gecachte Updates beliebig oft (alle 30 Min OK)

### 12V-Batterie schonen
- Ruhezeit 23:00-06:00 Uhr nutzen
- Nicht zu häufige Force-Updates
- Auto regelmäßig fahren (>30 Min/Woche)

### Reichweiten-Optimierung
Der Sensor zeigt die vom Fahrzeug berechnete Reichweite. Faktoren:
- Fahrstil
- Außentemperatur
- Heizung/Klimaanlage
- Geschwindigkeit

## 🆘 Support

### Hilfe bekommen:
- 📖 [Vollständige Dokumentation](README.md)
- 🐛 [GitHub Issues](https://github.com/your_username/ioniq5_2025/issues)
- 💬 [Home Assistant Community (Deutsch)](https://community.home-assistant.io/)
- 💬 [Ioniq 5 Forum Österreich](https://www.ioniqforum.com/)

### Logs teilen:
Wenn Sie Hilfe benötigen, teilen Sie:
- Home Assistant Version
- Ioniq 5 Baujahr und Modelljahr
- Fehlermeldung
- Debug-Logs (persönliche Daten entfernen!)

## 🎉 Viel Erfolg!

Ihre Integration ist nun optimal für Österreich/Europa konfiguriert. Genießen Sie die smarte Steuerung Ihres Ioniq 5!

**Wichtiger Hinweis**: Diese Integration ist ein Community-Projekt und nicht offiziell von Hyundai unterstützt. Nutzung auf eigene Verantwortung.

---

**🇦🇹 Entwickelt mit ❤️ für österreichische Ioniq 5 Besitzer**
