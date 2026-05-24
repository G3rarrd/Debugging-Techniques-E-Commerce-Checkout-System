from decimal import Decimal, getcontext

import uuid
from uuid import UUID

import logging
from logging import Logger

getcontext().prec = 28
LOGGER : Logger = logging.getLogger(__name__) # Helps identify the logs are coming from.

class Product:
    def __init__(self, name: str, description: str, price: Decimal, stock_quantity : int):
        self.__name : str = name
        self.__price : Decimal = price
        self.__description : str = description
        self.__stock_quantity : int = stock_quantity
        self.__id : UUID = uuid.uuid4()

        LOGGER.info(   
            "[PRODUCT CREATED] | "
            f"id={self.__id} | "
            f"name={self.__name} | "
            f"price={self.__price} | "
            f"stock={self.__stock_quantity}"
        )

    @property
    def price(self):
        return self.__price
    
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def stock_quantity(self):
        return self.__stock_quantity
    
    @property
    def id(self):
        return self.__id
    
    def __repr__(self):
        return (
            f"Product("
            f"id={self.__id}, "
            f"name={self.__name!r}, "
            f"price={self.__price}, "
            f"stock={self.__stock_quantity}"
            f")"
        )

    
    def __str__(self):
        return f"Product(name={self.__name}, price={self.__price}, stock={self.__stock_quantity}, description={self.__description})"
    
    def remove_stock(self, count : int) -> None:
        action : str = "Stock removal"
        if count < 1:
            LOGGER.error(f"{action} failed: invalid removal count {count} for product {self.__name}")
            raise ValueError("Removal count must be greater than zero")
        
        
        if count > self.__stock_quantity:
            LOGGER.error(f"{action} failed: Unable to remove {count} {self.__name} as only {self.__stock_quantity} is available")
            raise ValueError("Removal count exceeds the stock available")
            
        self.__stock_quantity -= count
        LOGGER.info(
            f"{action} successful: "
            f"{self.__name} x{count} removed from stock. "
            f"{self.__stock_quantity} remaining."
        )

    def add_stock(self, count : int) -> None:
        action : str = "Stock addition"
        if count < 1:
            LOGGER.error(
                f"{action} failed: "
                f"Invalid addtion count of {count} "
                f"for {self.__name}"
            )
            raise ValueError("Invalid stock input. Added stock must be greater than 0")
        
        self.__stock_quantity += count

        LOGGER.info(
            f"{action} successful: "
            f"{count} x {self.__name} added to stock. "
            f"{self.__stock_quantity} available."
        )