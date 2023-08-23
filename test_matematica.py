from app.AC1 import Matematica


def test_salarioLiquido():
    assert Matematica.salario_liquido(200, 13.9, 6.48) == (2599.86)




def test_DescontoDoProduto():
    assert Matematica.DescontoDoProduto(60000) == (54600, 5400)




def test_ValorPromocao():
    assert Matematica.ValorPromocao(500, 50) == (450)



def test_ValorTotal():
    assert Matematica.ValorTotal(125) == (137.50, 12.5)




