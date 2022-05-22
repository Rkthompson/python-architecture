from dataclasses import dataclass
from typing import Optional
from datetime import date


# Order class
@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


# Batch class
class Batch:
    def __init__(
        self, ref: str, sku: str, qty: int, eta: Optional[date]
    ):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()  # type: set[OrderLine]

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)


'''
    def allocate(self, line: OrderLine):
        if(self.check_in_stock(line)):
            self.available_quantity -= line.qty
        else:
            print('Out of stock')


    def check_in_stock(self, line):
        if(self.available_quantity >= line.qty):
            return True
        else:
            return False
'''
