from inventory_report.importer.csv_importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls: str, path: str):
        if path.endswith(".csv"):
            with open(path) as file:
                return [row for row in csv.DictReader(file)]
        else:
            raise ValueError("Arquivo inválido")
