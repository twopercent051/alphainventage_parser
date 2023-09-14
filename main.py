import asyncio
import json

from api import AlphaAPI
from excel import ExcelCreate

api = AlphaAPI()


async def main():
    with open("tickers.json") as config_file:
        tickers = json.loads(config_file.read())
        result_list = []
        count = 0
        for ticker in tickers:
            ticker = ticker.upper()
            overview = await api.get_overview(symbol=ticker)
            total_revenue_ttm = await api.get_revenue_five_ttm(symbol=ticker)
            if overview and total_revenue_ttm:
                price_to_sales = overview[0]
                name_company = overview[1]
                tr_div_ps = round(total_revenue_ttm / price_to_sales, 6)
                data = dict(ticker=ticker,
                            name=name_company,
                            price_to_sales=price_to_sales,
                            total_revenue_ttm=f"{total_revenue_ttm} %",
                            tr_div_ps=f"{tr_div_ps} %")
                count += 1
            else:
                data = dict(ticker=ticker, name="---", price_to_sales="---", total_revenue_ttm="---", tr_div_ps="---")
            result_list.append(data)
        ExcelCreate.create_file(data=result_list)
        print(f"Обработано {count} из {len(tickers)} тикеров")


if __name__ == "__main__":
    asyncio.run(main())