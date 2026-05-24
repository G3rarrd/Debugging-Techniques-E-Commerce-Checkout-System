# E-Commerce Checkout System with Debugging Techniques

## Project Overview

This project is a simplified **E-Commerce Checkout System** built in Python using Object-Oriented Programming principles.

The system simulates:

* Product management
* Shopping cart operations
* Checkout processing
* Stock validation and deduction
* Discount application
* Order generation

The project also demonstrates the use of:

* Python logging using the `logging` library
* Debugging with `pdb` using `breakpoint()`
* Error handling using `raise`

---

# Features

## Product Management

* Create products with:

  * name
  * description
  * price
  * stock quantity
* Add stock
* Remove stock
* Stock validation

---

## Cart System

* Add products to cart
* Remove products from cart
* Update quantities
* Calculate subtotals
* Calculate cart totals

---

## Checkout System

* Validate stock before checkout
* Apply discounts
* Deduct stock after successful checkout
* Generate order summary

---

## Logging

The project uses Python's built-in `logging` module to record:

* Cart updates
* Checkout operations
* Stock deductions
* Errors and invalid operations

Example log output:

```text
INFO | models.cart | Cart updated: Added Laptop x2
INFO | models.checkout | [CHECKOUT PROCESSED SUCCESSFULLY]: 3 items sold
ERROR | models.checkout | Invalid discount configuration detected
```

---

# Debugging with pdb

The project demonstrates debugging using Python's built-in debugger (`pdb`).

A debugging scenario was intentionally created using an incorrect discount value.

## Bug Scenario

Incorrect discount value:

```python
discount=Decimal("10.00")
```

Correct discount value:

```python
discount=Decimal("0.10")
```

The bug caused the final checkout total to become negative.

---

## Debugging Process

A `breakpoint()` was placed inside:

```python
Checkout.process()
```

Variables inspected during debugging:

```python
cart_total
final_price
self.cart
```

Example pdb session:
## Debugging session without bug
![PDB Debugging session without bug](https://github.com/G3rarrd/Debugging-Techniques-E-Commerce-Checkout-System/blob/main/readme_assests/pdb_without_bug.png)

## Debugging session with bug
![PDB Debugging session with bug](https://github.com/G3rarrd/Debugging-Techniques-E-Commerce-Checkout-System/blob/main/readme_assests/pdb_with_bug.png)

# Project Structure

```text
Debugging_Techniques/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── cart_item.py
│   ├── cart.py
│   ├── checkout.py
│   └── order.py
```


# Learning Outcomes

* Logging and monitoring
* Runtime debugging
* Error handling
* State inspection

---

# Running the Project

## Clone the repository

```bash
git clone https://github.com/G3rarrd/Debugging-Techniques-E-Commerce-Checkout-System
```

---

## Environment Setup
- This project uses the venv environment
```bash
python -m venv venv # setups environment
venv/scripts/activate # launches environment
```

## Run the application

```bash
python main.py
```

---
