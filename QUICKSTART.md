# Quick Start Guide - Hyundai Ioniq 5 (2025)

Get your Ioniq 5 connected to Home Assistant in 5 minutes! ⚡

## Prerequisites ✓

- [ ] Home Assistant 2024.1.0+ installed
- [ ] Hyundai Bluelink account with Ioniq 5 2025 registered
- [ ] Bluelink username, password, and PIN (if in Canada)

## Installation (Choose One)

### Option A: HACS (Easiest) 🌟

1. **Open HACS** → **Integrations**
2. Click **⋮** (top right) → **Custom repositories**
3. Add: `https://github.com/your_username/ioniq5_2025`
4. Category: **Integration**
5. Search "**Ioniq 5**" → **Download**
6. **Restart Home Assistant**

### Option B: Manual 📦

1. Download this repository
2. Copy `custom_components/ioniq5_2025/` to:
   ```
   <HA config>/custom_components/ioniq5_2025/
   ```
3. **Restart Home Assistant**

## Setup ⚙️

1. **Settings** → **Devices & Services** → **+ Add Integration**
2. Search: "**Hyundai Ioniq 5**"
3. Enter your credentials:
   - **Username**: Your Bluelink email
   - **Password**: Your Bluelink password
   - **Region**: Your location
   - **Brand**: Hyundai (pre-selected)
   - **PIN**: If required (Canada: yes, others: optional)
4. Click **Submit** and wait 30-60 seconds
5. ✅ Done!

## What You Get

Your Ioniq 5 will appear with these entities:

### 📊 Main Sensors
- `sensor.ioniq5_ev_battery_level` - Battery %
- `sensor.ioniq5_ev_range` - Driving range
- `device_tracker.ioniq5_location` - GPS location
- `binary_sensor.ioniq5_charging_status` - Charging yes/no

### 🎛️ Controls
- `lock.ioniq5_door_lock` - Lock/unlock doors
- `climate.ioniq5_climate` - Climate control
- Services for charging, climate, etc.

## First Actions to Try

### 1. Update Vehicle Data
**Developer Tools** → **Actions**
```yaml
service: ioniq5_2025.update
```

### 2. Check Battery Level
Look for: `sensor.ioniq5_ev_battery_level`

### 3. Lock Your Car
```yaml
service: lock.lock
target:
  entity_id: lock.ioniq5_door_lock
```

## Quick Automations

### Charge at Night (Cheap Electricity)
```yaml
automation:
  - alias: "Charge Ioniq 5 at 2 AM"
    trigger:
      platform: time
      at: "02:00:00"
    action:
      service: ioniq5_2025.start_charge
      target:
        device_id: YOUR_DEVICE_ID
```

### Low Battery Alert
```yaml
automation:
  - alias: "Ioniq 5 Low Battery"
    trigger:
      platform: numeric_state
      entity_id: sensor.ioniq5_ev_battery_level
      below: 20
    action:
      service: notify.mobile_app
      data:
        message: "Ioniq 5 battery low: {{ states('sensor.ioniq5_ev_battery_level') }}%"
```

### Pre-heat Before Work
```yaml
automation:
  - alias: "Warm Ioniq 5 Before Work"
    trigger:
      platform: time
      at: "07:30:00"
    condition:
      condition: state
      entity_id: binary_sensor.workday
      state: 'on'
    action:
      service: ioniq5_2025.start_climate
      target:
        device_id: YOUR_DEVICE_ID
```

## Optional: Configure Advanced Settings

**Integrations** → **Hyundai Ioniq 5** → **Configure**

- **Update interval**: 30 min (how often to check)
- **Force refresh**: 240 min (how often to wake car)
- **Quiet hours**: 22:00-07:00 (don't wake car)
- **Geolocation**: Enable for address lookup

## Troubleshooting 🔧

### Can't find integration?
- Did you restart HA after install?
- Clear browser cache (Ctrl+F5)

### Authentication failed?
- Check credentials in Bluelink app
- EU users: Visit hyundai.com and accept consent
- Wait 5 min and retry (rate limit)

### No entities appearing?
- Wait 2-3 minutes
- Call `ioniq5_2025.force_update` service
- Check HA logs for errors

### Enable debug logging:
Integration page → **Enable debug logging**

## Next Steps 🚀

1. ✅ Add car entities to your dashboard
2. ✅ Create more automations (see [README.md](README.md))
3. ✅ Join the community for support
4. ✅ Share your setup!

## Need Help? 💡

- 📖 Full docs: [README.md](README.md)
- 🔧 Install guide: [INSTALLATION.md](INSTALLATION.md)
- 🐛 Issues: Create a GitHub issue
- 💬 Community: Join Discord

---

**Enjoy your smart Ioniq 5!** 🎉
