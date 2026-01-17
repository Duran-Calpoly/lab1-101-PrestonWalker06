def calculate_average (num1, num2, num3):
    return (num1 + num2 + num3) / 3
num1 = 3
num2 = 4
num3 = 5
average1 = calculate_average (num1, num2, num3)

def add_tax (bill_total):
    return (bill_total * 1.1)
bill_total = 40
bill_with_tax = add_tax (bill_total)

def greet_user (name):
    return (f"Hello {name}")
greeting_Alice = greet_user ("Alice")
