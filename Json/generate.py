import json
import random
import os

pwd = os.getcwd()
output = os.path.join(pwd, 'Json', 'Json - Aircraft Maintaince.json')
# === EXTENDED SYSTEM DEFINITIONS ===
systems = {
    "landing_gear": {
        "replacement_name": "Landing Gear System",
        "keywords": [
            "undercarriage", "landing gear", "gear collapse", "gear-up landing", "tire failure",
            "brake failure", "strut failure", "retraction failure", "oleo failure", "wheel assembly",
            "shimmy", "axle crack", "drag brace", "uplock failure", "downlock sensor", "gear doors",
            "WOW sensor", "proximity sensor", "gear warning", "tire pressure", "anti-skid", "shock absorber",
            "scissor link", "torque link", "wheel well", "landing gear actuator", "bearing failure",
            "retraction motor", "landing gear truck", "wheel brake", "drag brace pin"
        ],
        "common_parts": [
            "MLG", "NLG", "STRUT", "ACTUATOR-GEAR", "SHOCK-ABSORB", "BRAKE-ASSY", "WHEEL",
            "TIRE", "HYDRAULIC-CYL", "TORQUE-LINK", "AXLE", "BEARING", "SHIMMY DAMPER",
            "UPLOCK", "DOWNLOCK", "TRUCK BEAM", "SCISSOR LINK", "GEAR DOOR", "WOW SWITCH",
            "PROXIMITY SENSOR", "BRAKE VALVE", "ANTI-SKID VALVE", "TIRE PRESSURE SENSOR",
            "RETRACTION MOTOR", "GEAR LOCK", "DRAG BRACE PIN", "WHEEL WELL COVER"
        ],
        "failure_modes": [
            "Structural collapse", "Hydraulic leakage", "Bearing seizure", "Tire blowout",
            "Brake overheating", "Shimmy vibration", "Corrosion", "Fatigue cracking",
            "Door jam", "Sensor malfunction", "Anti-skid failure", "Retraction failure",
            "Axle crack", "Shock absorber leak"
        ],
        "risk_level": "Extreme",
        "replacement_interval": {
            "Tires": "200-300 landings or tread depth < 2mm",
            "Brakes": "500-1000 landings or wear sensors trigger",
            "Shock Struts": "5-10 years (nitrogen pressure checks every 500 hrs)",
            "Actuators": "10,000 cycles or 15 years",
            "Bearings": "5,000 FH or grease contamination",
            "WOW Switches": "5 years or intermittent faults",
            "Gear Doors": "15,000 cycles or structural cracks"
        }
    },
    "engine_system": {
        "replacement_name": "Engine System",
        "keywords": [
            "engine stall", "compressor stall", "oil pressure drop", "turbine blade crack",
            "fan blade damage", "igniter failure", "fuel nozzle clog", "bleed air leak",
            "oil leak", "exhaust damage", "engine vibration", "bearing failure",
            "compressor blade erosion", "oil filter clog", "oil pump failure", "turbocharger issue",
            "fuel control unit", "engine control unit", "flame out", "engine surge"
        ],
        "common_parts": [
            "FAN BLADE", "IGNITER", "OIL PUMP", "COMPRESSOR BLADE", "TURBINE BLADE",
            "FUEL NOZZLE", "BLEED AIR VALVE", "OIL FILTER", "FUEL CONTROL UNIT",
            "ENGINE CONTROL UNIT", "EXHAUST DUCT", "OIL COOLER", "BEARING",
            "TURBOCHARGER", "OIL TANK", "FUEL PUMP"
        ],
        "failure_modes": [
            "Oil starvation", "Turbine crack", "Compressor stall", "Igniter failure",
            "Fuel contamination", "Bearing seizure", "Vibration", "Bleed air leak"
        ],
        "risk_level": "Extreme",
        "replacement_interval": {
            "Oil Filter": "500 FH or contamination",
            "Igniter": "2000 FH or failure",
            "Fan Blade": "5,000 cycles or damage",
            "Fuel Nozzle": "4,000 FH or clogging",
            "Compressor Blade": "6,000 FH or erosion"
        }
    },
    "fuel_system": {
        "replacement_name": "Fuel System",
        "keywords": [
            "fuel leak", "fuel pump failure", "fuel contamination", "fuel tank crack",
            "crossfeed valve stuck", "fuel filter clog", "fuel pressure drop",
            "fuel line rupture", "boost pump failure", "fuel level sensor error",
            "fuel control unit failure", "fuel transfer failure", "fuel manifold leak"
        ],
        "common_parts": [
            "FUEL PUMP", "FILTER", "TANK", "CROSSFEED VALVE", "BOOST PUMP",
            "FUEL LEVEL SENSOR", "FUEL MANIFOLD", "FUEL CONTROL UNIT", "FUEL LINE",
            "FUEL TRANSFER PUMP"
        ],
        "failure_modes": [
            "Leakage", "Contamination", "Valve jam", "Pressure drop", "Pump failure",
            "Sensor error", "Fuel starvation"
        ],
        "risk_level": "High",
        "replacement_interval": {
            "Fuel Filter": "1000 FH or clog detected",
            "Boost Pump": "3000 FH or pressure loss",
            "Crossfeed Valve": "5 years or failure",
            "Fuel Tank": "10 years or crack detected"
        }
    },
    "avionics": {
        "replacement_name": "Avionics",
        "keywords": [
            "navigation failure", "FMS error", "autopilot disengage", "radio loss",
            "GPS drift", "display blank", "altimeter fault", "transponder fail",
            "TCAS alert", "weather radar issue", "communication failure",
            "flight management error", "sensor failure", "power surge", "circuit failure"
        ],
        "common_parts": [
            "FMS", "GPS MODULE", "AUTOPILOT UNIT", "VHF RADIO", "TCAS", "ALTIMETER",
            "PFD", "ND", "ADIRU", "DME", "RADAR", "TRANSPONDER", "COM RADIO"
        ],
        "failure_modes": [
            "Loss of signal", "Display failure", "Sensor drift", "Software crash",
            "Power dropout", "Data bus error", "Weather data loss"
        ],
        "risk_level": "Moderate",
        "replacement_interval": {
            "FMS Unit": "6000 FH or software update required",
            "Autopilot": "7500 FH or failure",
            "GPS Receiver": "5 years or signal issues",
            "Display Panels": "6 years or fail"
        }
    },
    "hydraulics": {
        "replacement_name": "Hydraulic System",
        "keywords": [
            "hydraulic leak", "fluid loss", "pressure drop", "actuator jam",
            "hydraulic overheat", "pump fail", "system B loss", "reservoir crack",
            "valve failure", "seal rupture", "filter clog"
        ],
        "common_parts": [
            "HYDRAULIC PUMP", "RESERVOIR", "HYD ACTUATOR", "PRESSURE SWITCH",
            "MANIFOLD", "RELIEF VALVE", "HYD LINE", "FILTER", "ACCUMULATOR", "INDICATOR"
        ],
        "failure_modes": [
            "Leakage", "Cavitation", "Pressure loss", "Pump overheating", "Seal rupture"
        ],
        "risk_level": "High",
        "replacement_interval": {
            "Hydraulic Filter": "Every 1000 FH",
            "Pump": "Every 4000 FH or pressure drop",
            "Reservoir": "8 years or crack signs"
        }
    },
    "electrical": {
        "replacement_name": "Electrical System",
        "keywords": [
            "short circuit", "power loss", "battery drain", "generator fail",
            "voltage drop", "circuit breaker trip", "wiring fault", "busbar failure"
        ],
        "common_parts": [
            "GENERATOR", "BATTERY", "BUSBAR", "CIRCUIT BREAKER", "INVERTER", "TRANSFORMER",
            "FUSE", "RELAYS", "SWITCHES", "WIRING HARNESS"
        ],
        "failure_modes": [
            "Power loss", "Overvoltage", "Undervoltage", "Component burn", "Battery failure"
        ],
        "risk_level": "Moderate",
        "replacement_interval": {
            "Battery": "2 years or capacity drop",
            "Generator": "5000 FH",
            "Inverter": "6000 FH"
        }
    },
    "air_conditioning": {
        "replacement_name": "Air Conditioning System",
        "keywords": [
            "cabin overheat", "pack failure", "airflow drop", "temperature spike",
            "valve jam", "sensor failure", "duct blockage"
        ],
        "common_parts": [
            "PACK", "HEAT EXCHANGER", "ACM", "DUCTING", "CABIN SENSOR", "VALVES"
        ],
        "failure_modes": [
            "Pack overheat", "Sensor failure", "Duct blockage", "Valve jam"
        ],
        "risk_level": "Low",
        "replacement_interval": {
            "PACK": "8000 FH",
            "Sensor": "3 years or signal loss"
        }
    },
    "fire_protection": {
        "replacement_name": "Fire Protection System",
        "keywords": [
            "smoke detection", "engine fire", "cargo fire", "fire bottle",
            "loop failure", "discharge failure", "false alert"
        ],
        "common_parts": [
            "SMOKE DETECTOR", "FIRE BOTTLE", "FIRE LOOP", "DISCHARGE SWITCH"
        ],
        "failure_modes": [
            "Sensor failure", "Discharge fail", "Loop break", "False alert"
        ],
        "risk_level": "High",
        "replacement_interval": {
            "Fire Bottle": "5 years",
            "Smoke Detector": "2 years or fail"
        }
    },
    "flight_controls": {
        "replacement_name": "Flight Controls",
        "keywords": [
            "aileron jam", "rudder issue", "elevator stuck", "servo failure",
            "cable snap", "trim failure", "actuator delay", "control surface jam"
        ],
        "common_parts": [
            "AILERON", "RUDDER", "ELEVATOR", "ACTUATOR", "CABLE", "TRIM MOTOR"
        ],
        "failure_modes": [
            "Cable snap", "Servo motor failure", "Jam", "Actuator delay"
        ],
        "risk_level": "Extreme",
        "replacement_interval": {
            "Actuators": "7000 FH or cycle count",
            "Control Cables": "10 years or tension loss"
        }
    }
}

