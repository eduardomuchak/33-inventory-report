from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products):
        oldest_manufactoring_date = cls.get_oldest_manufactoring_date(products)
        nearest_expiration_date = cls.get_nearest_expiration_date(products)
        company_with_more_products = cls.get_company_with_more_products(
            products
        )

        return (
            f"Data de fabricação mais antiga: {oldest_manufactoring_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )

    @classmethod
    def get_oldest_manufactoring_date(cls, products):
        oldest_manufactoring_date = datetime.now()
        for product in products:
            manufactoring_date = datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            )
            if manufactoring_date:
                if manufactoring_date < oldest_manufactoring_date:
                    oldest_manufactoring_date = manufactoring_date
        return oldest_manufactoring_date.strftime("%Y-%m-%d")

    @classmethod
    def get_nearest_expiration_date(cls, products):
        return min(
            [
                datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                for product in products
            ]
        ).strftime("%Y-%m-%d")

    @classmethod
    def get_company_with_more_products(cls, products):
        companies = {}
        for product in products:
            company = product["nome_da_empresa"]
            if company in companies:
                companies[company] += 1
            else:
                companies[company] = 1

        return max(companies, key=companies.get)
