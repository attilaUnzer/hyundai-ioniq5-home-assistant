"""Constants for the Hyundai Ioniq 5 (2025) integration."""

DOMAIN: str = "ioniq5_2025"

CONF_BRAND: str = "brand"
CONF_FORCE_REFRESH_INTERVAL: str = "force_refresh"
CONF_NO_FORCE_REFRESH_HOUR_START: str = "no_force_refresh_hour_start"
CONF_NO_FORCE_REFRESH_HOUR_FINISH: str = "no_force_refresh_hour_finish"
CONF_ENABLE_GEOLOCATION_ENTITY: str = "enable_geolocation_entity"
CONF_USE_EMAIL_WITH_GEOCODE_API: str = "use_email_with_geocode_api"

REGION_EUROPE: str = "Europe"
REGION_CANADA: str = "Canada"
REGION_USA: str = "USA"
REGION_CHINA: str = "China"
REGION_AUSTRALIA: str = "Australia"
REGION_INDIA: str = "India"
REGION_NZ: str = "New Zealand"
REGIONS = {
    1: REGION_EUROPE,
    2: REGION_CANADA,
    3: REGION_USA,
    4: REGION_CHINA,
    5: REGION_AUSTRALIA,
    6: REGION_INDIA,
    7: REGION_NZ,
}
BRAND_KIA: str = "Kia"
BRAND_HYUNDAI: str = "Hyundai"
BRAND_GENESIS: str = "Genesis"
BRANDS = {1: BRAND_KIA, 2: BRAND_HYUNDAI, 3: BRAND_GENESIS}

CHARGING_CURRENTS = {1: 100, 2: 90, 3: 60}

DEFAULT_PIN: str = ""
DEFAULT_SCAN_INTERVAL: int = 30
DEFAULT_FORCE_REFRESH_INTERVAL: int = 240  # 4 hours - recommended for EU to avoid excessive API calls
DEFAULT_NO_FORCE_REFRESH_HOUR_START: int = 23  # 11 PM in Austria
DEFAULT_NO_FORCE_REFRESH_HOUR_FINISH: int = 6  # 6 AM in Austria
DEFAULT_ENABLE_GEOLOCATION_ENTITY: bool = True  # Enable for EU users (OpenStreetMap)
DEFAULT_USE_EMAIL_WITH_GEOCODE_API: bool = False

DYNAMIC_UNIT: str = "dynamic_unit"
