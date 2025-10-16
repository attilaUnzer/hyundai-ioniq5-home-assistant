# Hyundai Ioniq 5 (2025) - Europa Edition
## 🇦🇹 Zusammenfassung für österreichische Benutzer

### ✅ Was wurde erstellt

Eine **vollständig für Europa/Österreich optimierte** Home Assistant Integration für Ihren Ioniq 5 2025.

### 🎯 EU-Spezifische Anpassungen

#### 1. **Voreinstellungen**
- ✅ Region: **Europa** (vorausgewählt)
- ✅ Marke: **Hyundai** (vorausgewählt)
- ✅ API-Endpunkt: `https://prd.eu-ccapi.hyundai.com:8080`
- ✅ Force-Refresh: **4 Stunden** (schont 12V-Batterie)
- ✅ Ruhezeit: **23:00 - 06:00 Uhr** (österreichische Zeitzone)
- ✅ Geolokalisierung: **Aktiviert** (OpenStreetMap)

#### 2. **Deutsche Benutzeroberfläche**
- ✅ Komplette deutsche Übersetzung in `de.json`
- ✅ UI-Texte auf Deutsch/Englisch
- ✅ Service-Beschreibungen auf Deutsch
- ✅ Österreichische Terminologie

#### 3. **EU 2023+ Funktionen** ⭐
Ihr Ioniq 5 2025 unterstützt:
- ✅ **Fenstersteuerung** - Fenster öffnen/schließen
- ✅ **Valet-Modus** - Sicheres Parken durch Dritte
- ✅ **Ladeklappe steuern** - Fernöffnen/-schließen
- ✅ **V2L (Vehicle-to-Load)** - Fahrzeug als Stromquelle (3.6 kW)
- ✅ **Erweiterte Ladesteuerung** - AC/DC Limits, Ladestrom
- ✅ **Warnblinker & Hupe** - Sicherheitsfunktionen

#### 4. **Dokumentation auf Deutsch**
- 📖 **EU_SETUP_GUIDE.md** - Vollständige Anleitung auf Deutsch
- 📖 **EU_FEATURES.md** - Alle EU-Funktionen erklärt
- 📖 **README.md** - Aktualisiert mit EU-Fokus
- 📖 **API_REFERENCE.md** - API-Dokumentation mit EU-Endpunkten

### 📁 Dateistruktur

```
/workspace/
├── custom_components/ioniq5_2025/    # Integration
│   ├── manifest.json                 # "Europa Edition"
│   ├── strings.json                  # Deutsche UI-Texte
│   ├── translations/de.json          # Vollständige deutsche Übersetzung
│   ├── const.py                      # EU-optimierte Standardwerte
│   ├── config_flow.py               # EU vorausgewählt
│   └── ... (weitere Dateien)
│
├── EU_SETUP_GUIDE.md                 # 🇦🇹 Hauptanleitung auf Deutsch
├── EU_FEATURES.md                    # EU-spezifische Funktionen
├── EU_VERSION_SUMMARY.md             # Diese Datei
├── README.md                         # Aktualisiert mit EU-Fokus
├── API_REFERENCE.md                  # API-Endpunkte inkl. Europa
├── INSTALLATION.md                   # Installationsanleitung
├── QUICKSTART.md                     # Schnellstart
├── CHANGELOG.md                      # Versionshistorie
└── hacs.json                         # HACS-Konfiguration
```

### 🚀 Schnellstart für österreichische Benutzer

#### Schritt 1: Voraussetzungen ✅
1. Besuchen Sie **https://www.hyundai.com/de** (oder .at)
2. Melden Sie sich mit Bluelink-Daten an
3. **Akzeptieren Sie die Einwilligung zur Datenverarbeitung**
4. Warten Sie 5-10 Minuten

#### Schritt 2: Installation
**Via HACS (empfohlen):**
1. HACS → Integrationen → ⋮ → Benutzerdefinierte Repositories
2. Repository: `https://github.com/your_username/ioniq5_2025`
3. Kategorie: Integration
4. Herunterladen & Home Assistant neu starten

#### Schritt 3: Konfiguration
1. Einstellungen → Geräte & Dienste → + Integration hinzufügen
2. "Hyundai Ioniq 5" suchen
3. Eingeben:
   - E-Mail: Ihre Bluelink-Adresse
   - Passwort: Ihr Bluelink-Passwort
   - Region: **Europa** ✅ (vorausgewählt)
   - Marke: **Hyundai** ✅ (vorausgewählt)
   - PIN: Leer lassen
4. Fertig! 🎉

### 🔑 Wichtigste Änderungen vs. Original

| Feature | Original kia_uvo | EU Edition ioniq5_2025 |
|---------|------------------|------------------------|
| Domain | `kia_uvo` | `ioniq5_2025` |
| Region-Standard | Keine | **Europa** vorausgewählt |
| Marke-Standard | Keine | **Hyundai** vorausgewählt |
| UI-Sprache | Englisch | **Deutsch** + Englisch |
| API-Version | 3.48.0 | **3.48.1** (neueste) |
| Force-Refresh | 1440 Min (24h) | **240 Min (4h)** |
| Ruhezeit | 22:00-07:00 | **23:00-06:00** (AT Zeit) |
| Geolokalisierung | Aus | **An** (OpenStreetMap) |
| Integration Name | Generic | **Europa Edition** |
| Dokumentation | Englisch | **Deutsch** + Englisch |

### 📊 Verfügbare Entitäten (Auswahl)

#### Batterie & Laden
- `sensor.ioniq5_ev_batterie` → Batteriestand (%)
- `sensor.ioniq5_reichweite` → Reichweite (km)
- `sensor.ioniq5_ladeleistung` → Ladeleistung (kW)
- `binary_sensor.ioniq5_ladevorgang` → Lädt (ja/nein)

