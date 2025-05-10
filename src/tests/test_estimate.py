'''
from smeta_app.model.estimate import Estimate
from smeta_app.model.item import EstimateItem

def test_add_item():
    estimate = Estimate()
    item = EstimateItem("Тест", 2, 100)
    estimate.add_item(item)
    assert len(estimate.items) == 1

def test_total_calculation():
    estimate = Estimate()
    estimate.add_item(EstimateItem("Товар 1", 2, 100))
    estimate.add_item(EstimateItem("Товар 2", 3, 50))
    assert estimate.total == 350
'''

import pytest
from smeta_app.model.estimate import Estimate
from smeta_app.model.item import EstimateItem


class TestEstimateModel:
    def test_add_item(self):
        estimate = Estimate()
        item = EstimateItem("Тестовый товар", 2, 100)
        estimate.add_item(item)
        assert len(estimate.items) == 1
        assert estimate.items[0].name == "Тестовый товар"

    def test_total_calculation(self):
        estimate = Estimate()
        estimate.add_item(EstimateItem("Товар 1", 2, 100))
        estimate.add_item(EstimateItem("Товар 2", 3, 50.5))
        assert estimate.total == 351.5  # 2*100 + 3*50.5 = 351.5

    def test_remove_item(self):
        estimate = Estimate()
        item1 = EstimateItem("Товар A", 1, 10)
        item2 = EstimateItem("Товар B", 2, 20)
        estimate.add_item(item1)
        estimate.add_item(item2)

        estimate.remove_item(item1.id)
        assert len(estimate.items) == 1
        assert estimate.items[0].name == "Товар B"

    @pytest.mark.parametrize("qty,price,expected", [
        (2, 100, 200),
        (1.5, 10.5, 15.75),
        (3, 33.33, 99.99)
    ])
    def test_item_cost_calculation(self, qty, price, expected):
        item = EstimateItem("Тест", qty, price)
        assert float(item.cost) == pytest.approx(float(expected))