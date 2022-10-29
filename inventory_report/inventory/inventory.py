from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls: str, path: str, type: str):
        report: str = ""
        product_info: list = []
        with open(path) as file:
            if path.endswith(".csv"):
                product_info = [row for row in csv.DictReader(file)]
            if path.endswith(".json"):
                product_info = json.load(file)
            if path.endswith(".xml"):
                product_info = xmltodict.parse(file.read())["dataset"][
                    "record"
                ]
            if type == "simples":
                report = SimpleReport.generate(product_info)
            else:
                report = CompleteReport.generate(product_info)
            return report
