'''
from unittest.mock import MagicMock
from smeta_app.presenter.estimate_presenter import EstimatePresenter


def test_add_item():
    mock_view = MagicMock()
    mock_view.name_input.text.return_value = "Тест"
    mock_view.quantity_input.text.return_value = "2"
    mock_view.price_input.text.return_value = "100"

    presenter = EstimatePresenter(mock_view)
    presenter.add_item()

    assert len(presenter.estimate.items) == 1
    #mock_view.update_view.assert_called_once()
'''

import pytest
from unittest.mock import MagicMock, patch

from smeta_app.model.item import EstimateItem
from smeta_app.presenter.estimate_presenter import EstimatePresenter


class TestEstimatePresenter:
    @pytest.fixture
    def mock_view(self):
        view = MagicMock()
        view.name_input = MagicMock()
        view.quantity_input = MagicMock()
        view.price_input = MagicMock()
        view.table = MagicMock()
        view.total_label = MagicMock()
        view.show_error = MagicMock()  # Добавляем mock для show_error
        return view

    def test_add_valid_item(self, mock_view):
        mock_view.name_input.text.return_value = "Тестовый товар"
        mock_view.quantity_input.text.return_value = "2"
        mock_view.price_input.text.return_value = "100.50"

        presenter = EstimatePresenter(mock_view)
        presenter.add_item()

        assert len(presenter.estimate.items) == 1
        mock_view.update_view.assert_called_once()
        mock_view.show_error.assert_not_called()

    @pytest.mark.parametrize("qty,price,expected_error", [
        ("2a", "100", "Количество содержит недопустимые символы"),
        ("2!", "100", "Количество содержит недопустимые символы"),
        ("2.3.4", "100", "Некорректный формат количества"),
        ("2-3", "100", "Некорректный формат количества"),
        ("2", "100a", "Цена содержит недопустимые символы"),
        ("2", "100$", "Цена содержит недопустимые символы"),
        ("2", "10.50.25", "Некорректный формат цены"),
        ("2", "10-50", "Некорректный формат цены"),
    ])
    def test_invalid_symbols(self, mock_view, qty, price, expected_error):
        mock_view.name_input.text.return_value = "Тестовый товар"
        mock_view.quantity_input.text.return_value = qty
        mock_view.price_input.text.return_value = price

        presenter = EstimatePresenter(mock_view)
        presenter.add_item()

        mock_view.show_error.assert_called_once_with(expected_error)
        assert len(presenter.estimate.items) == 0
    def test_invalid_inputs(self, mock_view, name, qty, price, expected_error):
        mock_view.name_input.text.return_value = name
        mock_view.quantity_input.text.return_value = qty
        mock_view.price_input.text.return_value = price

        presenter = EstimatePresenter(mock_view)
        presenter.add_item()

        mock_view.show_error.assert_called_once_with(expected_error)
        assert len(presenter.estimate.items) == 0

    def test_update_view_calls(self, mock_view):
        presenter = EstimatePresenter(mock_view)
        presenter.estimate.add_item(EstimateItem("Товар 1", 2, 100))
        presenter.estimate.add_item(EstimateItem("Товар 2", 3, 50))

        presenter.update_view()

        assert mock_view.table.setRowCount.call_count == 1
        assert mock_view.table.setItem.call_count == 8  # 4 поля x 2 строки
        mock_view.total_label.setText.assert_called_once_with("Итого: 350.00")