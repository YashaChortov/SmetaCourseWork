class EstimateItem:
    def __init__(self, name: str, quantity: float, price: float, unit: str = "шт."):
        self.id = id(self)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.unit = unit

    @property
    def cost(self) -> float:
        return self.quantity * self.price