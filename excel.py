from typing import List

from openpyxl import Workbook
from openpyxl.styles import Font
import os


class ExcelCreate:

    @classmethod
    def create_file(cls, data: List[dict]):
        """Создание и сохранение файла"""
        file_path = f"{os.getcwd()}/report.xlsx"
        wb = Workbook()
        ws = wb.active
        ws.append(
            (
                "Тикер",
                "Название компании",
                "P/S (Price to Sales)",
                "Рост выручки за 5 лет (Total Revenue Growth Rate 5Y (TTM)",
                "Рост выручки за 5 лет / P/S",
            )
        )
        ft = Font(bold=True)
        for row in ws['A1:T1']:
            for cell in row:
                cell.font = ft
        for item in data:
            ws.append(
                (
                    item["ticker"],
                    item["name"],
                    item["price_to_sales"],
                    item["total_revenue_ttm"],
                    item["tr_div_ps"]
                )
            )
        wb.save(filename=file_path)
        return file_path