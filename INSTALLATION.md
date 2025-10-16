# Installation Guide - Hyundai Ioniq 5 (2025)

## Quick Start

This guide will help you install and configure the Hyundai Ioniq 5 (2025) integration for Home Assistant.

## Prerequisites

Before you begin, ensure you have:

1. ✅ **Home Assistant 2024.1.0 or newer**
2. ✅ **Active Hyundai Bluelink account** with your Ioniq 5 2025 registered
3. ✅ **Your Bluelink login credentials** (email and password)
4. ✅ **PIN code** (if you're in Canada or have set one up)
5. ✅ **Working internet connection** on your Home Assistant instance

## Installation Methods

### Method 1: HACS (Recommended) 🌟

HACS (Home Assistant Community Store) is the easiest way to install and keep this integration updated.

#### Step 1: Install HACS
If you don't have HACS installed:
1. Visit [HACS Installation Guide](https://hacs.xyz/docs/setup/download)
2. Follow the installation steps
3. Restart Home Assistant

#### Step 2: Add Custom Repository
1. Open Home Assistant
2. Go to **HACS** in the sidebar
3. Click on **Integrations**
4. Click the **three dots** (⋮) in the top right corner
5. Select **Custom repositories**
6. Add the following:
   - **Repository**: `https://github.com/your_username/ioniq5_2025`
   - **Category**: `Integration`
7. Click **Add**

#### Step 3: Install Integration
1. Search for "Hyundai Ioniq 5 (2025)" in HACS
2. Click on it
3. Click **Download**
4. Restart Home Assistant

### Method 2: Manual Installation 🔧

For advanced users who prefer manual installation:

#### Step 1: Download Files
1. Download the latest release from GitHub
2. Extract the ZIP file

#### Step 2: Copy Files
1. Navigate to your Home Assistant configuration directory
2. If it doesn't exist, create a `custom_components` folder
3. Copy the entire `ioniq5_2025` folder into `custom_components`:
   ```
   <config_dir>/
   ├── custom_components/
   │   └── ioniq5_2025/
   │       ├── __init__.py
   │       ├── manifest.json
   │       ├── ... (other files)
   ```

#### Step 3: Restart
1. Restart Home Assistant
2. Wait for it to fully start up

## Configuration

### Step 1: Add Integration

1. Go to **Settings** → **Devices & Services**
2. Click the **+ Add Integration** button (bottom right)
3. Search for "**Hyundai Ioniq 5 (2025)**"
4. Click on it to start configuration

### Step 2: Enter Credentials

You'll be prompted to enter:

| Field | Description | Example |
|-------|-------------|---------|
| **Username/Email** | Your Bluelink account email | `you@email.com` |
| **Password** | Your Bluelink password | `YourSecurePassword123` |
| **Region** | Your geographic region | `Europe`, `USA`, `Canada`, etc. |
| **Brand** | Vehicle brand (pre-selected) | `Hyundai` |
| **PIN** | 4-digit PIN (if required) | `1234` (required for Canada) |

### Step 3: Wait for Discovery

- The integration will connect to Hyundai Bluelink
- It will discover your Ioniq 5 2025
- This may take 30-60 seconds

### Step 4: Success! 🎉

Once configured, you'll see:
- A new device: **Hyundai Ioniq 5**
- Multiple entities for battery, location, sensors, etc.
- Available services for remote control

## Regional Considerations

### 🇪🇺 Europe (EU)

**Special Steps Required for Some Users:**

If you encounter login issues in Europe:

1. Visit https://www.hyundai.com/eu (or your country's site)
2. Log in with your Bluelink credentials
3. Accept the data processing consent
4. Then retry the Home Assistant integration setup

**Note**: For EU vehicles from 2023 onwards, more features are available including window control and valet mode.

**Detailed Guide**: [EU Login Flow](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api/wiki/Kia-Europe-Login-Flow)

### 🇺🇸 United States (USA)

- Select "USA" as your region
- PIN is optional
- Some advanced features may be limited

### 🇨🇦 Canada

- Select "Canada" as your region
- **PIN is required** - use your 4-digit Bluelink PIN
- Full feature support available

### 🇦🇺 Australia / 🇳🇿 New Zealand

- Select appropriate region
- Most features supported
- Some features in testing

## Advanced Configuration

### Customize Update Intervals

After initial setup, click **Configure** on the integration to adjust:

1. **Update Interval** (15-999 minutes, default: 30)
   - How often to check for cached updates
   - Lower = more frequent updates, higher API usage

2. **Force Refresh Interval** (90-9999 minutes, default: 240)
   - How often to wake the car for fresh data
   - ⚠️ Be conservative to preserve car's 12V battery

3. **Quiet Hours**
   - **Start Hour** (0-23, default: 22): When to stop force refreshes
   - **Finish Hour** (0-23, default: 7): When to resume force refreshes
   - Prevents waking the car during night

### Enable Geolocation

To show your car's address instead of just coordinates:

1. Click **Configure** on the integration
2. Enable **"Enable geolocation"**
3. Optionally enable **"Use email for geocode API"**
4. Click **Submit**

**Note**: Uses OpenStreetMap by default (free, no API key needed)

## Verify Installation

### Check Entities

Go to **Settings** → **Devices & Services** → **Hyundai Ioniq 5 (2025)**

You should see entities like:
- ✅ `sensor.ioniq5_ev_battery_level`
- ✅ `sensor.ioniq5_ev_range`
- ✅ `device_tracker.ioniq5_location`
- ✅ `lock.ioniq5_door_lock`
- ✅ `binary_sensor.ioniq5_charging_status`
- ✅ And many more...

### Test a Service

1. Go to **Developer Tools** → **Actions**
2. Select service: `ioniq5_2025.update`
3. Select your vehicle
4. Click **Call Service**
5. Check if data updates

## Troubleshooting

### ❌ Integration Not Appearing

**Problem**: Can't find "Hyundai Ioniq 5 (2025)" in the integration list

**Solutions**:
1. Ensure you've restarted Home Assistant after installation
2. Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
3. Check `custom_components/ioniq5_2025/` exists and has files
4. Check Home Assistant logs for errors

### ❌ Authentication Failed

**Problem**: "Invalid authentication credentials" error

**Solutions**:
1. Verify credentials work in the Bluelink mobile app
2. For EU: Complete the consent process on Hyundai website
3. Check if your PIN is correct (Canada users)
4. Try creating a second Bluelink account and share your vehicle to it
5. Wait 5-10 minutes and try again (rate limiting)

### ❌ No Entities Created

**Problem**: Integration added but no entities appear

**Solutions**:
1. Wait 2-3 minutes for initial data fetch
2. Check if your Ioniq 5 is properly registered in Bluelink
3. Try calling `ioniq5_2025.force_update` service
4. Enable debug logging (see below)

### ❌ "Config Not Ready" Error

**Problem**: Integration fails to start

**Solutions**:
1. Check internet connectivity
2. Verify Bluelink service is online (try mobile app)
3. Restart Home Assistant
4. Remove and re-add the integration

### 🔍 Enable Debug Logging

For detailed troubleshooting:

1. Go to integration page
2. Click **Enable debug logging**
3. Reproduce the issue
4. Click **Download diagnostics**
5. Review or share logs (remove sensitive info!)

Or add to `configuration.yaml`:
```yaml
logger:
  default: info
  logs:
    custom_components.ioniq5_2025: debug
    hyundai_kia_connect_api: debug
```

Then restart Home Assistant.

## Getting Help

If you're still having issues:

1. 📖 Check the [README](README.md) for detailed documentation
2. 🐛 Search [existing issues](https://github.com/your_username/ioniq5_2025/issues)
3. 💬 Join the [discussion forum](https://github.com/your_username/ioniq5_2025/discussions)
4. 🆕 Create a [new issue](https://github.com/your_username/ioniq5_2025/issues/new) with:
   - Home Assistant version
   - Region
   - Error messages
   - Debug logs (sanitized)

## Next Steps

Once installed and working:

1. 📊 **Create Dashboard Cards** - Add car entities to your Lovelace dashboard
2. 🤖 **Set Up Automations** - See [README](README.md#-example-automations) for examples
3. 📱 **Configure Notifications** - Get alerts for low battery, charging complete, etc.
4. 🎨 **Customize Entities** - Rename entities, set custom icons, etc.

---

**Welcome to the Ioniq 5 Home Assistant community!** 🎉
