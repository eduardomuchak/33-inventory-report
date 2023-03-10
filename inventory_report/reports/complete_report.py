from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        products_per_company = cls.get_count_products_per_company(products)

        complete_report = ""

        for key, value in products_per_company.items():
            complete_report += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{complete_report}"
        )

    @classmethod
    def get_count_products_per_company(cls, products):
        companies_products = {}
        for product in products:
            company = product["nome_da_empresa"]
            if company in companies_products:
                companies_products[company] += 1
            else:
                companies_products[company] = 1
        return companies_products
