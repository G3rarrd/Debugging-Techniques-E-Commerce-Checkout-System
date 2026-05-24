from decimal import Decimal, getcontext

import logging
from logging import Logger

from models.cart import Cart
from models.order import Order

getcontext().prec = 28
LOGGER : Logger = logging.getLogger(__name__) # Helps identify the logs are coming from.

class Checkout:
    def __init__(self, cart : Cart, discount : Decimal):
        self.__cart : Cart = cart
        self.__discount_price_threshold : Decimal = Decimal("1000")
        self.__discount_price : Decimal = discount
    
    @property
    def cart(self) -> Cart:
        return self.__cart
    
    @property
    def discount_price_threhold(self)-> Decimal:
        return self.__discount_price_threshold
    
    @property
    def discount_price(self) -> Decimal:
        return self.__discount_price

    def __apply_discount(self, total_price : Decimal):
        if total_price > self.__discount_price_threshold:
            return total_price * (Decimal("1.00") - self.__discount_price)
        return total_price
    
    def __validate_stock(self) -> None :
        for item in self.__cart.items.values():
            if item.quantity > item.product.stock_quantity:
                LOGGER.error(
                    f"Stock validation failed: "
                    f"requested {item.quantity} x {item.product.name}, "
                    f"but only {item.product.stock_quantity} available "
                    f"(Product ID: {item.product.id})"
                )

                raise ValueError(f"Insufficient Stock for product {item.product.name}")
    
    def __deduct_stock(self) -> int:
        total_cart_item_removed : int = 0
        for cart_item in self.__cart.items.values():
            total_cart_item_removed += cart_item.quantity
            cart_item.product.remove_stock(cart_item.quantity)

        return total_cart_item_removed

    
    def process(self) -> Order:
        self.__validate_stock()

        cart_total : Decimal = self.__cart.total
        final_price : Decimal = self.__apply_discount(cart_total)


        deducted_count : int = self.__deduct_stock()
        breakpoint()
        purchased_item_log = {
            pid : item.quantity 
            for pid, item in self.__cart.items.items()
        }
        LOGGER.info(f"[CHECKOUT PROCESSED SUCCESSFULLY]: {deducted_count} items sold")
        return Order(purchased_item_log, final_price, self.__discount_price)