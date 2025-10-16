# Hyundai Bluelink API Reference

This document lists the official Hyundai Bluelink API endpoints used by the integration, organized by region.

## 🌍 API Endpoints by Region

### 🇺🇸 United States (USA)
**Base URL:** `https://api.telematics.hyundaiusa.com`

- **Login API:** `https://api.telematics.hyundaiusa.com/v2/ac/`
- **Main API:** `https://api.telematics.hyundaiusa.com/ac/v2/`

**Example Endpoints:**
- Vehicle Status: `/rcs/rvs/vehicleStatus`
- Start Climate: `/evc/fatc/start` (EV) or `/rcs/rsc/start` (ICE)
- Lock/Unlock: `/rcs/rdo/on` or `/rcs/rdo/off`
- Start Charge: `/evc/charge/start`
- Find My Car: `/rcs/rfc/findMyCar`

---

### 🇪🇺 Europe (EU)

#### Hyundai Europe
**Base URL:** `https://prd.eu-ccapi.hyundai.com:8080`

- **User API:** `https://prd.eu-ccapi.hyundai.com:8080/api/v1/user/`
- **Vehicle API (v1):** `https://prd.eu-ccapi.hyundai.com:8080/api/v1/spa/`
- **Vehicle API (v2):** `https://prd.eu-ccapi.hyundai.com:8080/api/v2/spa/`
- **Login Portal:** `https://idpconnect-eu.hyundai.com`

#### Kia Europe
**Base URL:** `https://prd.eu-ccapi.kia.com:8080`

- **User API:** `https://prd.eu-ccapi.kia.com:8080/api/v1/user/`
- **Vehicle API (v1):** `https://prd.eu-ccapi.kia.com:8080/api/v1/spa/`
- **Vehicle API (v2):** `https://prd.eu-ccapi.kia.com:8080/api/v2/spa/`

**Example Endpoints:**
- Get Vehicles: `/api/v1/spa/vehicles`
- Vehicle Status: `/api/v1/spa/vehicles/{vehicle_id}/status`
- Location: `/api/v1/spa/vehicles/{vehicle_id}/location`
- Lock/Unlock: `/api/v1/spa/vehicles/{vehicle_id}/control/door`
- Climate Control: `/api/v1/spa/vehicles/{vehicle_id}/control/temperature`
- Start/Stop Charge: `/api/v2/spa/vehicles/{vehicle_id}/ccs2/control/charge`
- Charge Port: `/api/v2/spa/vehicles/{vehicle_id}/control/portdoor`
- Windows: `/api/v2/spa/vehicles/{vehicle_id}/control/windowcurtain`
- Valet Mode: `/api/v2/spa/vehicles/{vehicle_id}/control/valet`

---

### 🇨🇦 Canada

#### Hyundai Canada
**Base URL:** `https://mybluelink.ca`

- **API:** `https://mybluelink.ca/tods/api/`

#### Kia Canada
**Base URL:** `https://kiaconnect.ca`

- **API:** `https://kiaconnect.ca/tods/api/`

**Example Endpoints:**
- Login: `/v2/login`
- Vehicle List: `/vhcllst`
- Vehicle Status: `/lstvhclsts`
- Real-time Status: `/rltmvhclsts`
- Lock: `/drlck`
- Unlock: `/drulck`
- Start Climate (EV): `/evc/rfon`
- Stop Climate (EV): `/evc/rfoff`
- Start Charge: `/evc/rcstrt`
- Set Charge Limits: `/evc/setsoc`

---

### 🇦🇺 Australia

#### Hyundai Australia
**Base URL:** `https://au-apigw.ccs.hyundai.com.au:8080`

- **User API:** `https://au-apigw.ccs.hyundai.com.au:8080/api/v1/user/`
- **Vehicle API (v1):** `https://au-apigw.ccs.hyundai.com.au:8080/api/v1/spa/`
- **Vehicle API (v2):** `https://au-apigw.ccs.hyundai.com.au:8080/api/v2/spa/`

#### Kia Australia
**Base URL:** `https://au-apigw.ccs.kia.com.au:8082`

Similar endpoint structure to Hyundai AU.

---

### 🇧🇷 Brazil

#### Hyundai Brazil
**Base URL:** `https://br-ccapi.hyundai.com.br`

