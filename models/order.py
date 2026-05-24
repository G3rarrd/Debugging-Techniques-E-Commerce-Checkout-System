from decimal import Decimal, getcontext
import logging
from uuid import UUID

getcontext().prec = 28
LOGGER = logging.getLogger(__name__) # Helps identify the logs are coming from.

class Order:
    def __init__(self, items : dict[UUID, int], total : Decimal, discount_applied : Decimal):
        self._items = items
        self._total = total
        self._discount_applied = discount_applied

    @property
    def items(self):
        return self._items

    @property
    def total(self):
        return self._total

    @property
    def discount_applied(self):
        return self._discount_applied
    
    def __repr__(self):
        return (
            f"Order("
            f"items={self._items}, "
            f"total={self._total}, "
            f"discount_applied={self._discount_applied}"
            f")"
        )
    
    def __str__(self):
        return (
            f"Order("
            f"items={self._items}, "
            f"total={self._total}, "
            f"discount_applied={self._discount_applied}"
            f")"
        )