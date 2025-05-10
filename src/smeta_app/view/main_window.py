from PyQt5.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QPushButton, QLineEdit,
    QMessageBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сметная программа")
        self.setup_ui()

    def setup_ui(self):
        # Widgets
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Наименование", "Кол-во", "Цена", "Сумма"])

        self.name_input = QLineEdit(placeholderText="Наименование")
        self.quantity_input = QLineEdit(placeholderText="Количество")
        self.price_input = QLineEdit(placeholderText="Цена")
        self.add_button = QPushButton("Добавить")
        self.total_label = QLineEdit("Итого: 0.00")
        self.total_label.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.name_input)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.price_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.total_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def setFocus(self):
        self.name_input.setFocus()

    def show_error(self, message):
        QMessageBox.critical(self, "Ошибка", message)