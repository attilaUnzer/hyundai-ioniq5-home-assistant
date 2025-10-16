# Hyundai Ioniq 5 (2025) - Home Assistant Integration
## 🇪🇺 Optimiert für Europa / Österreich

Eine Home Assistant Custom Integration, speziell für den **Hyundai Ioniq 5 2025** entwickelt. Diese Integration verbindet Ihren Ioniq 5 über Hyundai Bluelink mit Home Assistant.

> **🇦🇹 Für österreichische Benutzer:** Diese Integration ist vollständig auf Europa/Österreich optimiert mit deutschen Übersetzungen, EU API-Endpunkten und voreingestellten Werten für den europäischen Markt. Siehe [EU Setup Guide](EU_SETUP_GUIDE.md) für detaillierte Anweisungen auf Deutsch.

> **Note:** Based on [Hyundai-Kia-Connect/kia_uvo](https://github.com/Hyundai-Kia-Connect/kia_uvo) and customized for Ioniq 5 2025 with EU focus.

## ✨ Features

### 🚗 Vehicle Information
- **Battery Status**: EV battery level, remaining range, and charging status
- **Location Tracking**: GPS coordinates and optional geocoded address
- **Odometer**: Current mileage
- **Door/Window Status**: Real-time status of all doors, windows, trunk, and hood
- **Lock Status**: Monitor and control vehicle locks
- **Tire Pressure**: Individual tire pressure warnings
- **12V Battery**: Monitor auxiliary battery level

### ⚡ Charging Control
- **Start/Stop Charging**: Remotely control charging sessions
- **Charge Limits**: Set AC and DC charge limits
- **Charging Current**: Adjust charging current (100%, 90%, 60%)
- **Charge Port**: Open/close charge port (region dependent)
- **Charging Power**: Monitor current charging power

### 🌡️ Climate Control
- **Remote Climate**: Start/stop climate control remotely
- **Temperature Settings**: View and adjust climate temperature
- **Defrost Control**: Monitor defrost status
- **Scheduled Climate**: Plan departure with pre-conditioning

### 🔧 Advanced Features (Region Dependent)
- **V2L (Vehicle to Load)**: Control discharge limits for using your car as a power source
- **Valet Mode**: Enable/disable valet mode
- **Window Control**: Open/close windows remotely (EU post-2023, NZ, AU)
- **Hazard Lights**: Activate emergency signals
- **Geolocation**: Optional reverse geocoding for address lookup

## 📋 Requirements

- Home Assistant 2024.1.0 or newer
- Active Hyundai Bluelink account with your Ioniq 5 registered
- **For EU users:** Data processing consent at www.hyundai.com required before setup
- Internet connection for cloud communication

### 🇪🇺 European Users - Important!
Before configuring this integration:
1. Visit **https://www.hyundai.com** (or your country's Hyundai site)
2. Sign in with your Bluelink credentials
3. Accept the **data processing consent**
4. Wait 5-10 minutes before proceeding with Home Assistant setup

**Why?** This is required due to EU GDPR regulations. Without consent, authentication will fail.

📖 **Detailed EU Guide:** [EU_SETUP_GUIDE.md](EU_SETUP_GUIDE.md) (German/English)

## 🚀 Installation

### Method 1: HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to **Integrations**
3. Click the **three dots** in the top right corner
4. Select **Custom repositories**
5. Add this repository URL: `https://github.com/your_username/ioniq5_2025`
6. Select **Integration** as the category
7. Click **Install**
8. Restart Home Assistant

### Method 2: Manual Installation

1. Download this repository
2. Copy the `custom_components/ioniq5_2025` folder to your Home Assistant's `custom_components` directory:
   ```
   <config_dir>/custom_components/ioniq5_2025/
   ```
3. Restart Home Assistant

## ⚙️ Configuration

### Initial Setup

1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration**
3. Search for **Hyundai Ioniq 5 (2025)**
4. Enter your Bluelink credentials:
   - **Username/Email**: Your Bluelink account email
   - **Password**: Your Bluelink password
   - **Region**: Select your region (Europe, USA, Canada, etc.)
   - **Brand**: Pre-selected as Hyundai
   - **PIN**: Required for Canada, optional for other regions

### 🇪🇺 EU/Austrian Users

The integration is **pre-configured for Europe**:
- ✅ Region defaults to **Europe**
- ✅ Brand defaults to **Hyundai**
- ✅ German language interface available
- ✅ Geolocation enabled (OpenStreetMap)
- ✅ Optimal update intervals for EU

**Setup Credentials:**
- **Region**: Europe (pre-selected)
- **Brand**: Hyundai (pre-selected)
- **PIN**: Leave empty (not required in EU)

📖 **Ausführliche Anleitung auf Deutsch:** [EU_SETUP_GUIDE.md](EU_SETUP_GUIDE.md)

For detailed EU login flow: [EU Login Guide](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api/wiki/Kia-Europe-Login-Flow)

### Advanced Options

After setup, click **Configure** on the integration to adjust:

#### Recommended Settings for Europe/Austria:
- **Update Interval**: 30 minutes (default) - How often to fetch cached data
- **Force Refresh Interval**: 240 minutes / 4 hours (default) - How often to wake the vehicle for fresh data
- **No Force Refresh Hours**: 23:00 - 06:00 (default for Austrian timezone) - Quiet hours to preserve 12V battery
- **Enable Geolocation**: ✅ Enabled (default) - Shows address instead of GPS coordinates using OpenStreetMap
- **Use Email for Geocode**: ❌ Disabled (default) - Not needed for OpenStreetMap

**Why these defaults?**
- 4-hour force refresh protects your vehicle's 12V battery
- Quiet hours prevent night-time vehicle wake-ups
- OpenStreetMap provides free, accurate geocoding in Austria/EU

## 📊 Supported Entities

### Sensors
- EV Battery Level (%)
- EV Battery Range (km/mi)
- 12V Battery Level (%)
- Odometer (km/mi)
- Charging Power (kW)
- Tire Pressure Warnings
- Last Update Timestamp

### Binary Sensors
- Charging Status
- Plugged In Status
- Engine Status
- Door Status (individual doors)
- Window Status
- Hood Status
- Trunk Status
- Low Fuel Light (for PHEV)

### Device Tracker
- Vehicle Location (GPS coordinates)
- Geocoded Address (optional)

### Lock
- Vehicle Door Lock/Unlock

### Climate
- Climate Control
- Set Temperature
- Defrost Status

### Number
- V2L Discharge Limit

## 🎯 Services

Access these services via **Developer Tools** → **Actions** or use in automations:

| Service | Description | Availability |
|---------|-------------|--------------|
| `update` | Get latest cached vehicle data | All regions |
| `force_update` | Request fresh data from vehicle | Most regions |
| `start_climate` | Start climate control | All regions |
| `stop_climate` | Stop climate control | All regions |
| `start_charge` | Start charging | EV/PHEV |
| `stop_charge` | Stop charging | EV/PHEV |
| `set_charge_limits` | Set AC/DC charge limits | EV/PHEV |
| `set_charging_current` | Set charging current level | EV/PHEV |
| `lock` | Lock vehicle | All regions |
| `unlock` | Unlock vehicle | All regions |
| `open_charge_port` | Open charge port | Select regions |
| `close_charge_port` | Close charge port | Select regions |
| `set_windows` | Control windows | EU (>2023), NZ, AU |
| `start_hazard_lights` | Activate hazard lights | Select regions |
| `start_hazard_lights_and_horn` | Panic mode | Select regions |
| `schedule_charging_and_climate` | Plan departure | Select regions |
| `start_valet_mode` | Enable valet mode | Select regions |
| `stop_valet_mode` | Disable valet mode | Select regions |

## 🌍 Regional Support

| Region | Update | Force Update | Climate | Charging | Advanced Features | Notes |
|--------|--------|--------------|---------|----------|-------------------|-------|
| **🇪🇺 Europe** | ✅ | ✅ | ✅ | ✅ | ⭐ All features | **Default & Optimized** |
| **🇦🇹 Austria** | ✅ | ✅ | ✅ | ✅ | ⭐ All features | German UI, EU defaults |
| **EU (2023+)** | ✅ | ✅ | ✅ | ✅ | ⭐ All + Windows, Valet | Ioniq 5 2025 included |
| **🇺🇸 USA** | ✅ | ✅ | ✅ | ✅ | Basic features | Limited advanced features |
| **🇨🇦 Canada** | ✅ | ✅ | ✅ | ✅ | Most features | PIN required |
| **🇦🇺 Australia** | ✅ | ✅ | ✅ | ✅ | Most features | Select features |
| **🇳🇿 New Zealand** | ✅ | ✅ | ✅ | ✅ | Most features | Select features |

**This integration is optimized for European/Austrian Ioniq 5 2025 owners** with all features including:
- ✅ Window control
- ✅ Valet mode  
- ✅ V2L (Vehicle-to-Load)
- ✅ Enhanced charging controls
- ✅ Trip information

## 📱 Example Automations

### Charge when electricity is cheap
```yaml
automation:
  - alias: "Start Ioniq 5 Charging at Night"
    trigger:
      - platform: time
        at: "02:00:00"
    condition:
      - condition: numeric_state
        entity_id: sensor.ioniq5_ev_battery_level
        below: 80
    action:
      - service: ioniq5_2025.start_charge
        target:
          device_id: YOUR_DEVICE_ID
```

### Pre-condition before leaving
```yaml
automation:
  - alias: "Warm up Ioniq 5 before work"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: state
        entity_id: binary_sensor.workday
        state: 'on'
    action:
      - service: ioniq5_2025.start_climate
        data:
          climate_options:
            set_temp: 22
            defrost: true
        target:
          device_id: YOUR_DEVICE_ID
```

### Alert on low battery
```yaml
automation:
  - alias: "Ioniq 5 Low Battery Alert"
    trigger:
      - platform: numeric_state
        entity_id: sensor.ioniq5_ev_battery_level
        below: 20
    action:
      - service: notify.mobile_app
        data:
          message: "Ioniq 5 battery is below 20%"
```

## 🔧 Troubleshooting

### 🇪🇺 EU Users: Authentication Failed
**Most common issue for European users!**

**Solution:**
1. Visit **https://www.hyundai.com/de** (or your country)
2. Sign in with Bluelink credentials
3. Accept **data processing consent**
4. Wait 10 minutes
5. Try Home Assistant setup again

If still failing:
- Reset password in Bluelink app
- Ensure Ioniq 5 is visible in Bluelink app
- Check [EU Login Flow Guide](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api/wiki/Kia-Europe-Login-Flow)

### Integration not showing up
- Ensure you've restarted Home Assistant after installation
- Check that the folder is correctly placed in `custom_components/`
- Clear browser cache (Ctrl+F5)
- Verify Home Assistant logs for errors

### Other Authentication errors
1. Double-check your Bluelink credentials
2. Ensure your Ioniq 5 is registered in your Bluelink account
3. Try creating a new Bluelink account and sharing your vehicle to it

### Connection issues
- Verify your Ioniq 5 has cellular connectivity
- Check if you can access the vehicle via the Bluelink mobile app
- Enable debug logging to investigate further

### Enable Debug Logging
1. Go to **Settings** → **Devices & Services**
2. Click on the Ioniq 5 integration
3. Click **Enable debug logging**
4. Reproduce the issue
5. Click **Download diagnostics**
6. Check logs in **Settings** → **System** → **Logs**

## ⚠️ API Rate Limits

Be mindful of API rate limits to avoid being blocked:
- **Force updates**: Use sparingly (recommended: 4+ hours apart)
- **Climate/Charging actions**: Allow time between commands
- **Quiet hours**: Configure to avoid unnecessary vehicle wake-ups

## 🙏 Credits

- Original integration: [Hyundai-Kia-Connect/kia_uvo](https://github.com/Hyundai-Kia-Connect/kia_uvo) by [@fuatakgun](https://github.com/fuatakgun)
- API library: [hyundai_kia_connect_api](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api)
- Inspired by: [bluelinky](https://github.com/Hacksore/bluelinky)

## 📄 License

This project inherits the license from the original kia_uvo integration. Please see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your_username/ioniq5_2025/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your_username/ioniq5_2025/discussions)
- **Original Project**: [kia_uvo Discord](https://discord.gg/HwnG8sY)

## 🔮 Roadmap

- [ ] Add more Ioniq 5 2025-specific features
- [ ] Improve region-specific functionality
- [ ] Add more example automations
- [ ] Enhanced dashboard cards
- [ ] Support for 2025 model year updates

---

**Note**: This is a third-party integration and is not officially endorsed by Hyundai. Use at your own risk.
