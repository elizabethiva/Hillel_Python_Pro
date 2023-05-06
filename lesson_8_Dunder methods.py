import requests


class Price:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency
        self.currency_to_usd = get_rate(self.currency, "USD")

    def __add__(self, other) -> float:
        if self.currency == other.currency:
            return self.represent(self.amount + other.amount)
        else:
            total = (
                self.amount * self.currency_to_usd
                + other.amount * other.currency_to_usd
            ) / self.currency_to_usd
            return self.represent(total)

    def __sub__(self, other) -> float:
        if self.currency == other.currency:
            return self.represent(self.amount - other.amount)
        else:
            total = (
                self.amount * self.currency_to_usd
                - other.amount * other.currency_to_usd
            ) / self.currency_to_usd
            return self.represent(total)

    def represent(self, total: float) -> str:
        return f"{round(total,3)} {self.currency}"


def get_rate(source: str, target: str) -> float:
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source}&to_currency={target}&apikey=EFO5Z08U1IXU5EXO"
    response = requests.get(url)
    return float(response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"])


left = Price(1000, "UAH")
right = Price(5, "GBP")
a = left + right
s = left - right
print(a)
print(s)
