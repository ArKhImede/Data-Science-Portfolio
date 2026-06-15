BLOODSTREAM_INVADERS = ["PM2.5", "PM1", "BC"]
LUNG_BURNERS = ["NO2", "O3", "SO2", "NOX", "NO"]
GATEWAY_IRRITANTS = ["PM10"]
WILDCARDS = ["CO", "UM003"]
ENVIRONMENT = ["TEMPERATURE", "RELATIVEHUMIDITY"]


def choose_pollutant_danger(pollutant: str) -> str:
    pollutant_clean = str(pollutant).strip().upper()

    if pollutant_clean in BLOODSTREAM_INVADERS:
        return "Most Dangerous"
    elif pollutant_clean in LUNG_BURNERS:
        return "Highly Harmful"
    elif pollutant_clean in GATEWAY_IRRITANTS:
        return "Moderate"
    elif pollutant_clean in WILDCARDS:
        return "Context-Dependent"
    elif pollutant_clean in ENVIRONMENT:
        return "Weather/Environment Factor"
    else:
        return "Harmless"
