class FareService:
    rates = {
        "ECONOMY": 10,
        "PREMIUM": 18,
        "SUV": 25
    }

    def calculate(self, km, vehicle, hour):
        vehicle = vehicle.strip().upper()  # 🔥 IMPORTANT FIX

        if vehicle not in self.rates:
            raise ValueError("Service Not Available")

        cost = km * self.rates[vehicle]

        if 17 <= hour <= 20:
            cost *= 1.5

        return round(cost, 1)