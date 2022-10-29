from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "Café",
        "Orfeu",
        "2020-01-01",
        "2021-01-01",
        "123456789",
        "em local seco, fresco e longe de luz",
    )
    assert produto.id == 1
    assert produto.nome_do_produto == "Café"
    assert produto.nome_da_empresa == "Orfeu"
    assert produto.data_de_fabricacao == "2020-01-01"
    assert produto.data_de_validade == "2021-01-01"
    assert produto.numero_de_serie == "123456789"
    assert (
        produto.instrucoes_de_armazenamento
        == "em local seco, fresco e longe de luz"
    )
