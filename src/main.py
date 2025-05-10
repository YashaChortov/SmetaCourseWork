import sys
from PyQt5.QtWidgets import QApplication
from smeta_app.view.main_window import MainWindow
from smeta_app.presenter.estimate_presenter import EstimatePresenter


def main():
    app = QApplication(sys.argv)

    view = MainWindow()
    presenter = EstimatePresenter(view)

    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()