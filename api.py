import asyncio
from typing import Literal

import aiohttp as aiohttp


class AlphaAPI:
    def __init__(self):
        self.token = "demo"
        self.url = "https://www.alphavantage.co/query"

    async def __request(self, function: Literal["OVERVIEW", "INCOME_STATEMENT"], symbol: str) -> dict:
        params = dict(function=function, symbol=symbol, apikey=self.token)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url, params=params) as resp:
                return await resp.json()

    async def get_overview(self, symbol: str) -> tuple:
        """Метод получения P/S и полное название компании"""
        result = await self.__request(function="OVERVIEW", symbol=symbol)
        try:
            return float(result["PriceToSalesRatioTTM"]), result["Name"]
        except KeyError:
            return

    async def get_revenue_five_ttm(self, symbol: str) -> float:
        """Метод получения Total Revenue 5TTM в виде десятичной дроби с округлением 6зн"""
        result = await self.__request(function="INCOME_STATEMENT", symbol=symbol)
        try:
            quarters = result["quarterlyReports"]
        except KeyError:
            return
        first_total_revenue = 0
        last_total_revenue = 0
        for quarter in quarters[-4:]:
            first_total_revenue += int(quarter["totalRevenue"])
        for quarter in quarters[:4]:
            last_total_revenue += int(quarter["totalRevenue"])
        return round((last_total_revenue - first_total_revenue) * 100 / first_total_revenue, 6)



async def main():
    api = AlphaAPI()
    result = await api.get_revenue_five_ttm(symbol="AMZN")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
