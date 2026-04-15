def compute_price(km, vtype, hr):
    price_chart = {
        "ECONOMY": 10,
        "PREMIUM": 18,
        "SUV": 25
    }

    vtype_clean = vtype.strip().upper()

    if vtype_clean not in price_chart:
        raise ValueError("Service Not Available")

    cost = km * price_chart[vtype_clean]

    peak_flag = False

    if 17 <= hr <= 20:
        cost *= 1.5
        peak_flag = True

    return round(cost, 1), peak_flag