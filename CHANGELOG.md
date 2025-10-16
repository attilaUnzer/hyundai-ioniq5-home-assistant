# Changelog

All notable changes to the Hyundai Ioniq 5 (2025) Home Assistant integration will be documented in this file.

## [1.0.0] - 2025-10-16

### 🎉 Initial Release

This is the first release of the Hyundai Ioniq 5 (2025) integration, forked and customized from the excellent [kia_uvo](https://github.com/Hyundai-Kia-Connect/kia_uvo) project.

### ✨ Features

#### Core Functionality
- **Vehicle Integration**: Full integration with Hyundai Bluelink for Ioniq 5 2025
- **Real-time Monitoring**: Battery level, range, location, and vehicle status
- **Remote Control**: Climate control, charging, and door locks
- **Multi-region Support**: Europe, USA, Canada, Australia, New Zealand, and more

#### Sensors
- EV Battery Level and Range
- 12V Battery Status
- Odometer
- Charging Power
- Tire Pressure Warnings
- Location Tracking with optional geocoding

#### Controls
- Lock/Unlock doors
- Start/Stop climate control
- Start/Stop charging
- Set charge limits (AC/DC)
- Adjust charging current
- V2L discharge control
- Open/Close charge port (region dependent)

#### Advanced Features (Region Dependent)
- Window control
- Valet mode
- Hazard lights and horn
- Scheduled charging and climate
- Trip information

### 🔧 Technical Updates

- Updated to `hyundai_kia_connect_api==3.48.1` (latest version)
- Pre-configured for Hyundai brand (Ioniq 5)
- Optimized configuration flow
- Enhanced user interface strings
- Comprehensive documentation

### 📚 Documentation

- Complete README with feature list and examples
- Detailed INSTALLATION guide
- Example automations
- Troubleshooting guide
- Regional compatibility matrix

### 🙏 Credits

Based on [Hyundai-Kia-Connect/kia_uvo](https://github.com/Hyundai-Kia-Connect/kia_uvo) v2.45.3
- Original author: [@fuatakgun](https://github.com/fuatakgun)
- API library: [hyundai_kia_connect_api](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api)

---

## Version History Format

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Types of Changes
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` in case of vulnerabilities
