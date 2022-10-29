from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path) as file:
                return [row for row in csv.DictReader(file)]
        else:
            raise ValueError("Arquivo inválido")
