from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

mock = [
    {
        "id": 1,
        "nome_do_produto": "Café",
        "nome_da_empresa": "Orfeu",
        "data_de_fabricacao": "2020-01-01",
        "data_de_validade": "2021-01-01",
        "numero_de_serie": "123456789",
        "instrucoes_de_armazenamento": "em local seco, fresco e longe de luz",
    },
]


def test_decorar_relatorio():
    report = ColoredReport(SimpleReport()).generate(mock)

    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[36m"
    final = "\033[0m"

    assert f"{green}Data de fabricação mais antiga:{final}" in report
    assert f"{blue}2020-01-01{final}" in report

    assert f"{green}Data de validade mais próxima:{final}" in report
    assert f"{blue}2021-01-01{final}" in report

    assert f"{green}Empresa com mais produtos:{final}" in report
    assert f"{red}Orfeu{final}" in report
