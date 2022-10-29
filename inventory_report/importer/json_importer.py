from inventory_report.importer.csv_importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path) as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido")
