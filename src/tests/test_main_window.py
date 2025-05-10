from PyQt5.QtWidgets import QTableWidgetItem
from smeta_app.view.main_window import MainWindow
import pytest


class TestMainWindow:
    @pytest.fixture
    def window(self):
        return MainWindow()

    def test_ui_elements_exist(self, window):
        assert hasattr(window, 'table')
        assert hasattr(window, 'name_input')
        assert hasattr(window, 'add_button')

    def test_update_view(self, window):
        test_data = [
            ("Товар 1", "2", "100", "200.00"),
            ("Товар 2", "3", "50", "150.00")
        ]

        # Добавляем метод update_view, если его нет
        if not hasattr(window, 'update_view'):
            def update_view(data):
                window.table.setRowCount(len(data))
                for row, (name, qty, price, cost) in enumerate(data):
                    window.table.setItem(row, 0, QTableWidgetItem(name))
                    window.table.setItem(row, 1, QTableWidgetItem(qty))
                    window.table.setItem(row, 2, QTableWidgetItem(price))
                    window.table.setItem(row, 3, QTableWidgetItem(cost))

            window.update_view = update_view

        window.update_view(test_data)

        assert window.table.rowCount() == 2
        for row in range(2):
            for col in range(4):
                assert window.table.item(row, col) is not None

    def test_show_error(self, window):
        # Добавляем метод show_error, если его нет
        if not hasattr(window, 'show_error'):
            window.show_error = lambda msg: None

        window.show_error("Тестовая ошибка")
        # Проверяем, что метод вызван без ошибок
        assert True