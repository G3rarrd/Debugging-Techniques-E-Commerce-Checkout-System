from decimal import Decimal, getcontext

import logging
from logging import Logger

from models.product import Product

getcontext().prec = 28
LOGGER : Logger = logging.getLogger(__name__)
class CartItem:
    def __init__(self, product : Product, quantity : int):
        action : str = "CartItem creation"
        if quantity < 1:
            LOGGER.error(
                f"{action} failed: invalid quantity {quantity}"
                f"for product {product.name} (ID: {product.id})"
            )
            raise ValueError("Quantity must be greater than 0")

        if quantity > product.stock_quantity:
            LOGGER.error(
                f"{action} failed: requested {quantity} x {product.name}. "
                f"Only {product.stock_quantity} available. "
                f"Product ID: {product.id}"
            )
            raise ValueError("Quantity exceeds available stock")
        
        self.__product : Product = product
        self.__quantity : int = quantity
        LOGGER.info(
            f"[CART ITEM CREATED] "
            F"Product name: {product.name} "
            f"Quantity used: {quantity} "
            f"(Product ID: {product.id})"
        )

    @property
    def product(self):
        return self.__product
    
    @property
    def quantity(self):
        return self.__quantity
    
    @property
    def subtotal(self) -> Decimal:
        return self.__product.price * self.quantity

    def __repr__(self):
        return (
            f"CartItem("
            f"product={self.__product.name!r}, "
            f"quantity={self.__quantity}, "
            f"subtotal={self.subtotal}"
            f")"
        )

    def __str__(self):
        return (
            f"CartItem("
            f"product={self.__product.name}, "
            f"quantity={self.__quantity}, "
            f"subtotal={self.subtotal})"
        )
    
    def increase_quantity(self, amount: int) -> None:
        action : str = "Increase quantity"
        if amount < 1:
            LOGGER.error(
                f"{action} failed: invalid amount {amount} "
                f"for product {self.__product.name}"
            )
            raise ValueError("Increase amount must be greater than zero")

        if self.__quantity + amount > self.__product.stock_quantity:
            LOGGER.error(
                f"{action} failed: +{amount} x {self.__product.name} "
                f"exceeds stock ({self.__product.stock_quantity})"
            )
            raise ValueError("Insufficient stock available")

        self.__quantity += amount
        
        LOGGER.info(
            f"CartItem updated: +{amount} x {self.__product.name}. "
            f"New quantity: {self.__quantity}"
        )

    def decrease_quantity(self, amount: int) -> None:
        action : str = "Decrease quantity"
        if amount < 1:
            LOGGER.error(
                f"{action} failed: invalid amount {amount} "
                f"for product {self.__product.name}"
            )
            raise ValueError("Decrease amount must be greater than 0")

        if self.__quantity - amount < 1:
            LOGGER.error(
                f"{action} failed: -{amount} x {self.__product.name} "
                f"would result in invalid quantity (current: {self.__quantity})"
            )
            raise ValueError("Quantity cannot go below 1")

        self.__quantity -= amount

        LOGGER.info(
            f"CartItem updated: -{amount} x {self.__product.name}. "
            f"New quantity: {self.__quantity}"
        )
