from decimal import Decimal, getcontext
import logging

# Models
from models.cart_item import CartItem
from models.product import Product
from models.checkout import Checkout
from models.cart import Cart
from models.order import Order

getcontext().prec = 28
# Global configuration for pyhon logging system setup
# Formatted the output log for readability
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s"
) 

def pipeline_without_bug():
    # Product
    # Product creation
    laptop : Product = Product(
        name="Laptop", 
        description="Portable PC", 
        price=Decimal("1000"), 
        stock_quantity=3
    )

    phone : Product = Product(
        name="Phone", 
        description="Handheld Device", 
        price=Decimal("250"), 
        stock_quantity=10
    )

    # Cart
    cart : Cart = Cart()
    cart.add_item(laptop, 2)
    cart.add_item(phone, 1)

    # Checkout
    checkout : Checkout = Checkout(
        cart=cart,  
        discount=Decimal("0.10")
    )
    order : Order = checkout.process()
    print(order)
    
    laptop.add_stock(3) # Replenish stock
        
def pipeline_with_bug():
    # Product
    # Product creation
    laptop : Product = Product(
        name="Laptop", 
        description="Portable PC", 
        price=Decimal("1000"), 
        stock_quantity=3
    )

    phone : Product = Product(
        name="Phone", 
        description="Handheld Device", 
        price=Decimal("250"), 
        stock_quantity=10
    )

    # Cart
    cart : Cart = Cart()
    cart.add_item(laptop, 2)
    cart.add_item(phone, 1)

    # Checkout
    # The pdb was used in the ./models/checkout.py file to check for 
    # the discounted price and original price of all the cart items 
    checkout : Checkout = Checkout(
        cart=cart,  
        discount=Decimal("10.00")
    )
    # Bug: the value of the discount is meant to be stored as 
    # decimal fraction not percentage
    # Possible Fix: raise error in the checkout class if 
    # the discount is not within the ranges 0.0 to 1.0
    # to prevent purchases from being made

    order : Order = checkout.process()
    print(order)
    
    laptop.add_stock(3) # Replenish stock
        

def main():
    pipeline_with_bug()
    
    


if "__main__" == __name__:
    main()
