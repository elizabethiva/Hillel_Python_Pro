import asyncio
from pprint import pprint as print
import httpx


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, urls: list) -> None:
        if ExchangeRates._initialized:
            return None

        self.data = asyncio.run(fetch_from_api(urls))

        ExchangeRates._initialized = True


async def fetch_from_api(urls: list) -> list:
    async with httpx.AsyncClient() as client:
        requests = [client.get(url) for url in urls]
        result = [res.json() for res in await asyncio.gather(*requests)]
    return result


urls = [
    "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=UAH&apikey=EFO5Z08U1IXU5EXO",
    "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey=EFO5Z08U1IXU5EXO",
    "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=UAH&to_currency=USD&apikey=EFO5Z08U1IXU5EXO",
    "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=UAH&to_currency=GBP&apikey=EFO5Z08U1IXU5EXO",
]

