BASE_PRICE = {
    "basic": 150,
    "bot_db": 250,
    "ai_agent": 400,
}

SCENARIOS_SURCHARGE = {
    "1-3": 0,
    "4-7": 50,
    "8+": 100,
}

INTEGRATIONS_SURCHARGE = 70


def calculate_price(service, scenarios, integrations):
    base = BASE_PRICE[service]
    surcharge = SCENARIOS_SURCHARGE[scenarios]
    if integrations:
        surcharge += INTEGRATIONS_SURCHARGE

    low = base + surcharge
    high = low + 100
    return low, high