#### Steuerung
- `lock.ioniq5_tuerschloss` → Türen
- `climate.ioniq5_klima` → Klimatisierung
- `number.ioniq5_v2l_limit` → V2L Limit

#### Services (Actions)
- `ioniq5_2025.start_charge` → Laden starten
- `ioniq5_2025.start_climate` → Klimatisierung
- `ioniq5_2025.set_windows` → Fenster steuern ⭐
- `ioniq5_2025.start_valet_mode` → Valet-Modus ⭐

⭐ = Exklusiv für EU 2023+ (inkl. Ihr Ioniq 5 2025)

### 🇦🇹 Österreich-spezifische Features

#### PV-Überschuss-Laden
```yaml
# Automatisch laden wenn PV-Überschuss vorhanden
automation:
  - alias: "PV-Überschuss Laden"
    trigger:
      platform: numeric_state
      entity_id: sensor.pv_ueberschuss
      above: 3000  # 3kW
    action:
      service: ioniq5_2025.start_charge
```

#### Strompreis-Optimierung (aWATTar)
```yaml
# Laden wenn Strom günstig ist
automation:
  - alias: "Günstig laden"
    trigger:
      platform: numeric_state
      entity_id: sensor.awattar_preis
      below: 0.15  # Unter 15 Cent/kWh
    action:
      service: ioniq5_2025.start_charge
```

#### Winter-Vorheizen
```yaml
# Automatisch vorheizen im Winter
automation:
  - alias: "Winter Vorheizen"
    trigger:
      platform: time
      at: "07:00:00"
    condition:
      condition: numeric_state
      entity_id: sensor.aussentemperatur
      below: 5
    action:
      service: ioniq5_2025.start_climate
      data:
        temperature: 21
        defrost: true
        heating: true
```

### 🌐 EU API-Endpunkte

**Basis-URL für Österreich:**
```
https://prd.eu-ccapi.hyundai.com:8080
```

**Wichtigste Endpunkte:**
- User API: `/api/v1/user/`
- Vehicle API v1: `/api/v1/spa/`
- Vehicle API v2: `/api/v2/spa/` (erweiterte Funktionen)
- CCS2: `/api/v2/spa/vehicles/{id}/ccs2/` (EU 2023+)

### ⚠️ Wichtige Hinweise für EU-Nutzer

#### 1. **EU Einwilligung erforderlich!**
Ohne Einwilligung bei www.hyundai.com schlägt die Authentifizierung fehl!

#### 2. **API Rate Limits**
- ❌ Nicht jede Minute `force_update` aufrufen
- ✅ Max. alle 4 Stunden (Standard-Einstellung)
- ✅ Gecachte Updates beliebig oft

#### 3. **12V-Batterie schonen**
- Ruhezeit nutzen (23:00-06:00 Uhr)
- Nicht zu häufige Force-Updates
- Auto regelmäßig fahren

#### 4. **DSGVO-Konformität**
- ✅ Datenverarbeitung in EU
- ✅ Einwilligung erforderlich
- ✅ Lokale Speicherung in Home Assistant
- ✅ OpenStreetMap (EU-konform)

### 📚 Dokumentation

| Dokument | Beschreibung | Sprache |
|----------|--------------|---------|
| **EU_SETUP_GUIDE.md** | Vollständige Installationsanleitung | 🇩🇪 Deutsch |
| **EU_FEATURES.md** | Alle EU-spezifischen Funktionen | 🇩🇪 Deutsch |
| **README.md** | Hauptdokumentation (EU-Fokus) | 🇬🇧 Englisch |
| **INSTALLATION.md** | Detaillierte Installation | 🇬🇧 Englisch |
| **QUICKSTART.md** | 5-Minuten Schnellstart | 🇬🇧 Englisch |
| **API_REFERENCE.md** | API-Dokumentation | 🇬🇧 Englisch |

### 🆘 Support & Hilfe

**Bei Problemen:**
1. 📖 Lesen Sie **EU_SETUP_GUIDE.md** (auf Deutsch)
2. 🔍 Prüfen Sie [EU Login Flow](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api/wiki/Kia-Europe-Login-Flow)
3. 🐛 Erstellen Sie ein [GitHub Issue](https://github.com/your_username/ioniq5_2025/issues)
4. 💬 Fragen Sie in der [HA Community (Deutsch)](https://community.home-assistant.io/)

**Häufigste Probleme:**
- **Authentifizierung fehlgeschlagen** → EU Einwilligung bei www.hyundai.com
- **Keine Entitäten** → 2-3 Minuten warten, dann `force_update`
- **Integration nicht sichtbar** → Home Assistant neu starten, Cache leeren

### ✅ Checkliste vor der Verwendung

- [ ] Hyundai.com besucht und Einwilligung erteilt
- [ ] 5-10 Minuten gewartet
- [ ] Home Assistant 2024.1.0+ installiert
- [ ] Ioniq 5 in Bluelink App sichtbar
- [ ] Integration über HACS oder manuell installiert
- [ ] Home Assistant neu gestartet
- [ ] Integration konfiguriert (Region: Europa)
- [ ] Entitäten erschienen (2-3 Min warten)

### 🎉 Fertig!

Ihre Integration ist jetzt vollständig für Österreich/Europa optimiert und einsatzbereit!

**Genießen Sie die intelligente Steuerung Ihres Ioniq 5 2025!** ⚡🚗

---

**Version:** 1.0.0-eu  
**Optimiert für:** 🇦🇹 Österreich, 🇩🇪 Deutschland, 🇨🇭 Schweiz, 🇪🇺 EU  
**Ioniq 5 Modell:** 2025 (EU-Version)  
**API:** Hyundai Bluelink Europa (v3.48.1)