- **API:** `https://br-ccapi.hyundai.com.br/api/v1/`
- **Login/OAuth:** `https://br-ccapi.hyundai.com.br/web/v1/user/signin`

**Example Endpoints:**
- OAuth Authorize: `/user/oauth2/authorize`
- Sign In: `/user/signin`
- Get Token: `/user/oauth2/token`
- Vehicles: `/spa/vehicles`
- Vehicle Details: `/spa/vehicles/{vehicle_id}`
- Location: `/spa/vehicles/{vehicle_id}/location/park`
- Trip Info: `/spa/vehicles/{vehicle_id}/tripinfo`

---

### 🇨🇳 China
**Base URL:** Varies by provider (e.g., `prd.cn-ccapi.hyundai.com`)

- **User API:** `/api/v1/user/`
- **Vehicle API:** `/api/v1/spa/` and `/api/v2/spa/`

---

### 🇮🇳 India
**Base URL:** `prd.in-ccapi.kia.com:8080` (Kia)

- **User API:** `https://prd.in-ccapi.kia.com:8080/api/v1/user/`
- **Vehicle API (v1):** `https://prd.in-ccapi.kia.com:8080/api/v1/spa/`
- **Vehicle API (v2):** `https://prd.in-ccapi.kia.com:8080/api/v2/spa/`

---

## 📡 Common API Patterns

### Authentication Flow
1. **Login** → Get access token
2. **OAuth Token Exchange** → Get refresh token
3. **Token Refresh** → Maintain session

### Vehicle Operations
All regional APIs follow similar patterns:

```
GET  /vehicles                          # List vehicles
GET  /vehicles/{id}/status              # Get status
GET  /vehicles/{id}/location            # Get location
POST /vehicles/{id}/control/door        # Lock/unlock
POST /vehicles/{id}/control/temperature # Climate
POST /vehicles/{id}/control/charge      # Charging
```

### API Versions
- **v1 API** (`/api/v1/spa/`): Legacy endpoints
- **v2 API** (`/api/v2/spa/`): Newer features (windows, valet, enhanced charging)
- **CCS2** (`/ccs2/`): Combined Charging System endpoints (EU 2023+)

## 🔐 Authentication Headers

### USA (Hyundai)
```http
Host: api.telematics.hyundaiusa.com
Content-Type: application/json
```

### Europe (Hyundai/Kia)
```http
Host: prd.eu-ccapi.hyundai.com:8080
Authorization: Bearer {access_token}
ccsp-service-id: {service_id}
ccsp-application-id: {app_id}
Stamp: {timestamp}
Content-Type: application/json
```

### Canada
```http
Host: mybluelink.ca
Authorization: Bearer {access_token}
Content-Type: application/json
```

## 📝 Important Notes

### Rate Limits
- **Force refresh**: Limit to once every 4+ hours
- **Cached updates**: Can be more frequent (30 min default)
- Excessive requests may result in temporary blocking

### Regional Differences
- **USA**: Limited advanced features (no window control, valet mode)
- **EU (2023+)**: Most features including windows, valet, V2L
- **Canada**: Full feature set, requires PIN
- **Australia/NZ**: Most features, some in testing

### Vehicle-to-Load (V2L)
Available in newer EVs (Ioniq 5, EV6, etc.):
```
POST /vehicles/{id}/ccs2/charge/dischargelimit
```

### Trip Information
Available in some regions:
```
GET /vehicles/{id}/tripinfo?yyyymm={period}
GET /vehicles/{id}/drvhistory?yyyymmdd={date}
```

## 🔗 Related Resources

- **API Library:** [hyundai_kia_connect_api](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api)
- **Home Assistant Integration:** [kia_uvo](https://github.com/Hyundai-Kia-Connect/kia_uvo)
- **EU Login Guide:** [Wiki](https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api/wiki/Kia-Europe-Login-Flow)
- **Bluelinky (Node.js):** [Reference Implementation](https://github.com/Hacksore/bluelinky)

## ⚠️ Disclaimer

These are unofficial API endpoints discovered through reverse engineering. Use responsibly and respect rate limits to avoid account issues.

---

**For Ioniq 5 2025 specifically:** Your vehicle will use the Hyundai endpoints for your region. Most regions support the full feature set including V2L, climate control, and charging management.
