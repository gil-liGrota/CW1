visitor_age = 70
visitor_height = 150
is_vip = True

ticket_price = 80

if visitor_height >= 140 and visitor_age >= 12:
    if is_vip:
        status = "Allowed to ride with VIP Fast Pass!"
    else:
        status = "Allowed to ride!"
else:
    status = "Access Denied"
    status = "Sorry, you cannot ride the roller coaster."

if visitor_age < 6:
    ticket_price = 0
elif visitor_age < 65:
    ticket_price = ticket_price
else:
    ticket_price = ticket_price


print("--- Visitor Report ---")
print("Age:", visitor_age)
print("Height:", visitor_height)
print("Ticket Price:", ticket_price)
print("Ride Status:", status)