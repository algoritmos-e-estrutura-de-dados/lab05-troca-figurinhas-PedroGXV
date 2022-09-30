from main import maximizar_troca_de_figurinhas

def test_scenario_01():
    maria = [1000]
    joao = [1000]

    assert maximizar_troca_de_figurinhas(maria, joao) == 0


def test_scenario_02():
    maria = ['1', '3', '5']
    joao = ['2', '4', '6', '8']

    assert maximizar_troca_de_figurinhas(maria, joao) == 3


def test_scenario_03():
    maria = ['1', '1', '2', '3', '5', '7', '8', '8', '9', '15']
    joao = ['2', '2', '2', '3', '4', '6', '10', '11', '11']

    assert maximizar_troca_de_figurinhas(maria, joao) == 4
