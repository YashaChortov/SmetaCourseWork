from typing import List
from smeta_app.model.item import EstimateItem

class Estimate:
    def __init__(self, name: str = "Новая смета"):
        self.id = id(self)
        self.name = name
        self.items: List[EstimateItem] = []
        self._status = "draft"  # draft/approved/archived

    @property
    def total(self) -> float:
        return sum(item.cost for item in self.items)

    def add_item(self, item: EstimateItem):
        self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [item for item in self.items if item.id != item_id]