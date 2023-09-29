import pytest
from calculadora import soma, subtracao, multiplicacao, divisao


def test_soma():
    assert soma(2, 3) == 4
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(10, -5) == 5


def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(10, 5) == 5
    assert subtracao(-1, 1) == -2
    assert subtracao(0, 0) == 0


def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-1, 1) == -1
    assert multiplicacao(0, 5) == 0
    assert multiplicacao(4, 0.5) == 2


def test_divisao():
    assert divisao(6, 2) == 3
    assert divisao(-8, 4) == -2
    assert divisao(10, 2) == 5

    with pytest.raises(ValueError):
        divisao(5, 0)  # Teste de divisão por zero
