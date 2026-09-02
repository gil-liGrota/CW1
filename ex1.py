store_stock = {
    "book": {"price": 50, "quantity": 10},
    "notebook": {"price": 15, "quantity": 5},
    "pen": {"price": 5, "quantity": 20},
    "bag": {"price": 120, "quantity": 2}
}

applied_coupons = []


def check_stock(item_name, qty):
    if item_name in store_stock:
        if store_stock[item_name]["quantity"] >= qty:
            return True
    return False


def add_to_cart(cart, item_name, qty):
    clean_name = item_name.strip().lower()

    if not check_stock(clean_name, qty):
        print(f"Not enough stock for {item_name}!")
        return cart

    if clean_name in cart.keys():
        cart[clean_name] = qty + cart[clean_name]
    else:
        cart[clean_name] = qty
    return cart


def apply_coupon_code(code, current_total):
    global applied_coupons

    if code in applied_coupons:
        print("Coupon is already applied!")
        return current_total

    discount = 0
    if code == "SAVE10":
        discount = 0.1
    elif code == "VIP20":
        discount = 0.2

    applied_coupons.append(code)

    final_price = current_total - (current_total * discount)
    return final_price


def process_checkout(cart, coupon_code=""):
    total_price = 0
    items_to_remove = []

    for item, qty in cart.items():
        price = store_stock[item]["price"]
        total_price += price * qty


    if coupon_code != "":
        total_price = apply_coupon_code(coupon_code, total_price)

    return total_price


def remove_from_cart(cart):
    for item, qty in cart.items():
        store_stock[item]["quantity"] -= qty

def print_receipt(customer_name, cart, final_price):
    print("=" * 30)
    print("Receipt for:", customer_name)

    remove_from_cart(cart)

    for item, qty in cart.items():
        item_count = qty
        print(f"- {item} x{qty}")

    if item_count > 0:
        avg_price = final_price / item_count

    print(f"Total to pay: ${final_price}")
    print(f"Average price per item: ${avg_price:.2f}")
    print("=" * 30)


# check run
cart1 = {}
cart1 = add_to_cart(cart1, " Book ", 2)
cart1 = add_to_cart(cart1, "book", 1)  # כעת יעלה את הכמות ל-3

price1 = process_checkout(cart1, coupon_code="SAVE10")
print_receipt("ישראל", cart1, price1)

# לקוח שני שמנסה להשתמש באותו קופון - הקופון ייחסם
cart2 = {}
cart2 = add_to_cart(cart2, "pen", 5)
price2 = process_checkout(cart2, coupon_code="SAVE10")
print_receipt("דנה", cart2, price2)