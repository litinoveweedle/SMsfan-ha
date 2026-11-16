FULL_NAME = "Smart Fan"
LINK = "https://sequentmicrosystems.com/products/smart-fan-for-raspberry-pi"

from . import driver_adapter
API = driver_adapter
DOMAIN = "smsfan"
NAME_PREFIX = "smsf"
SM_MAP = {
    "sensor": {
        "processor_temp": {
            "chan_no": 1, "optional": True, "uom": "°C",
            "com": {"get": "getProcTemp"},
        },
    },
    "switch": {
        "led_blink": {
            "chan_no": 1, "optional": True,
            "com": {"get": "getLedBlink", "set": "setLedBlink"},
        },
    },
    "number": {
        "safety_temp": {
                "chan_no": 1, "optional": True, "uom": "°C",
                "min_value": 30, "max_value": 80, "step": 1,
                "com": {"get": "getSafetyTemp", "set": "setSafetyTemp"},
        },
        "power": {
                "chan_no": 1,
                "uom": "%",
                "min_value": 0.0,
                "max_value": 100.0,
                "step": 1.0,
                "com": {
                    "get": "getPower",
                    "set": "setPower"
                },
                "icon": {
                    "on": "mdi:fan",
                    "off": "mdi:fan-off"
                }
        },
    },
}
