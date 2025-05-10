# smeta_app/__init__.py
"""
Основной пакет сметной программы.

Содержит:
- model: Бизнес-логика и данные
- view: Пользовательский интерфейс
- presenter: Связующая логика (MVP)
"""

__version__ = "0.1.0"

# Делаем ключевые классы доступными на верхнем уровне пакета
from .model.estimate import Estimate
from .model.item import EstimateItem
from .view.main_window import MainWindow