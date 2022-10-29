from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "Café",
        "Orfeu",
        "2020-01-01",
        "2021-01-01",
        "123456789",
        "em local seco, fresco e longe de luz",
    )
    assert (
        produto.__repr__() == "O produto Café"
        " fabricado em 2020-01-01"
        " por Orfeu com validade"
        " até 2021-01-01"
        " precisa ser armazenado em local seco, fresco e longe de luz."
    )
