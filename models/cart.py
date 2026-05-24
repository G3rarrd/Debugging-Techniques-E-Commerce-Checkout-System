from decimal import Decimal, getcontext

import logging
from logging import Logger

from uuid import UUID

from models.product import Product
from models.cart_item import CartItem

getcontext().prec = 28
LOGGER : Logger =  logging.getLogger(__name__)

class Cart:
    def __init__(self):
        self.__items : dict[UUID, CartItem] = {}

        LOGGER.info("CART CREATED")

    @property
    def items(self) -> dict[UUID, CartItem]:
        return self.__items
    
    @property
    def total(self) -> Decimal:
        return sum((value.subtotal for value in self.__items.values()), Decimal("0"))
    
    def __str__(self):
        return (
            f"Cart("
            f"items={list(self.__items.values())}, "
            f"total={self.total}"
            f")"
        )
    
    def __repr__(self):
        return (
            f"Cart("
            f"items={list(self.__items.values())}, "
            f"total={self.total})"
        )
    
    def clear_cart(self) -> None:
        self.__items.clear()
        LOGGER.info("Cart cleared")

    def add_item(self, product : Product, quantity_to_add : int) -> None:

        if quantity_to_add < 1:
            LOGGER.error(f"Tried adding {quantity_to_add} {product.name} which is invalid")
            raise ValueError("Product quantity to add must be greater than zero")
        

        if product.id in self.__items:
            cart_item : CartItem = self.__items[product.id]

            cart_item.increase_quantity(quantity_to_add)

            LOGGER.info(
                f"Cart updated: Added {product.name} x{quantity_to_add}. "
                f"New quantity: {cart_item.quantity} "
                f"Product ID: {product.id}"
            )

        else:
            self.__items[product.id] = CartItem(product, quantity_to_add)
            
            LOGGER.info(
                f"Cart item created: {product.name} x{quantity_to_add} "
                f"(Product ID: {product.id})"
            )

    def remove_item(self, product: Product, quantity_to_remove : int) -> None:
        LOGGER.info(f"Remove request: {quantity_to_remove} x {product.name}")

        if quantity_to_remove < 1:
            LOGGER.error(
                f"Invalid removal quantity {quantity_to_remove} "
                f"for product {product.name}"
            )
            raise ValueError("The quantity of product you want to remove must be greater than zero")
        
        
        if product.id in self.__items:
            cart_item : CartItem = self.__items[product.id]

            if cart_item.quantity < quantity_to_remove:
                LOGGER.error(
                    f"Cart item removal failed: attempted to remove {quantity_to_remove} {product.name}"
                    f"but only {cart_item.quantity} in cart"
                )
                raise ValueError("The quantity to remove exceeds the products in the cart")
            
            elif cart_item.quantity == quantity_to_remove:

                removed_item : CartItem = self.__items.pop(product.id)
            
                LOGGER.info(
                    f"Cart item removed: All {product.name} removed "
                    f"(Product ID: {product.id})"
                )
            else: 
                cart_item.decrease_quantity(quantity_to_remove)
                LOGGER.info(
                    f"Cart updated: Removed {quantity_to_remove} x {product.name}. "
                    f"Remaining quantity: {cart_item.quantity}. "
                    f"(Product ID: {product.id})"
                )

        else:
            LOGGER.warning(
                f"Attempted to remove item not in cart: {product.name} "
                f"(Product ID: {product.id})"
            )