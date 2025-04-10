def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user outside the function
price = float(input("Enter the original price of the item (e.g. 1000): "))
discount_percent = float(input("Enter the discount percentage (e.g. 25): "))

# Call the function and display the result
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"The discount is {discount_percent}%.\nOriginal price: {price}\nDiscounted price: {final_price}")
else:
    print(f"No discount applied.\nFinal price: {price}")
