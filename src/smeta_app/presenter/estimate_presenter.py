from PyQt5.QtWidgets import QTableWidgetItem
from smeta_app.model.estimate import Estimate
from smeta_app.model.item import EstimateItem


class EstimatePresenter:
    def __init__(self, view):
        self.view = view
        self.estimate = Estimate()
        self._connect_signals()

    def _connect_signals(self):
        self.view.add_button.clicked.connect(self.add_item)

    def add_item(self):
        """Добавляет новую позицию в смету с валидацией данных"""
        try:
            # Получаем и валидируем наименование
            name = self.view.name_input.text().strip()
            if not name:
                raise ValueError("Необходимо указать наименование позиции")
            if len(name) > 100:
                raise ValueError("Наименование слишком длинное (макс. 100 символов)")

            # Получаем и валидируем количество
            quantity_text = self.view.quantity_input.text().strip().replace(',', '.')

            # Проверка на недопустимые символы
            if not all(c.isdigit() or c in '.-' for c in quantity_text):
                raise ValueError("Количество содержит недопустимые символы")

            # Проверка на корректное число точек/минусов
            if quantity_text.count('.') > 1 or quantity_text.count('-') > 1 or \
                    (quantity_text.count('-') == 1 and not quantity_text.startswith('-')):
                raise ValueError("Некорректный формат количества")


            quantity = float(quantity_text)
            if quantity <= 0:
                raise ValueError("Количество должно быть положительным числом")
            if quantity > 1000000:
                raise ValueError("Слишком большое количество")

            # Получаем и валидируем цену
            price_text = self.view.price_input.text().strip().replace(',', '.')

            # Проверка на недопустимые символы
            if not all(c.isdigit() or c in '.-' for c in price_text):
                raise ValueError("Цена содержит недопустимые символы")

            # Проверка на корректное число точек/минусов
            if price_text.count('.') > 1 or price_text.count('-') > 1 or \
                    (price_text.count('-') == 1 and not price_text.startswith('-')):
                raise ValueError("Некорректный формат цены")

            price = float(price_text)
            if price <= 0:
                raise ValueError("Цена должна быть положительным числом")
            if price > 10000000:
                raise ValueError("Слишком большая цена")

            # Создаем и добавляем позицию
            item = EstimateItem(name, quantity, price)
            self.estimate.add_item(item)
            self.update_view()

            # Очистка полей и сброс фокуса
            self.view.name_input.clear()
            self.view.quantity_input.clear()
            self.view.price_input.clear()
            self.view.name_input.setFocus()

        except ValueError as e:
            self.view.show_error(str(e))

    def update_view(self):
        """Обновляет таблицу и итоговую сумму"""
        self.view.table.setRowCount(len(self.estimate.items))
        for row, item in enumerate(self.estimate.items):
            self.view.table.setItem(row, 0, QTableWidgetItem(item.name))
            self.view.table.setItem(row, 1, QTableWidgetItem(f"{item.quantity:.2f}"))
            self.view.table.setItem(row, 2, QTableWidgetItem(f"{item.price:.2f}"))
            self.view.table.setItem(row, 3, QTableWidgetItem(f"{item.cost:.2f}"))

        self.view.total_label.setText(f"Итого: {self.estimate.total:.2f}")