# === REPLACEMENT HOURS MAPPING (Fixed FH values per system) ===
replacement_hours = {
    "landing_gear": 3500,
    "engine_system": 5000,
    "fuel_system": 4000,
    "avionics": 6000,
    "hydraulics": 4500,
    "electrical": 5000,
    "air_conditioning": 8000,
    "fire_protection": 7000,
    "flight_controls": 7500
}

# === COUNTRY PRIORITY EXAMPLES ===
country_priority = {
    "Morocco": ["landing_gear", "fuel_system", "engine_system"],
    "United States": ["engine_system", "avionics", "hydraulics"],
    "Saudi Arabia": ["landing_gear", "hydraulics", "fuel_system"],
    "India": ["fuel_system", "engine_system", "landing_gear"],
    "Russia": ["engine_system", "landing_gear", "hydraulics"],
    "Germany": ["avionics", "fuel_system", "engine_system"],
    "France": ["avionics", "engine_system", "fuel_system"],
    "Brazil": ["fuel_system", "landing_gear", "avionics"],
    "Canada": ["avionics", "engine_system", "landing_gear"],
    "South Africa": ["landing_gear", "hydraulics", "engine_system"]
}

# === ALL 195 COUNTRIES ===
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
    "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
    "DR Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
    "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos",
    "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia",
    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

geo_zones = ["Desert", "Coastal", "Tropical", "Arctic", "Mountain", "Continental", "Island", "Urban"]

# === DATASET GENERATION ===
dataset = []

for country in countries:
    geo = ", ".join(random.sample(geo_zones, k=random.randint(1, 3)))
    priority_systems = country_priority.get(country, random.sample(list(systems.keys()), 3))

    for sys_key in systems:
        is_priority = sys_key in priority_systems

        record = {
            "country": country,
            "geographical_location": geo,
            "replacement_flighthour": replacement_hours[sys_key],
            "replacement_name": systems[sys_key]["replacement_name"],
            "keywords": systems[sys_key]["keywords"],
            "common_parts": systems[sys_key]["common_parts"],
            "failure_modes": systems[sys_key]["failure_modes"],
            "risk_level": systems[sys_key]["risk_level"],
            "replacement_interval": systems[sys_key]["replacement_interval"],
            "priority_system": is_priority
        }
        dataset.append(record)

# === SAVE JSON FILE ===
with open(output, "w") as f:
    json.dump(dataset, f, indent=2)

print("✅ File 'aircraft_maintenance_fixed_FH.json' generated with fixed flight hours.")
